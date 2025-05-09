# onelogin-python-sdk

Python SDK for OneLogin API

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

# Defining the host is optional and defaults to https://your-api-subdomain.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = onelogin.Configuration(
    host = "https://your-api-subdomain.onelogin.com"
)

configuration = onelogin.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
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

## Documentation For Authorization

## OAuth2

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: 
 - **Authentication Only**: Gives the credential pair the ability to generate an access token that can perform POST calls only to authentication endpoints, providing least privileged access to authentication code. These endpoints include:   - Verify Factor (SAML Assertion)   - Generate SAML Assertion   - Verify Factor (Login)   - Create Session Login Token   - Log User Out
 - **Read Users**: Gives the credential pair the ability to generate an access token that can perform GET calls available for the User, Role, and Group API resources.
 - **Manage users**: Gives the credential pair the ability to generate an access token that can perform GET, POST, PUT, and DELETE calls available for the User, Role, and Group API resources, with the exception of setting passwords and assigning and removing roles
 - **Manage All**: Gives the credential pair the ability to generate an access token that can perform GET, POST, PUT, and DELETE calls for all available API resources, including the ability to set passwords and assign and remove roles.
 - **Read All**: Gives the credential pair the ability to generate an access token that can perform GET calls available for all API resources.

- **Type**: HTTP basic authentication

## basicAuth

- **Type**: HTTP basic authentication
