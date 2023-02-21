# onelogin.APIAuthClientAppsApi

All URIs are relative to *https://your-api-subdomain.onelogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_client_app**](APIAuthClientAppsApi.md#add_client_app) | **POST** /api/2/api_authorizations/{api_auth_id}/clients | Add Client App
[**delete_client_app**](APIAuthClientAppsApi.md#delete_client_app) | **DELETE** /api/2/api_authorizations/{api_auth_id}/clients/{client_app_id} | Remove Client App
[**list_client_apps**](APIAuthClientAppsApi.md#list_client_apps) | **GET** /api/2/api_authorizations/{api_auth_id}/clients | List Clients Apps
[**update_client_app**](APIAuthClientAppsApi.md#update_client_app) | **PUT** /api/2/api_authorizations/{api_auth_id}/clients/{client_app_id} | Update Client App


# **add_client_app**
> AddClientApp201Response add_client_app(content_type, api_auth_id, add_client_app_request=add_client_app_request)

Add Client App

Add Client App

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
    api_instance = onelogin.APIAuthClientAppsApi(api_client)
    content_type = 'application/json' # str | Set to `application/json` (default to 'application/json')
    api_auth_id = 'api_auth_id_example' # str | 
    add_client_app_request = onelogin.AddClientAppRequest() # AddClientAppRequest |  (optional)

    try:
        # Add Client App
        api_response = api_instance.add_client_app(content_type, api_auth_id, add_client_app_request=add_client_app_request)
        print("The response of APIAuthClientAppsApi->add_client_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIAuthClientAppsApi->add_client_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Set to &#x60;application/json&#x60; | [default to &#39;application/json&#39;]
 **api_auth_id** | **str**|  | 
 **add_client_app_request** | [**AddClientAppRequest**](AddClientAppRequest.md)|  | [optional] 

### Return type

[**AddClientApp201Response**](AddClientApp201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client_app**
> AddClientApp201Response delete_client_app(api_auth_id, client_app_id, content_type=content_type)

Remove Client App

Delete Client App

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
    api_instance = onelogin.APIAuthClientAppsApi(api_client)
    api_auth_id = 'api_auth_id_example' # str | 
    client_app_id = 56 # int | 
    content_type = 'application/json' # str |  (optional) (default to 'application/json')

    try:
        # Remove Client App
        api_response = api_instance.delete_client_app(api_auth_id, client_app_id, content_type=content_type)
        print("The response of APIAuthClientAppsApi->delete_client_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIAuthClientAppsApi->delete_client_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_auth_id** | **str**|  | 
 **client_app_id** | **int**|  | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]

### Return type

[**AddClientApp201Response**](AddClientApp201Response.md)

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_client_apps**
> ListClientApps200Response list_client_apps(api_auth_id, content_type=content_type)

List Clients Apps

List Client Apps

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
    api_instance = onelogin.APIAuthClientAppsApi(api_client)
    api_auth_id = 'api_auth_id_example' # str | 
    content_type = 'application/json' # str |  (optional) (default to 'application/json')

    try:
        # List Clients Apps
        api_response = api_instance.list_client_apps(api_auth_id, content_type=content_type)
        print("The response of APIAuthClientAppsApi->list_client_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIAuthClientAppsApi->list_client_apps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_auth_id** | **str**|  | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]

### Return type

[**ListClientApps200Response**](ListClientApps200Response.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_app**
> AddClientApp201Response update_client_app(content_type, api_auth_id, client_app_id, update_client_app_request=update_client_app_request)

Update Client App

Update Client App

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
    api_instance = onelogin.APIAuthClientAppsApi(api_client)
    content_type = 'application/json' # str | Set to `application/json` (default to 'application/json')
    api_auth_id = 'api_auth_id_example' # str | 
    client_app_id = 56 # int | 
    update_client_app_request = onelogin.UpdateClientAppRequest() # UpdateClientAppRequest |  (optional)

    try:
        # Update Client App
        api_response = api_instance.update_client_app(content_type, api_auth_id, client_app_id, update_client_app_request=update_client_app_request)
        print("The response of APIAuthClientAppsApi->update_client_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIAuthClientAppsApi->update_client_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Set to &#x60;application/json&#x60; | [default to &#39;application/json&#39;]
 **api_auth_id** | **str**|  | 
 **client_app_id** | **int**|  | 
 **update_client_app_request** | [**UpdateClientAppRequest**](UpdateClientAppRequest.md)|  | [optional] 

### Return type

[**AddClientApp201Response**](AddClientApp201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

