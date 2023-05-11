# onelogin.SmartHooksApi

All URIs are relative to *https://your-api-subdomain.onelogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_environment_variable**](SmartHooksApi.md#create_environment_variable) | **POST** /api/2/hooks/envs | Create Environment Variable
[**create_hook**](SmartHooksApi.md#create_hook) | **POST** /api/2/hooks | Create Smart Hook
[**delete_environment_variable**](SmartHooksApi.md#delete_environment_variable) | **DELETE** /api/2/hooks/envs/{envvar_id} | Delete Environment Variable
[**delete_hook**](SmartHooksApi.md#delete_hook) | **DELETE** /api/2/hooks/{hook_id} | Delete Smart Hook by ID
[**get_environment_variable**](SmartHooksApi.md#get_environment_variable) | **GET** /api/2/hooks/envs/{envvar_id} | Get Environment Variable
[**get_hook**](SmartHooksApi.md#get_hook) | **GET** /api/2/hooks/{hook_id} | Get Smart Hook by ID
[**get_logs**](SmartHooksApi.md#get_logs) | **GET** /api/2/hooks/{hook_id}/logs | Get Smart Hook Logs
[**list_environment_variables**](SmartHooksApi.md#list_environment_variables) | **GET** /api/2/hooks/envs | List Environment Variables
[**list_hooks**](SmartHooksApi.md#list_hooks) | **GET** /api/2/hooks | List all Smart Hooks
[**update_environment_variable**](SmartHooksApi.md#update_environment_variable) | **PUT** /api/2/hooks/envs/{envvar_id} | Update Environment Variable
[**update_hook**](SmartHooksApi.md#update_hook) | **PUT** /api/2/hooks/{hook_id} | Update Smart Hook by ID


# **create_environment_variable**
> HookEnvvar create_environment_variable(hook_envvar)

Create Environment Variable

Create Environment Variable

### Example

* OAuth Authentication (OAuth2):
```python
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
    api_instance = onelogin.SmartHooksApi(api_client)
    hook_envvar = onelogin.HookEnvvar() # HookEnvvar | 

    try:
        # Create Environment Variable
        api_response = api_instance.create_environment_variable(hook_envvar)
        print("The response of SmartHooksApi->create_environment_variable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartHooksApi->create_environment_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hook_envvar** | [**HookEnvvar**](HookEnvvar.md)|  | 

### Return type

[**HookEnvvar**](HookEnvvar.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CREATED |  -  |
**401** | Unauthorized |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_hook**
> Hook create_hook(hook)

Create Smart Hook

Create Smart Hook

### Example

* OAuth Authentication (OAuth2):
```python
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
    api_instance = onelogin.SmartHooksApi(api_client)
    hook = onelogin.Hook() # Hook | 

    try:
        # Create Smart Hook
        api_response = api_instance.create_hook(hook)
        print("The response of SmartHooksApi->create_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartHooksApi->create_hook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hook** | [**Hook**](Hook.md)|  | 

### Return type

[**Hook**](Hook.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CREATED |  -  |
**401** | Unauthorized |  -  |
**409** | Conflict |  -  |
**422** | You function is not base64 encoded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_environment_variable**
> delete_environment_variable(envvar_id)

Delete Environment Variable

Delete Environment Variable

### Example

* OAuth Authentication (OAuth2):
```python
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
    api_instance = onelogin.SmartHooksApi(api_client)
    envvar_id = 'envvar_id_example' # str | Set to the id of the Hook Environment Variable that you want to fetch.

    try:
        # Delete Environment Variable
        api_instance.delete_environment_variable(envvar_id)
    except Exception as e:
        print("Exception when calling SmartHooksApi->delete_environment_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **envvar_id** | **str**| Set to the id of the Hook Environment Variable that you want to fetch. | 

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
**204** | Success. The environment variable has been deleted. No content is returned. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_hook**
> delete_hook(hook_id)

Delete Smart Hook by ID

Delete Smart Hook

### Example

* OAuth Authentication (OAuth2):
```python
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
    api_instance = onelogin.SmartHooksApi(api_client)
    hook_id = 'hook_id_example' # str | Set to the id of the Hook that you want to return.

    try:
        # Delete Smart Hook by ID
        api_instance.delete_hook(hook_id)
    except Exception as e:
        print("Exception when calling SmartHooksApi->delete_hook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hook_id** | **str**| Set to the id of the Hook that you want to return. | 

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
**202** | Success. The hook function has been queued for deletion. This typically happens within seconds of making the request. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_variable**
> HookEnvvar get_environment_variable(envvar_id)

Get Environment Variable

Get Environment Variable

### Example

* OAuth Authentication (OAuth2):
```python
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
    api_instance = onelogin.SmartHooksApi(api_client)
    envvar_id = 'envvar_id_example' # str | Set to the id of the Hook Environment Variable that you want to fetch.

    try:
        # Get Environment Variable
        api_response = api_instance.get_environment_variable(envvar_id)
        print("The response of SmartHooksApi->get_environment_variable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartHooksApi->get_environment_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **envvar_id** | **str**| Set to the id of the Hook Environment Variable that you want to fetch. | 

### Return type

[**HookEnvvar**](HookEnvvar.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hook**
> Hook get_hook(hook_id)

Get Smart Hook by ID

Get Smart Hook

### Example

* OAuth Authentication (OAuth2):
```python
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
    api_instance = onelogin.SmartHooksApi(api_client)
    hook_id = 'hook_id_example' # str | Set to the id of the Hook that you want to return.

    try:
        # Get Smart Hook by ID
        api_response = api_instance.get_hook(hook_id)
        print("The response of SmartHooksApi->get_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartHooksApi->get_hook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hook_id** | **str**| Set to the id of the Hook that you want to return. | 

### Return type

[**Hook**](Hook.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logs**
> List[HookLog] get_logs(hook_id, limit=limit, page=page, cursor=cursor, request_id=request_id, correlation_id=correlation_id)

Get Smart Hook Logs

Get Smart Hook Logs

### Example

* OAuth Authentication (OAuth2):
```python
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
    api_instance = onelogin.SmartHooksApi(api_client)
    hook_id = 'hook_id_example' # str | Set to the id of the Hook that you want to return.
    limit = 56 # int | How many items to return at one time (max 100) (optional)
    page = 56 # int | The page number of results to return. (optional)
    cursor = 'cursor_example' # str | Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. (optional)
    request_id = 'request_id_example' # str | Returns logs that contain this request_id. (optional)
    correlation_id = 'correlation_id_example' # str | Returns logs that contain this correlation_id. (optional)

    try:
        # Get Smart Hook Logs
        api_response = api_instance.get_logs(hook_id, limit=limit, page=page, cursor=cursor, request_id=request_id, correlation_id=correlation_id)
        print("The response of SmartHooksApi->get_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartHooksApi->get_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hook_id** | **str**| Set to the id of the Hook that you want to return. | 
 **limit** | **int**| How many items to return at one time (max 100) | [optional] 
 **page** | **int**| The page number of results to return. | [optional] 
 **cursor** | **str**| Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. | [optional] 
 **request_id** | **str**| Returns logs that contain this request_id. | [optional] 
 **correlation_id** | **str**| Returns logs that contain this correlation_id. | [optional] 

### Return type

[**List[HookLog]**](HookLog.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Current-Page -  <br>  * Page-Items -  <br>  * Total-Count -  <br>  * Total-Pages -  <br>  * Link -  <br>  * Before-Cursor -  <br>  * After-Cursor -  <br>  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_environment_variables**
> List[HookEnvvar] list_environment_variables(limit=limit, page=page, cursor=cursor)

List Environment Variables

List Environment Variables

### Example

* OAuth Authentication (OAuth2):
```python
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
    api_instance = onelogin.SmartHooksApi(api_client)
    limit = 56 # int | How many items to return at one time (max 100) (optional)
    page = 56 # int | The page number of results to return. (optional)
    cursor = 'cursor_example' # str | Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. (optional)

    try:
        # List Environment Variables
        api_response = api_instance.list_environment_variables(limit=limit, page=page, cursor=cursor)
        print("The response of SmartHooksApi->list_environment_variables:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartHooksApi->list_environment_variables: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many items to return at one time (max 100) | [optional] 
 **page** | **int**| The page number of results to return. | [optional] 
 **cursor** | **str**| Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. | [optional] 

### Return type

[**List[HookEnvvar]**](HookEnvvar.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Current-Page -  <br>  * Page-Items -  <br>  * Total-Count -  <br>  * Total-Pages -  <br>  * Link -  <br>  * Before-Cursor -  <br>  * After-Cursor -  <br>  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_hooks**
> List[Hook] list_hooks(limit=limit, page=page, cursor=cursor)

List all Smart Hooks

List Smart Hooks

### Example

* OAuth Authentication (OAuth2):
```python
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
    api_instance = onelogin.SmartHooksApi(api_client)
    limit = 56 # int | How many items to return at one time (max 100) (optional)
    page = 56 # int | The page number of results to return. (optional)
    cursor = 'cursor_example' # str | Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. (optional)

    try:
        # List all Smart Hooks
        api_response = api_instance.list_hooks(limit=limit, page=page, cursor=cursor)
        print("The response of SmartHooksApi->list_hooks:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartHooksApi->list_hooks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many items to return at one time (max 100) | [optional] 
 **page** | **int**| The page number of results to return. | [optional] 
 **cursor** | **str**| Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. | [optional] 

### Return type

[**List[Hook]**](Hook.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Current-Page -  <br>  * Page-Items -  <br>  * Total-Count -  <br>  * Total-Pages -  <br>  * Link -  <br>  * Before-Cursor -  <br>  * After-Cursor -  <br>  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_environment_variable**
> HookEnvvar update_environment_variable(envvar_id, update_environment_variable_request)

Update Environment Variable

Update Environment Variable

### Example

* OAuth Authentication (OAuth2):
```python
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
    api_instance = onelogin.SmartHooksApi(api_client)
    envvar_id = 'envvar_id_example' # str | Set to the id of the Hook Environment Variable that you want to fetch.
    update_environment_variable_request = onelogin.UpdateEnvironmentVariableRequest() # UpdateEnvironmentVariableRequest | 

    try:
        # Update Environment Variable
        api_response = api_instance.update_environment_variable(envvar_id, update_environment_variable_request)
        print("The response of SmartHooksApi->update_environment_variable:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartHooksApi->update_environment_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **envvar_id** | **str**| Set to the id of the Hook Environment Variable that you want to fetch. | 
 **update_environment_variable_request** | [**UpdateEnvironmentVariableRequest**](UpdateEnvironmentVariableRequest.md)|  | 

### Return type

[**HookEnvvar**](HookEnvvar.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_hook**
> Hook update_hook(hook_id, hook)

Update Smart Hook by ID

Update Smart Hook

### Example

* OAuth Authentication (OAuth2):
```python
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
    api_instance = onelogin.SmartHooksApi(api_client)
    hook_id = 'hook_id_example' # str | Set to the id of the Hook that you want to return.
    hook = onelogin.Hook() # Hook | 

    try:
        # Update Smart Hook by ID
        api_response = api_instance.update_hook(hook_id, hook)
        print("The response of SmartHooksApi->update_hook:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SmartHooksApi->update_hook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hook_id** | **str**| Set to the id of the Hook that you want to return. | 
 **hook** | [**Hook**](Hook.md)|  | 

### Return type

[**Hook**](Hook.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**422** | You function is not base64 encoded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

