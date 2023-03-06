# onelogin.EventsApi

All URIs are relative to *https://your-api-subdomain.onelogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event_by_id**](EventsApi.md#get_event_by_id) | **GET** /api/1/events/{event_id} | Get Event by ID
[**get_event_types**](EventsApi.md#get_event_types) | **GET** /api/1/events/types | Get Event Types
[**get_events**](EventsApi.md#get_events) | **GET** /api/1/events | Get Events


# **get_event_by_id**
> GetEventById200Response get_event_by_id(event_id)

Get Event by ID

Get Event By ID

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
    api_instance = onelogin.EventsApi(api_client)
    event_id = 56 # int | 

    try:
        # Get Event by ID
        api_response = api_instance.get_event_by_id(event_id)
        print("The response of EventsApi->get_event_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_event_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **int**|  | 

### Return type

[**GetEventById200Response**](GetEventById200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_types**
> GetEventTypes200Response get_event_types(content_type=content_type)

Get Event Types

Get Event types

### Example

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


# Enter a context with an instance of the API client
with onelogin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onelogin.EventsApi(api_client)
    content_type = 'application/json' # str |  (optional) (default to 'application/json')

    try:
        # Get Event Types
        api_response = api_instance.get_event_types(content_type=content_type)
        print("The response of EventsApi->get_event_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_event_types: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]

### Return type

[**GetEventTypes200Response**](GetEventTypes200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events**
> GetEvents200Response get_events(event_type_id=event_type_id, client_id=client_id, directory_id=directory_id, id=id, created_at=created_at, resolution=resolution, since=since, until=until, user_id=user_id)

Get Events

Get Events

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
    api_instance = onelogin.EventsApi(api_client)
    event_type_id = [56] # List[int] |  (optional)
    client_id = 56 # int |  (optional)
    directory_id = 56 # int |  (optional)
    id = 56 # int |  (optional)
    created_at = 'created_at_example' # str |  (optional)
    resolution = 'resolution_example' # str |  (optional)
    since = 'since_example' # str |  (optional)
    until = 'until_example' # str |  (optional)
    user_id = 56 # int | Set to the id of the user that you want to return. (optional)

    try:
        # Get Events
        api_response = api_instance.get_events(event_type_id=event_type_id, client_id=client_id, directory_id=directory_id, id=id, created_at=created_at, resolution=resolution, since=since, until=until, user_id=user_id)
        print("The response of EventsApi->get_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_type_id** | [**List[int]**](int.md)|  | [optional] 
 **client_id** | **int**|  | [optional] 
 **directory_id** | **int**|  | [optional] 
 **id** | **int**|  | [optional] 
 **created_at** | **str**|  | [optional] 
 **resolution** | **str**|  | [optional] 
 **since** | **str**|  | [optional] 
 **until** | **str**|  | [optional] 
 **user_id** | **int**| Set to the id of the user that you want to return. | [optional] 

### Return type

[**GetEvents200Response**](GetEvents200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

