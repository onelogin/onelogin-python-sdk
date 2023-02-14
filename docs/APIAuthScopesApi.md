# openapi_client.APIAuthScopesApi

All URIs are relative to *https://your-api-subdomain.onelogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_scope**](APIAuthScopesApi.md#create_scope) | **POST** /api/2/api_authorizations/{api_auth_id}/scopes | Create Api Auth Server Scope
[**delete_scope**](APIAuthScopesApi.md#delete_scope) | **DELETE** /api/2/api_authorizations/{api_auth_id}/scopes/{scope_id} | Delete Api Auth Server Scope
[**get_scopes**](APIAuthScopesApi.md#get_scopes) | **GET** /api/2/api_authorizations/{api_auth_id}/scopes | Get Api Auth Server Scopes
[**update_scope**](APIAuthScopesApi.md#update_scope) | **PUT** /api/2/api_authorizations/{api_auth_id}/scopes/{scope_id} | Update Api Auth Server Scope


# **create_scope**
> CreateScope200Response create_scope(api_auth_id, content_type=content_type, create_scope_request=create_scope_request)

Create Api Auth Server Scope

Create API Auth Server Scope

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://your-api-subdomain.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://your-api-subdomain.onelogin.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.APIAuthScopesApi(api_client)
    api_auth_id = 'api_auth_id_example' # str | 
    content_type = 'application/json' # str |  (optional) (default to 'application/json')
    create_scope_request = openapi_client.CreateScopeRequest() # CreateScopeRequest |  (optional)

    try:
        # Create Api Auth Server Scope
        api_response = api_instance.create_scope(api_auth_id, content_type=content_type, create_scope_request=create_scope_request)
        print("The response of APIAuthScopesApi->create_scope:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIAuthScopesApi->create_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_auth_id** | **str**|  | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]
 **create_scope_request** | [**CreateScopeRequest**](CreateScopeRequest.md)|  | [optional] 

### Return type

[**CreateScope200Response**](CreateScope200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scope**
> delete_scope(api_auth_id, scope_id, content_type=content_type)

Delete Api Auth Server Scope

Delete Scope

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://your-api-subdomain.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://your-api-subdomain.onelogin.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.APIAuthScopesApi(api_client)
    api_auth_id = 'api_auth_id_example' # str | 
    scope_id = 56 # int | 
    content_type = 'application/json' # str |  (optional) (default to 'application/json')

    try:
        # Delete Api Auth Server Scope
        api_instance.delete_scope(api_auth_id, scope_id, content_type=content_type)
    except Exception as e:
        print("Exception when calling APIAuthScopesApi->delete_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_auth_id** | **str**|  | 
 **scope_id** | **int**|  | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. The scope is deleted. No content is returned. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_scopes**
> List[GetScopes200ResponseInner] get_scopes(api_auth_id, content_type=content_type)

Get Api Auth Server Scopes

List Authorization Scopes

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://your-api-subdomain.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://your-api-subdomain.onelogin.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.APIAuthScopesApi(api_client)
    api_auth_id = 'api_auth_id_example' # str | 
    content_type = 'application/json' # str |  (optional) (default to 'application/json')

    try:
        # Get Api Auth Server Scopes
        api_response = api_instance.get_scopes(api_auth_id, content_type=content_type)
        print("The response of APIAuthScopesApi->get_scopes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIAuthScopesApi->get_scopes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_auth_id** | **str**|  | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]

### Return type

[**List[GetScopes200ResponseInner]**](GetScopes200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_scope**
> CreateScope200Response update_scope(api_auth_id, scope_id, content_type=content_type, create_scope_request=create_scope_request)

Update Api Auth Server Scope

Update Scope

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://your-api-subdomain.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://your-api-subdomain.onelogin.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.APIAuthScopesApi(api_client)
    api_auth_id = 'api_auth_id_example' # str | 
    scope_id = 56 # int | 
    content_type = 'application/json' # str |  (optional) (default to 'application/json')
    create_scope_request = openapi_client.CreateScopeRequest() # CreateScopeRequest |  (optional)

    try:
        # Update Api Auth Server Scope
        api_response = api_instance.update_scope(api_auth_id, scope_id, content_type=content_type, create_scope_request=create_scope_request)
        print("The response of APIAuthScopesApi->update_scope:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIAuthScopesApi->update_scope: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_auth_id** | **str**|  | 
 **scope_id** | **int**|  | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]
 **create_scope_request** | [**CreateScopeRequest**](CreateScopeRequest.md)|  | [optional] 

### Return type

[**CreateScope200Response**](CreateScope200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

