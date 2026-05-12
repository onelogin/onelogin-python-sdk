# Changelog

## 4.0.0 (2026-05-12)

### Breaking Changes

This release removes six orphan model classes that the original OpenAPI Generator
produced but no SDK API method ever deserialized into, accepted as input, or composed
into a live model. They have been re-exported from `onelogin/__init__.py` historically,
so any user importing them directly (e.g. `from onelogin import Verb`) will need to
update or pin to a `3.x` release.

The audit that surfaced these is documented in the broader maintainability sweep that
accompanied PRs #127-#131; this is the final cleanup before the public surface stops
advertising types that no endpoint exercises.

**Removed classes**:

- `CreatePrivilege200Response` — the live `create_privilege` endpoint returns
  `Privilege` directly; this model was never bound to that endpoint.
- `ListPrivelegeRoles200Response` — misspelled twin of the live
  `ListPrivilegeRoles200Response` (note "Privilege" vs "Privelege"); generator
  artifact.
- `Locale` — never referenced by any endpoint or composed by any other model.
- `OidcAppAllOf` — OpenAPI Generator `allOf` inheritance artifact; the
  user-facing `OidcApp` class is still present and live (via
  `CreateAppRequest`'s `oneOf` variants).
- `SamlAppAllOf` — same as above for `SamlApp`.
- `Verb` — generated event-type enum; no endpoint emitted or consumed it.

**Workaround** for anyone importing these directly: pin to `onelogin~=3.2` until
you can audit your call sites.

## 3.2.8 (2026-05-12)

### Bug Fixes

- **`update_mapping`** (`PUT /api/2/mappings/{mapping_id}`): Updating a mapping to set
  `status` to `disabled` (i.e. `enabled: false`) failed with a pydantic `ValidationError`
  because the API returns `null` for `position` on disabled mappings, but `position` was
  typed as the required non-nullable `StrictInt`. `position` is now
  `Optional[StrictInt]` (defaulting to `None`), so disabled-mapping responses
  deserialize correctly. The existing `exclude_none=True` in `to_dict` ensures `null`
  positions are omitted from update request bodies, preventing the API's 422
  "Position cannot be set while the mapping is not enabled" error.

## 3.2.7 (2026-05-07)

### Bug Fixes

- **`create_mapping`** (`POST /api/2/mappings`): Successful creates were raising
  `pydantic.ValidationError` because the API returns a partial payload (`{"id": ...}`)
  while `Mapping` requires `name`, `enabled`, `match`, `position`, `conditions`, and
  `actions`. `Mapping.from_dict` now keeps strict validation as the default but falls
  back to `model_construct` for the narrow id-only case, so successful creates return
  a `Mapping` with `id` populated instead of raising. All other malformed/partial
  payloads (including `{"id": null}`) still raise the original `ValidationError`.
  Callers that need the full mapping should follow up with `get_mapping(result.id)`.

## 3.2.6 (2026-05-06)

### Bug Fixes

- **`create_role`** (`POST /api/2/roles`): Fixed a pydantic `ValidationError` that occurred
  when the SDK tried to deserialize the 201 response. The API returns a single object
  `{"id": ...}`, but the SDK had declared the return type as `List[CreateRole201ResponseInner]`.
  The deserializer iterated over the dict keys, passing the string `'id'` to `from_dict`,
  which pydantic rejected. The return type is now correctly `CreateRole201ResponseInner`.

- **`create_mapping`** (`POST /api/2/mappings`): Fixed the same class of bug. The API returns
  a single `Mapping` object, but the SDK had declared `List[Mapping]`. This also led to user
  confusion: the `'id'` string in the error message was misread as a required field, causing
  users to include `id` in the request body, which the server rejected with
  `"Field is not allowed"`. The return type is now correctly `Mapping`.

### Other Changes

- Replaced all uses of the deprecated Pydantic v2 `parse_obj` method with `model_validate`
  and all uses of `self.dict()` with `self.model_dump()` across all model files, eliminating
  all remaining deprecated Pydantic v2 API usage in the models package.
