<a id="__pageTop"></a>
# onelogin.apis.tags.api_authorization_server_api.APIAuthorizationServerApi

All URIs are relative to *https://your-api-subdomain.onelogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_auth_server**](#create_auth_server) | **post** /api/2/api_authorizations | Create Api Auth Server
[**delete_auth_server**](#delete_auth_server) | **delete** /api/2/api_authorizations/{api_auth_id} | Delete Api Auth Server
[**get_auth_server**](#get_auth_server) | **get** /api/2/api_authorizations/{api_auth_id} | Get Api Auth Server
[**list_auth_servers**](#list_auth_servers) | **get** /api/2/api_authorizations | List Api Auth Servers
[**update_auth_server**](#update_auth_server) | **put** /api/2/api_authorizations/{api_auth_id} | Update Api Auth Server

# **create_auth_server**
<a id="create_auth_server"></a>
> AuthServer create_auth_server()

Create Api Auth Server

Create Auth Server

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import api_authorization_server_api
from onelogin.model.auth_server import AuthServer
from onelogin.model.alt_err import AltErr
from pprint import pprint
# Defining the host is optional and defaults to https://your-api-subdomain.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = onelogin.Configuration(
    host = "https://your-api-subdomain.onelogin.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = onelogin.Configuration(
    host = "https://your-api-subdomain.onelogin.com",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with onelogin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api_authorization_server_api.APIAuthorizationServerApi(api_client)

    # example passing only optional values
    header_params = {
        'Content-Type': "application/json",
    }
    body = AuthServer(
        id=1022697,
        name="Contacts API",
        description="API manages contacts",
        configuration=AuthServerConfiguration(
            audiences=[
                "audiences_example"
            ],
            refresh_token_expiration_minutes=30,
            resource_identifier="https://example.com/contacts",
            access_token_expiration_minutes=20,
        ),
    )
    try:
        # Create Api Auth Server
        api_response = api_instance.create_auth_server(
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling APIAuthorizationServerApi->create_auth_server: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthServer**](../../models/AuthServer.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Content-Type | ContentTypeSchema | | optional

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "application/json"

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_auth_server.ApiResponseFor200) | Successful response
401 | [ApiResponseFor401](#create_auth_server.ApiResponseFor401) | Unauthorized
422 | [ApiResponseFor422](#create_auth_server.ApiResponseFor422) | Unprocessable Entity

#### create_auth_server.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthServer**](../../models/AuthServer.md) |  | 


#### create_auth_server.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


#### create_auth_server.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_auth_server**
<a id="delete_auth_server"></a>
> delete_auth_server(api_auth_id)

Delete Api Auth Server

Delete Authentication Server

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import api_authorization_server_api
from onelogin.model.alt_err import AltErr
from pprint import pprint
# Defining the host is optional and defaults to https://your-api-subdomain.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = onelogin.Configuration(
    host = "https://your-api-subdomain.onelogin.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = onelogin.Configuration(
    host = "https://your-api-subdomain.onelogin.com",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with onelogin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api_authorization_server_api.APIAuthorizationServerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'api_auth_id': "api_auth_id_example",
    }
    header_params = {
    }
    try:
        # Delete Api Auth Server
        api_response = api_instance.delete_auth_server(
            path_params=path_params,
            header_params=header_params,
        )
    except onelogin.ApiException as e:
        print("Exception when calling APIAuthorizationServerApi->delete_auth_server: %s\n" % e)

    # example passing only optional values
    path_params = {
        'api_auth_id': "api_auth_id_example",
    }
    header_params = {
        'Content-Type': "application/json",
    }
    try:
        # Delete Api Auth Server
        api_response = api_instance.delete_auth_server(
            path_params=path_params,
            header_params=header_params,
        )
    except onelogin.ApiException as e:
        print("Exception when calling APIAuthorizationServerApi->delete_auth_server: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Content-Type | ContentTypeSchema | | optional

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "application/json"

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
api_auth_id | ApiAuthIdSchema | | 

# ApiAuthIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_auth_server.ApiResponseFor204) | Success. The auth server is deleted. No content is returned.
401 | [ApiResponseFor401](#delete_auth_server.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#delete_auth_server.ApiResponseFor404) | Not Found

#### delete_auth_server.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_auth_server.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


#### delete_auth_server.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_auth_server**
<a id="get_auth_server"></a>
> AuthServer get_auth_server(api_auth_id)

Get Api Auth Server

Get Authorization Server

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import api_authorization_server_api
from onelogin.model.auth_server import AuthServer
from onelogin.model.alt_err import AltErr
from pprint import pprint
# Defining the host is optional and defaults to https://your-api-subdomain.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = onelogin.Configuration(
    host = "https://your-api-subdomain.onelogin.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = onelogin.Configuration(
    host = "https://your-api-subdomain.onelogin.com",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with onelogin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api_authorization_server_api.APIAuthorizationServerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'api_auth_id': "api_auth_id_example",
    }
    header_params = {
    }
    try:
        # Get Api Auth Server
        api_response = api_instance.get_auth_server(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling APIAuthorizationServerApi->get_auth_server: %s\n" % e)

    # example passing only optional values
    path_params = {
        'api_auth_id': "api_auth_id_example",
    }
    header_params = {
        'Content-Type': "application/json",
    }
    try:
        # Get Api Auth Server
        api_response = api_instance.get_auth_server(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling APIAuthorizationServerApi->get_auth_server: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Content-Type | ContentTypeSchema | | optional

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "application/json"

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
api_auth_id | ApiAuthIdSchema | | 

# ApiAuthIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_auth_server.ApiResponseFor200) | Successful response
401 | [ApiResponseFor401](#get_auth_server.ApiResponseFor401) | Unauthorized

#### get_auth_server.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthServer**](../../models/AuthServer.md) |  | 


#### get_auth_server.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_auth_servers**
<a id="list_auth_servers"></a>
> [AuthServer] list_auth_servers()

List Api Auth Servers

List Authorization Servers

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import api_authorization_server_api
from onelogin.model.auth_server import AuthServer
from onelogin.model.alt_err import AltErr
from pprint import pprint
# Defining the host is optional and defaults to https://your-api-subdomain.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = onelogin.Configuration(
    host = "https://your-api-subdomain.onelogin.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = onelogin.Configuration(
    host = "https://your-api-subdomain.onelogin.com",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with onelogin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api_authorization_server_api.APIAuthorizationServerApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Api Auth Servers
        api_response = api_instance.list_auth_servers()
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling APIAuthorizationServerApi->list_auth_servers: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_auth_servers.ApiResponseFor200) | Successful response
401 | [ApiResponseFor401](#list_auth_servers.ApiResponseFor401) | Unauthorized

#### list_auth_servers.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**AuthServer**]({{complexTypePrefix}}AuthServer.md) | [**AuthServer**]({{complexTypePrefix}}AuthServer.md) | [**AuthServer**]({{complexTypePrefix}}AuthServer.md) |  | 

#### list_auth_servers.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_auth_server**
<a id="update_auth_server"></a>
> AuthServer update_auth_server(api_auth_id)

Update Api Auth Server

Update Authorization Server

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import api_authorization_server_api
from onelogin.model.auth_server import AuthServer
from onelogin.model.alt_err import AltErr
from pprint import pprint
# Defining the host is optional and defaults to https://your-api-subdomain.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = onelogin.Configuration(
    host = "https://your-api-subdomain.onelogin.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: OAuth2
configuration = onelogin.Configuration(
    host = "https://your-api-subdomain.onelogin.com",
    access_token = 'YOUR_ACCESS_TOKEN'
)
# Enter a context with an instance of the API client
with onelogin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = api_authorization_server_api.APIAuthorizationServerApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'api_auth_id': "api_auth_id_example",
    }
    header_params = {
    }
    try:
        # Update Api Auth Server
        api_response = api_instance.update_auth_server(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling APIAuthorizationServerApi->update_auth_server: %s\n" % e)

    # example passing only optional values
    path_params = {
        'api_auth_id': "api_auth_id_example",
    }
    header_params = {
        'Content-Type': "application/json",
    }
    body = AuthServer(
        id=1022697,
        name="Contacts API",
        description="API manages contacts",
        configuration=AuthServerConfiguration(
            audiences=[
                "audiences_example"
            ],
            refresh_token_expiration_minutes=30,
            resource_identifier="https://example.com/contacts",
            access_token_expiration_minutes=20,
        ),
    )
    try:
        # Update Api Auth Server
        api_response = api_instance.update_auth_server(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling APIAuthorizationServerApi->update_auth_server: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthServer**](../../models/AuthServer.md) |  | 


### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Content-Type | ContentTypeSchema | | optional

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "application/json"

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
api_auth_id | ApiAuthIdSchema | | 

# ApiAuthIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_auth_server.ApiResponseFor200) | Successful response
401 | [ApiResponseFor401](#update_auth_server.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#update_auth_server.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#update_auth_server.ApiResponseFor422) | Unprocessable Entity

#### update_auth_server.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthServer**](../../models/AuthServer.md) |  | 


#### update_auth_server.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


#### update_auth_server.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


#### update_auth_server.ApiResponseFor422
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor422ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor422ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

