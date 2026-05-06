# Changelog

## 3.2.3 (2026-05-06)

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
  across all model files.
