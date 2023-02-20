# openapi_client.UserMappingsApi

All URIs are relative to *https://your-api-subdomain.onelogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_mapping**](UserMappingsApi.md#create_mapping) | **POST** /api/2/mappings | Create Mapping
[**delete_mapping**](UserMappingsApi.md#delete_mapping) | **DELETE** /api/2/mappings/{mapping_id} | Delete Mapping
[**get_mapping**](UserMappingsApi.md#get_mapping) | **GET** /api/2/mappings/{mapping_id} | Get Mapping
[**list_mapping_action_values**](UserMappingsApi.md#list_mapping_action_values) | **GET** /api/2/mappings/actions/{mapping_action_value}/values | List Actions Values
[**list_mapping_conditions**](UserMappingsApi.md#list_mapping_conditions) | **GET** /api/2/mappings/conditions | List Conditions
[**list_mapping_conditions_operators**](UserMappingsApi.md#list_mapping_conditions_operators) | **GET** /api/2/mappings/conditions/{mapping_condition_value}/operators | List Conditions Operators
[**list_mapping_contion_values**](UserMappingsApi.md#list_mapping_contion_values) | **GET** /api/2/mappings/conditions/{mapping_condition_value}/values | List Conditions Values
[**list_mappings**](UserMappingsApi.md#list_mappings) | **GET** /api/2/mappings | List Mappings
[**list_mappings_actions**](UserMappingsApi.md#list_mappings_actions) | **GET** /api/2/mappings/actions | List Actions
[**sort_mappings**](UserMappingsApi.md#sort_mappings) | **PUT** /api/2/mappings/sort | Bulk Sort
[**update_mapping**](UserMappingsApi.md#update_mapping) | **PUT** /api/2/mappings/{mapping_id} | Update Mapping


# **create_mapping**
> List[ListMappings200ResponseInner] create_mapping(content_type=content_type, list_mappings200_response_inner=list_mappings200_response_inner)

Create Mapping

Create User Mapping

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
    api_instance = openapi_client.UserMappingsApi(api_client)
    content_type = 'application/json' # str |  (optional) (default to 'application/json')
    list_mappings200_response_inner = openapi_client.ListMappings200ResponseInner() # ListMappings200ResponseInner |  (optional)

    try:
        # Create Mapping
        api_response = api_instance.create_mapping(content_type=content_type, list_mappings200_response_inner=list_mappings200_response_inner)
        print("The response of UserMappingsApi->create_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserMappingsApi->create_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]
 **list_mappings200_response_inner** | [**ListMappings200ResponseInner**](ListMappings200ResponseInner.md)|  | [optional] 

### Return type

[**List[ListMappings200ResponseInner]**](ListMappings200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |
**401** | Unauthorized |  -  |
**422** | Unprocessable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mapping**
> delete_mapping(mapping_id)

Delete Mapping

Delete User Mapping

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
    api_instance = openapi_client.UserMappingsApi(api_client)
    mapping_id = 56 # int | The id of the user mapping to locate.

    try:
        # Delete Mapping
        api_instance.delete_mapping(mapping_id)
    except Exception as e:
        print("Exception when calling UserMappingsApi->delete_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_id** | **int**| The id of the user mapping to locate. | 

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
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mapping**
> ListMappings200ResponseInner get_mapping(mapping_id)

Get Mapping

Get User Mapping

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
    api_instance = openapi_client.UserMappingsApi(api_client)
    mapping_id = 56 # int | The id of the user mapping to locate.

    try:
        # Get Mapping
        api_response = api_instance.get_mapping(mapping_id)
        print("The response of UserMappingsApi->get_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserMappingsApi->get_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_id** | **int**| The id of the user mapping to locate. | 

### Return type

[**ListMappings200ResponseInner**](ListMappings200ResponseInner.md)

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

# **list_mapping_action_values**
> List[ListMappingActionValues200ResponseInner] list_mapping_action_values(mapping_action_value)

List Actions Values

List User Mappings' Actions' Values

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
    api_instance = openapi_client.UserMappingsApi(api_client)
    mapping_action_value = 'mapping_action_value_example' # str | 

    try:
        # List Actions Values
        api_response = api_instance.list_mapping_action_values(mapping_action_value)
        print("The response of UserMappingsApi->list_mapping_action_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserMappingsApi->list_mapping_action_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_action_value** | **str**|  | 

### Return type

[**List[ListMappingActionValues200ResponseInner]**](ListMappingActionValues200ResponseInner.md)

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

# **list_mapping_conditions**
> ListMappingConditions200Response list_mapping_conditions()

List Conditions

List User Mappings' Conditions

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
    api_instance = openapi_client.UserMappingsApi(api_client)

    try:
        # List Conditions
        api_response = api_instance.list_mapping_conditions()
        print("The response of UserMappingsApi->list_mapping_conditions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserMappingsApi->list_mapping_conditions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListMappingConditions200Response**](ListMappingConditions200Response.md)

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

# **list_mapping_conditions_operators**
> List[ListMappingConditionsOperators200ResponseInner] list_mapping_conditions_operators(mapping_condition_value)

List Conditions Operators

List User Mappings' Conditions' Operators

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
    api_instance = openapi_client.UserMappingsApi(api_client)
    mapping_condition_value = 'mapping_condition_value_example' # str | 

    try:
        # List Conditions Operators
        api_response = api_instance.list_mapping_conditions_operators(mapping_condition_value)
        print("The response of UserMappingsApi->list_mapping_conditions_operators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserMappingsApi->list_mapping_conditions_operators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_condition_value** | **str**|  | 

### Return type

[**List[ListMappingConditionsOperators200ResponseInner]**](ListMappingConditionsOperators200ResponseInner.md)

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

# **list_mapping_contion_values**
> List[ListMappingContionValues200ResponseInner] list_mapping_contion_values(mapping_condition_value)

List Conditions Values

List User Mappings'  Conditions' Values

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
    api_instance = openapi_client.UserMappingsApi(api_client)
    mapping_condition_value = 'mapping_condition_value_example' # str | 

    try:
        # List Conditions Values
        api_response = api_instance.list_mapping_contion_values(mapping_condition_value)
        print("The response of UserMappingsApi->list_mapping_contion_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserMappingsApi->list_mapping_contion_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_condition_value** | **str**|  | 

### Return type

[**List[ListMappingContionValues200ResponseInner]**](ListMappingContionValues200ResponseInner.md)

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

# **list_mappings**
> List[ListMappings200ResponseInner] list_mappings(enabled=enabled, has_condition=has_condition, has_condition_type=has_condition_type, has_action=has_action, has_action_type=has_action_type)

List Mappings

List Mappings

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
    api_instance = openapi_client.UserMappingsApi(api_client)
    enabled = True # bool | Defaults to true. When set to `false` will return all disabled mappings. (optional) (default to True)
    has_condition = 'has_condition=has_role:123456' # str | Filters Rules based on their Conditions. Values formatted as :, where name is the Condition to look for, and value is the value to find. Multiple filters can be declared by using a comma delimited list. Wildcards are supported in both the name and value fields. For example: Single filter. has_condition=has_role:123456 Multiple filters. has_condition=has_role:123456,status:1 Wildcard for conditions. has_condition=*:123456 Wildcard for condition values. has_condition=has_role:* (optional)
    has_condition_type = 'has_condition_type_example' # str | Filters Rules based on their Conditions. Values formatted as :, where name is the Condition to look for, and value is the value to find. Multiple filters can be declared by using a comma delimited list. Wildcards are supported in both the name and value fields. For example: Single filter. has_condition=has_role:123456 Multiple filters. has_condition=has_role:123456,status:1 Wildcard for conditions. has_condition=*:123456 Wildcard for condition values. has_condition=has_role:* (optional)
    has_action = 'has_action=set_groups:123456,set_usertype:*' # str | Filters Rules based on their Actions. Values formatted as :, where name is the Action to look for, and value is the value to find. Multiple filters can be declared by using a comma delimited list. Wildcards are supported in both the name and value fields. For example: Single filter. has_action=set_licenses:123456 Multiple filters. has_action=set_groups:123456,set_usertype:* Wildcard for actions. has_action=*:123456 Wildcard for action values. has_action=set_userprincipalname:* (optional)
    has_action_type = 'has_action_type_example' # str | Filters Rules based on their action types. Allowed values are: builtin - actions that involve standard attributes custom - actions that involve custom attributes none - no actions are defined For example: Find Rules with no actions has_action_type=none (optional)

    try:
        # List Mappings
        api_response = api_instance.list_mappings(enabled=enabled, has_condition=has_condition, has_condition_type=has_condition_type, has_action=has_action, has_action_type=has_action_type)
        print("The response of UserMappingsApi->list_mappings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserMappingsApi->list_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enabled** | **bool**| Defaults to true. When set to &#x60;false&#x60; will return all disabled mappings. | [optional] [default to True]
 **has_condition** | **str**| Filters Rules based on their Conditions. Values formatted as :, where name is the Condition to look for, and value is the value to find. Multiple filters can be declared by using a comma delimited list. Wildcards are supported in both the name and value fields. For example: Single filter. has_condition&#x3D;has_role:123456 Multiple filters. has_condition&#x3D;has_role:123456,status:1 Wildcard for conditions. has_condition&#x3D;*:123456 Wildcard for condition values. has_condition&#x3D;has_role:* | [optional] 
 **has_condition_type** | **str**| Filters Rules based on their Conditions. Values formatted as :, where name is the Condition to look for, and value is the value to find. Multiple filters can be declared by using a comma delimited list. Wildcards are supported in both the name and value fields. For example: Single filter. has_condition&#x3D;has_role:123456 Multiple filters. has_condition&#x3D;has_role:123456,status:1 Wildcard for conditions. has_condition&#x3D;*:123456 Wildcard for condition values. has_condition&#x3D;has_role:* | [optional] 
 **has_action** | **str**| Filters Rules based on their Actions. Values formatted as :, where name is the Action to look for, and value is the value to find. Multiple filters can be declared by using a comma delimited list. Wildcards are supported in both the name and value fields. For example: Single filter. has_action&#x3D;set_licenses:123456 Multiple filters. has_action&#x3D;set_groups:123456,set_usertype:* Wildcard for actions. has_action&#x3D;*:123456 Wildcard for action values. has_action&#x3D;set_userprincipalname:* | [optional] 
 **has_action_type** | **str**| Filters Rules based on their action types. Allowed values are: builtin - actions that involve standard attributes custom - actions that involve custom attributes none - no actions are defined For example: Find Rules with no actions has_action_type&#x3D;none | [optional] 

### Return type

[**List[ListMappings200ResponseInner]**](ListMappings200ResponseInner.md)

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

# **list_mappings_actions**
> List[ListMappingsActions200ResponseInner] list_mappings_actions()

List Actions

List User Mappings' Actions

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
    api_instance = openapi_client.UserMappingsApi(api_client)

    try:
        # List Actions
        api_response = api_instance.list_mappings_actions()
        print("The response of UserMappingsApi->list_mappings_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserMappingsApi->list_mappings_actions: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[ListMappingsActions200ResponseInner]**](ListMappingsActions200ResponseInner.md)

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

# **sort_mappings**
> List[int] sort_mappings(content_type=content_type, request_body=request_body)

Bulk Sort

Bulk Sort User Mappings

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
    api_instance = openapi_client.UserMappingsApi(api_client)
    content_type = 'application/json' # str |  (optional) (default to 'application/json')
    request_body = [56] # List[int] |  (optional)

    try:
        # Bulk Sort
        api_response = api_instance.sort_mappings(content_type=content_type, request_body=request_body)
        print("The response of UserMappingsApi->sort_mappings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserMappingsApi->sort_mappings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]
 **request_body** | [**List[int]**](int.md)|  | [optional] 

### Return type

**List[int]**

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
**422** | Unprocessable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mapping**
> int update_mapping(mapping_id, content_type=content_type, body=body)

Update Mapping

Update User Mapping

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
    api_instance = openapi_client.UserMappingsApi(api_client)
    mapping_id = 56 # int | The id of the user mapping to locate.
    content_type = 'application/json' # str |  (optional) (default to 'application/json')
    body = None # object |  (optional)

    try:
        # Update Mapping
        api_response = api_instance.update_mapping(mapping_id, content_type=content_type, body=body)
        print("The response of UserMappingsApi->update_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserMappingsApi->update_mapping: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mapping_id** | **int**| The id of the user mapping to locate. | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]
 **body** | **object**|  | [optional] 

### Return type

**int**

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
**422** | Unprocessable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

