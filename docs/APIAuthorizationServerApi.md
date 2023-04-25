# onelogin.APIAuthorizationServerApi

All URIs are relative to *https://your-api-subdomain.onelogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_auth_server**](APIAuthorizationServerApi.md#create_auth_server) | **POST** /api/2/api_authorizations | Create Api Auth Server
[**delete_auth_server**](APIAuthorizationServerApi.md#delete_auth_server) | **DELETE** /api/2/api_authorizations/{api_auth_id} | Delete Api Auth Server
[**get_auth_server**](APIAuthorizationServerApi.md#get_auth_server) | **GET** /api/2/api_authorizations/{api_auth_id} | Get Api Auth Server
[**list_auth_servers**](APIAuthorizationServerApi.md#list_auth_servers) | **GET** /api/2/api_authorizations | List Api Auth Servers
[**update_auth_server**](APIAuthorizationServerApi.md#update_auth_server) | **PUT** /api/2/api_authorizations/{api_auth_id} | Update Api Auth Server


# **create_auth_server**
> AuthServer create_auth_server(content_type=content_type, auth_server=auth_server)

Create Api Auth Server

Create Auth Server

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import os
import onelogin
from onelogin.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with onelogin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onelogin.APIAuthorizationServerApi(api_client)
    content_type = 'application/json' # str |  (optional) (default to 'application/json')
    auth_server = onelogin.AuthServer() # AuthServer |  (optional)

    try:
        # Create Api Auth Server
        api_response = api_instance.create_auth_server(content_type=content_type, auth_server=auth_server)
        print("The response of APIAuthorizationServerApi->create_auth_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIAuthorizationServerApi->create_auth_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]
 **auth_server** | [**AuthServer**](AuthServer.md)|  | [optional] 

### Return type

[**AuthServer**](AuthServer.md)

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
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_auth_server**
> delete_auth_server(api_auth_id, content_type=content_type)

Delete Api Auth Server

Delete Authentication Server

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import os
import onelogin
from onelogin.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with onelogin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onelogin.APIAuthorizationServerApi(api_client)
    api_auth_id = 'api_auth_id_example' # str | 
    content_type = 'application/json' # str |  (optional) (default to 'application/json')

    try:
        # Delete Api Auth Server
        api_instance.delete_auth_server(api_auth_id, content_type=content_type)
    except Exception as e:
        print("Exception when calling APIAuthorizationServerApi->delete_auth_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_auth_id** | **str**|  | 
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
**204** | Success. The auth server is deleted. No content is returned. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_server**
> AuthServer get_auth_server(api_auth_id, content_type=content_type)

Get Api Auth Server

Get Authorization Server

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import os
import onelogin
from onelogin.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with onelogin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onelogin.APIAuthorizationServerApi(api_client)
    api_auth_id = 'api_auth_id_example' # str | 
    content_type = 'application/json' # str |  (optional) (default to 'application/json')

    try:
        # Get Api Auth Server
        api_response = api_instance.get_auth_server(api_auth_id, content_type=content_type)
        print("The response of APIAuthorizationServerApi->get_auth_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIAuthorizationServerApi->get_auth_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_auth_id** | **str**|  | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]

### Return type

[**AuthServer**](AuthServer.md)

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

# **list_auth_servers**
> List[AuthServer] list_auth_servers()

List Api Auth Servers

List Authorization Servers

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import os
import onelogin
from onelogin.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with onelogin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onelogin.APIAuthorizationServerApi(api_client)

    try:
        # List Api Auth Servers
        api_response = api_instance.list_auth_servers()
        print("The response of APIAuthorizationServerApi->list_auth_servers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIAuthorizationServerApi->list_auth_servers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[AuthServer]**](AuthServer.md)

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

# **update_auth_server**
> AuthServer update_auth_server(api_auth_id, content_type=content_type, auth_server=auth_server)

Update Api Auth Server

Update Authorization Server

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import os
import onelogin
from onelogin.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with onelogin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onelogin.APIAuthorizationServerApi(api_client)
    api_auth_id = 'api_auth_id_example' # str | 
    content_type = 'application/json' # str |  (optional) (default to 'application/json')
    auth_server = onelogin.AuthServer() # AuthServer |  (optional)

    try:
        # Update Api Auth Server
        api_response = api_instance.update_auth_server(api_auth_id, content_type=content_type, auth_server=auth_server)
        print("The response of APIAuthorizationServerApi->update_auth_server:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIAuthorizationServerApi->update_auth_server: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_auth_id** | **str**|  | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]
 **auth_server** | [**AuthServer**](AuthServer.md)|  | [optional] 

### Return type

[**AuthServer**](AuthServer.md)

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

