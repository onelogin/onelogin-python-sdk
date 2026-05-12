# onelogin-python-sdk

Official Python SDK for the OneLogin API. Manage users, roles, groups, apps, and authentication programmatically.

API reference: [OneLogin API Documentation](https://developers.onelogin.com/api-docs/2/getting-started/dev-overview).
Per-endpoint docs: see [`docs/`](docs/) in this repo.

## Support

OneLogin by One Identity open-source projects are supported through GitHub. For help, please open an issue: <https://github.com/onelogin/onelogin-python-sdk/issues>. Requests filed via official One Identity Support are redirected here so all users can benefit.

## Requirements

- Python 3.10+
- Pydantic 2.11+ (enforced via `pyproject.toml`)

## Installation

```sh
pip install onelogin
```

For development:

```sh
pip install -e ".[test,lint]"
```

## Getting Started

```python
import os
import onelogin
from pprint import pprint

configuration = onelogin.Configuration(
    host="https://your-subdomain.onelogin.com",
    username=os.environ["ONELOGIN_CLIENT_ID"],
    password=os.environ["ONELOGIN_CLIENT_SECRET"],
)

with onelogin.ApiClient(configuration) as api_client:
    # Exchange client credentials for an access token.
    token_api = onelogin.OAuth2Api(api_client)
    token = token_api.generate_token({"grant_type": "client_credentials"})
    configuration.access_token = token.access_token

    # Now make authenticated calls.
    users_api = onelogin.UsersV2Api(api_client)
    pprint(users_api.list_users2())
```

## Authentication

OneLogin uses OAuth2 client credentials. Generate a Client ID + Client Secret under **Security → API Credentials** in the OneLogin admin portal, with one of:

- **Authentication Only** — Verify Factor, Generate SAML Assertion, Create Session Login Token, Log User Out
- **Read Users** — `GET` on User, Role, Group resources
- **Manage Users** — `GET`/`POST`/`PUT`/`DELETE` on User, Role, Group (no password management or role assignment)
- **Read All** — read-only across all resources
- **Manage All** — full access including password management and role assignment

## Tests

```sh
pip install -e ".[test]"
pytest
```

## Troubleshooting

- **`ImportError: cannot import name validate_call from pydantic`** — Pydantic <2.11 in your environment. Run `pip install -U pydantic`.
- **`ValidationError` on response deserialization** — likely a server-returned `null` for a field the SDK still types as required. Open an issue with the endpoint and a redacted response sample; this class of fix is straightforward (see PR #126, #131 for examples).
- **Connection issues** — confirm your subdomain in the `host` URL, that your credentials carry the right scope, and that your network can reach `*.onelogin.com`.

## Release Process (Maintainers)

Releases ship to PyPI automatically when you publish a GitHub Release. The publish workflow runs `sed -i` against `pyproject.toml` and `onelogin/__init__.py` *inside the CI runner* to set the version from the tag — those edits are **not committed back to `main`**, so the source tree may lag the latest PyPI release. Reconcile periodically with a manual version bump PR.

1. Open the [Releases page](../../releases) and click **Draft a new release**
2. Create a tag matching the version, e.g. `3.2.9` (no `v` prefix; matches releases 3.2.4 onward)
3. Set title to the version and paste the CHANGELOG entry into the description
4. **Publish release** — `.github/workflows/python-publish.yml` builds and uploads to PyPI

If a release fails to upload, re-run the failed workflow from the Actions tab; the build is idempotent up to the point of `twine upload`.
