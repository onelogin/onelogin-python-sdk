<a id="__pageTop"></a>
# onelogin.apis.tags.api_auth_scopes_api.APIAuthScopesApi

All URIs are relative to *https://your-api-subdomain.onelogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_scope**](#create_scope) | **post** /api/2/api_authorizations/{api_auth_id}/scopes | Create Api Auth Server Scope
[**delete_scope**](#delete_scope) | **delete** /api/2/api_authorizations/{api_auth_id}/scopes/{scope_id} | Delete Api Auth Server Scope
[**get_scopes**](#get_scopes) | **get** /api/2/api_authorizations/{api_auth_id}/scopes | Get Api Auth Server Scopes
[**update_scope**](#update_scope) | **put** /api/2/api_authorizations/{api_auth_id}/scopes/{scope_id} | Update Api Auth Server Scope

# **create_scope**
<a id="create_scope"></a>
> AuthScope create_scope(api_auth_id)

Create Api Auth Server Scope

Create API Auth Server Scope

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import api_auth_scopes_api
from onelogin.model.auth_scope import AuthScope
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
    api_instance = api_auth_scopes_api.APIAuthScopesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'api_auth_id': "api_auth_id_example",
    }
    header_params = {
    }
    try:
        # Create Api Auth Server Scope
        api_response = api_instance.create_scope(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling APIAuthScopesApi->create_scope: %s\n" % e)

    # example passing only optional values
    path_params = {
        'api_auth_id': "api_auth_id_example",
    }
    header_params = {
        'Content-Type': "application/json",
    }
    body = AuthScope(
        id=323005,
        value="custom:scope",
        description="A custom scope",
    )
    try:
        # Create Api Auth Server Scope
        api_response = api_instance.create_scope(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling APIAuthScopesApi->create_scope: %s\n" % e)
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
[**AuthScope**](../../models/AuthScope.md) |  | 


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
200 | [ApiResponseFor200](#create_scope.ApiResponseFor200) | Successful response
401 | [ApiResponseFor401](#create_scope.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#create_scope.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#create_scope.ApiResponseFor422) | Unprocessable Entity

#### create_scope.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthScope**](../../models/AuthScope.md) |  | 


#### create_scope.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


#### create_scope.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


#### create_scope.ApiResponseFor422
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

# **delete_scope**
<a id="delete_scope"></a>
> delete_scope(api_auth_idscope_id)

Delete Api Auth Server Scope

Delete Scope

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import api_auth_scopes_api
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
    api_instance = api_auth_scopes_api.APIAuthScopesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'api_auth_id': "api_auth_id_example",
        'scope_id': 1,
    }
    header_params = {
    }
    try:
        # Delete Api Auth Server Scope
        api_response = api_instance.delete_scope(
            path_params=path_params,
            header_params=header_params,
        )
    except onelogin.ApiException as e:
        print("Exception when calling APIAuthScopesApi->delete_scope: %s\n" % e)

    # example passing only optional values
    path_params = {
        'api_auth_id': "api_auth_id_example",
        'scope_id': 1,
    }
    header_params = {
        'Content-Type': "application/json",
    }
    try:
        # Delete Api Auth Server Scope
        api_response = api_instance.delete_scope(
            path_params=path_params,
            header_params=header_params,
        )
    except onelogin.ApiException as e:
        print("Exception when calling APIAuthScopesApi->delete_scope: %s\n" % e)
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
scope_id | ScopeIdSchema | | 

# ApiAuthIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ScopeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_scope.ApiResponseFor204) | Success. The scope is deleted. No content is returned.
401 | [ApiResponseFor401](#delete_scope.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#delete_scope.ApiResponseFor404) | Not Found

#### delete_scope.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_scope.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


#### delete_scope.ApiResponseFor404
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

# **get_scopes**
<a id="get_scopes"></a>
> [AuthScope] get_scopes(api_auth_id)

Get Api Auth Server Scopes

List Authorization Scopes

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import api_auth_scopes_api
from onelogin.model.auth_scope import AuthScope
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
    api_instance = api_auth_scopes_api.APIAuthScopesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'api_auth_id': "api_auth_id_example",
    }
    header_params = {
    }
    try:
        # Get Api Auth Server Scopes
        api_response = api_instance.get_scopes(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling APIAuthScopesApi->get_scopes: %s\n" % e)

    # example passing only optional values
    path_params = {
        'api_auth_id': "api_auth_id_example",
    }
    header_params = {
        'Content-Type': "application/json",
    }
    try:
        # Get Api Auth Server Scopes
        api_response = api_instance.get_scopes(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling APIAuthScopesApi->get_scopes: %s\n" % e)
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
200 | [ApiResponseFor200](#get_scopes.ApiResponseFor200) | Successful response
401 | [ApiResponseFor401](#get_scopes.ApiResponseFor401) | Unauthorized

#### get_scopes.ApiResponseFor200
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
[**AuthScope**]({{complexTypePrefix}}AuthScope.md) | [**AuthScope**]({{complexTypePrefix}}AuthScope.md) | [**AuthScope**]({{complexTypePrefix}}AuthScope.md) |  | 

#### get_scopes.ApiResponseFor401
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

# **update_scope**
<a id="update_scope"></a>
> AuthId update_scope(api_auth_idscope_id)

Update Api Auth Server Scope

Update Scope

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import api_auth_scopes_api
from onelogin.model.auth_scope import AuthScope
from onelogin.model.auth_id import AuthId
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
    api_instance = api_auth_scopes_api.APIAuthScopesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'api_auth_id': "api_auth_id_example",
        'scope_id': 1,
    }
    header_params = {
    }
    try:
        # Update Api Auth Server Scope
        api_response = api_instance.update_scope(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling APIAuthScopesApi->update_scope: %s\n" % e)

    # example passing only optional values
    path_params = {
        'api_auth_id': "api_auth_id_example",
        'scope_id': 1,
    }
    header_params = {
        'Content-Type': "application/json",
    }
    body = AuthScope(
        id=323005,
        value="custom:scope",
        description="A custom scope",
    )
    try:
        # Update Api Auth Server Scope
        api_response = api_instance.update_scope(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling APIAuthScopesApi->update_scope: %s\n" % e)
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
[**AuthScope**](../../models/AuthScope.md) |  | 


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
scope_id | ScopeIdSchema | | 

# ApiAuthIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ScopeIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_scope.ApiResponseFor200) | Successful response
401 | [ApiResponseFor401](#update_scope.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#update_scope.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#update_scope.ApiResponseFor422) | Unprocessable Entity

#### update_scope.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthId**](../../models/AuthId.md) |  | 


#### update_scope.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


#### update_scope.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


#### update_scope.ApiResponseFor422
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

