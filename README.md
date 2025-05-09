# onelogin-python-sdk

Official Python SDK for the OneLogin API, enabling you to programmatically manage users, roles, groups, and authentication in your OneLogin instance.

For more information about the OneLogin API, visit the [OneLogin API Documentation](https://developers.onelogin.com/api-docs/2/getting-started/dev-overview).

## Support
OneLogin by One Identity open source projects are supported through [OneLogin GitHub issues](https://github.com/onelogin/onelogin-python-sdk/issues). This includes all scripts, plugins, SDKs, modules, code snippets or other solutions. For assistance with any OneLogin by One Identity GitHub project, please raise a new Issue on the [OneLogin GitHub issues](https://github.com/onelogin/onelogin-python-sdk/issues) page. Requests for assistance made through official One Identity Support will be referred back to GitHub where those requests can benefit all users.

## Requirements.

Python 3.7+

## Installation & Usage

### pip install

You can install directly using pip:

```sh
pip install onelogin
```

For development and testing, install with test dependencies:

```sh
pip install onelogin[test]
```

Then import the package:

```python
import onelogin
```

### Tests

First, install the package with test dependencies:

```sh
pip install -e .[test]
```

Then run the tests:

```sh
pytest
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import os
import onelogin
from onelogin.rest import ApiException
from pprint import pprint

# Set up configuration
# Replace 'your-subdomain' with your actual OneLogin subdomain
configuration = onelogin.Configuration(
    host = "https://your-subdomain.onelogin.com"
)

# Set your API credentials
# Use environment variables to avoid hardcoding credentials
configuration = onelogin.Configuration(
    username = os.environ["ONELOGIN_CLIENT_ID"],
    password = os.environ["ONELOGIN_CLIENT_SECRET"]
)

# Enter a context with an instance of the API client
with onelogin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    token_instance = onelogin.OAuth2Api(api_client)
    generate_token_request = {"grant_type":"client_credentials"} # GenerateTokenRequest | Request Body to Generate OAuth Token
    content_type="application/json"
    try:
        # Generate and Save Access Token
        api_response = token_instance.generate_token(generate_token_request, content_type=content_type)
        configuration.access_token = api_response.access_token
        print(configuration.access_token)
    except Exception as e:
        print("Exception when generating access token: %s\n" % e)

    user_instance = onelogin.UsersV2Api(api_client)
    try:
        # List Users
        api_response = user_instance.list_users2()
        print("The response of UsersV2Api->list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV2Api->list_users: %s\n" % e)


```

## Authentication

### OAuth2

OneLogin API uses OAuth2 for authorization. Your client credentials (Client ID and Client Secret) are used to request an access token, which is then used for subsequent API calls.

#### Available Scopes

The OneLogin API supports the following scopes:

- **Authentication Only**: Access to authentication endpoints only (Verify Factor, Generate SAML Assertion, Create Session Login Token, Log User Out)
- **Read Users**: Access to GET calls for User, Role, and Group API resources
- **Manage Users**: Access to GET, POST, PUT, and DELETE calls for User, Role, and Group API resources (except password management and role assignment)
- **Manage All**: Full access to all API resources, including password management and role assignment
- **Read All**: Read-only access to all API resources

You can set up your API credentials with appropriate scopes in the OneLogin portal under Security > API Credentials.
