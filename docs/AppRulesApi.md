# onelogin.AppRulesApi

All URIs are relative to *https://your-api-subdomain.onelogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app_rule**](AppRulesApi.md#create_app_rule) | **POST** /api/2/apps/{app_id}/rules | 
[**delete_rule**](AppRulesApi.md#delete_rule) | **DELETE** /api/2/apps/{app_id}/rules/{rule_id} | Delete Rule
[**get_app_rule**](AppRulesApi.md#get_app_rule) | **GET** /api/2/apps/{app_id}/rules/{rule_id} | Get Rule
[**list_action_valies**](AppRulesApi.md#list_action_valies) | **GET** /api/2/apps/{app_id}/rules/actions/{rule_action_value}/values | List Actions Values
[**list_actions**](AppRulesApi.md#list_actions) | **GET** /api/2/apps/{app_id}/rules/actions | List Actions
[**list_app_rules**](AppRulesApi.md#list_app_rules) | **GET** /api/2/apps/{app_id}/rules | List Rules
[**list_condition_operators**](AppRulesApi.md#list_condition_operators) | **GET** /api/2/apps/{app_id}/rules/conditions/{rule_condition_value}/operators | List Conditions Operators
[**list_condition_values**](AppRulesApi.md#list_condition_values) | **GET** /api/2/apps/{app_id}/rules/conditions/{rule_condition_value}/values | List Conditions Values
[**list_conditions**](AppRulesApi.md#list_conditions) | **GET** /api/2/apps/{app_id}/rules/conditions | List Conditions
[**sort_app_rules**](AppRulesApi.md#sort_app_rules) | **PUT** /api/2/apps/{app_id}/rules/sort | Bulk Sort
[**update_app_rule**](AppRulesApi.md#update_app_rule) | **PUT** /api/2/apps/{app_id}/rules/{rule_id} | Update Rule


# **create_app_rule**
> AppRule create_app_rule(app_id, app_rule=app_rule)



Create App Rule

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
    api_instance = onelogin.AppRulesApi(api_client)
    app_id = 56 # int | 
    app_rule = onelogin.AppRule() # AppRule |  (optional)

    try:
        api_response = api_instance.create_app_rule(app_id, app_rule=app_rule)
        print("The response of AppRulesApi->create_app_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRulesApi->create_app_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**|  | 
 **app_rule** | [**AppRule**](AppRule.md)|  | [optional] 

### Return type

[**AppRule**](AppRule.md)

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

# **delete_rule**
> delete_rule(app_id, rule_id)

Delete Rule

Delete App Rule

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
    api_instance = onelogin.AppRulesApi(api_client)
    app_id = 56 # int | 
    rule_id = 'rule_id_example' # str | 

    try:
        # Delete Rule
        api_instance.delete_rule(app_id, rule_id)
    except Exception as e:
        print("Exception when calling AppRulesApi->delete_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**|  | 
 **rule_id** | **str**|  | 

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
**204** | Success. The rule is deleted. No content is returned. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_rule**
> AppRule get_app_rule(app_id, rule_id)

Get Rule

Get App Rule

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
    api_instance = onelogin.AppRulesApi(api_client)
    app_id = 56 # int | 
    rule_id = 'rule_id_example' # str | 

    try:
        # Get Rule
        api_response = api_instance.get_app_rule(app_id, rule_id)
        print("The response of AppRulesApi->get_app_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRulesApi->get_app_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**|  | 
 **rule_id** | **str**|  | 

### Return type

[**AppRule**](AppRule.md)

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

# **list_action_valies**
> List[RuleAction] list_action_valies(app_id, rule_action_value)

List Actions Values

Sort App rules

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
    api_instance = onelogin.AppRulesApi(api_client)
    app_id = 56 # int | 
    rule_action_value = 'rule_action_value_example' # str | 

    try:
        # List Actions Values
        api_response = api_instance.list_action_valies(app_id, rule_action_value)
        print("The response of AppRulesApi->list_action_valies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRulesApi->list_action_valies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**|  | 
 **rule_action_value** | **str**|  | 

### Return type

[**List[RuleAction]**](RuleAction.md)

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

# **list_actions**
> List[RuleAction] list_actions(app_id)

List Actions

List Actions

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
    api_instance = onelogin.AppRulesApi(api_client)
    app_id = 56 # int | 

    try:
        # List Actions
        api_response = api_instance.list_actions(app_id)
        print("The response of AppRulesApi->list_actions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRulesApi->list_actions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**|  | 

### Return type

[**List[RuleAction]**](RuleAction.md)

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

# **list_app_rules**
> List[AppRule] list_app_rules(app_id, has_condition=has_condition, has_condition_type=has_condition_type, has_action=has_action, has_action_type=has_action_type, enabled=enabled)

List Rules

List App Rules

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
    api_instance = onelogin.AppRulesApi(api_client)
    app_id = 56 # int | 
    has_condition = 'has_condition=has_role:123456' # str | Filters Rules based on their Conditions. Values formatted as :, where name is the Condition to look for, and value is the value to find. Multiple filters can be declared by using a comma delimited list. Wildcards are supported in both the name and value fields. For example: Single filter. has_condition=has_role:123456 Multiple filters. has_condition=has_role:123456,status:1 Wildcard for conditions. has_condition=*:123456 Wildcard for condition values. has_condition=has_role:* (optional)
    has_condition_type = 'has_condition_type_example' # str | Filters Rules based on their Conditions. Values formatted as :, where name is the Condition to look for, and value is the value to find. Multiple filters can be declared by using a comma delimited list. Wildcards are supported in both the name and value fields. For example: Single filter. has_condition=has_role:123456 Multiple filters. has_condition=has_role:123456,status:1 Wildcard for conditions. has_condition=*:123456 Wildcard for condition values. has_condition=has_role:* (optional)
    has_action = 'has_action=set_groups:123456,set_usertype:*' # str | Filters Rules based on their Actions. Values formatted as :, where name is the Action to look for, and value is the value to find. Multiple filters can be declared by using a comma delimited list. Wildcards are supported in both the name and value fields. For example: Single filter. has_action=set_licenses:123456 Multiple filters. has_action=set_groups:123456,set_usertype:* Wildcard for actions. has_action=*:123456 Wildcard for action values. has_action=set_userprincipalname:* (optional)
    has_action_type = 'has_action_type_example' # str | Filters Rules based on their action types. Allowed values are: builtin - actions that involve standard attributes custom - actions that involve custom attributes none - no actions are defined For example: Find Rules with no actions has_action_type=none (optional)
    enabled = True # bool | Defaults to true. When set to `false` will return all disabled mappings. (optional) (default to True)

    try:
        # List Rules
        api_response = api_instance.list_app_rules(app_id, has_condition=has_condition, has_condition_type=has_condition_type, has_action=has_action, has_action_type=has_action_type, enabled=enabled)
        print("The response of AppRulesApi->list_app_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRulesApi->list_app_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**|  | 
 **has_condition** | **str**| Filters Rules based on their Conditions. Values formatted as :, where name is the Condition to look for, and value is the value to find. Multiple filters can be declared by using a comma delimited list. Wildcards are supported in both the name and value fields. For example: Single filter. has_condition&#x3D;has_role:123456 Multiple filters. has_condition&#x3D;has_role:123456,status:1 Wildcard for conditions. has_condition&#x3D;*:123456 Wildcard for condition values. has_condition&#x3D;has_role:* | [optional] 
 **has_condition_type** | **str**| Filters Rules based on their Conditions. Values formatted as :, where name is the Condition to look for, and value is the value to find. Multiple filters can be declared by using a comma delimited list. Wildcards are supported in both the name and value fields. For example: Single filter. has_condition&#x3D;has_role:123456 Multiple filters. has_condition&#x3D;has_role:123456,status:1 Wildcard for conditions. has_condition&#x3D;*:123456 Wildcard for condition values. has_condition&#x3D;has_role:* | [optional] 
 **has_action** | **str**| Filters Rules based on their Actions. Values formatted as :, where name is the Action to look for, and value is the value to find. Multiple filters can be declared by using a comma delimited list. Wildcards are supported in both the name and value fields. For example: Single filter. has_action&#x3D;set_licenses:123456 Multiple filters. has_action&#x3D;set_groups:123456,set_usertype:* Wildcard for actions. has_action&#x3D;*:123456 Wildcard for action values. has_action&#x3D;set_userprincipalname:* | [optional] 
 **has_action_type** | **str**| Filters Rules based on their action types. Allowed values are: builtin - actions that involve standard attributes custom - actions that involve custom attributes none - no actions are defined For example: Find Rules with no actions has_action_type&#x3D;none | [optional] 
 **enabled** | **bool**| Defaults to true. When set to &#x60;false&#x60; will return all disabled mappings. | [optional] [default to True]

### Return type

[**List[AppRule]**](AppRule.md)

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

# **list_condition_operators**
> List[RuleCondition] list_condition_operators(app_id, rule_condition_value)

List Conditions Operators

List Condition Operators

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
    api_instance = onelogin.AppRulesApi(api_client)
    app_id = 56 # int | 
    rule_condition_value = 'rule_condition_value_example' # str | 

    try:
        # List Conditions Operators
        api_response = api_instance.list_condition_operators(app_id, rule_condition_value)
        print("The response of AppRulesApi->list_condition_operators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRulesApi->list_condition_operators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**|  | 
 **rule_condition_value** | **str**|  | 

### Return type

[**List[RuleCondition]**](RuleCondition.md)

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

# **list_condition_values**
> RuleCondition list_condition_values(app_id, rule_condition_value)

List Conditions Values

List Condition Values

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
    api_instance = onelogin.AppRulesApi(api_client)
    app_id = 56 # int | 
    rule_condition_value = 'rule_condition_value_example' # str | 

    try:
        # List Conditions Values
        api_response = api_instance.list_condition_values(app_id, rule_condition_value)
        print("The response of AppRulesApi->list_condition_values:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRulesApi->list_condition_values: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**|  | 
 **rule_condition_value** | **str**|  | 

### Return type

[**RuleCondition**](RuleCondition.md)

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

# **list_conditions**
> List[ListConditions200ResponseInner] list_conditions(app_id)

List Conditions

List App Conditions

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
    api_instance = onelogin.AppRulesApi(api_client)
    app_id = 56 # int | 

    try:
        # List Conditions
        api_response = api_instance.list_conditions(app_id)
        print("The response of AppRulesApi->list_conditions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRulesApi->list_conditions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**|  | 

### Return type

[**List[ListConditions200ResponseInner]**](ListConditions200ResponseInner.md)

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

# **sort_app_rules**
> List[int] sort_app_rules(app_id, request_body=request_body)

Bulk Sort

Sort App rules

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
    api_instance = onelogin.AppRulesApi(api_client)
    app_id = 56 # int | 
    request_body = [56] # List[int] |  (optional)

    try:
        # Bulk Sort
        api_response = api_instance.sort_app_rules(app_id, request_body=request_body)
        print("The response of AppRulesApi->sort_app_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRulesApi->sort_app_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**|  | 
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
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app_rule**
> AppRule update_app_rule(app_id, rule_id, app_rule=app_rule)

Update Rule

Update App Rule.

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
    api_instance = onelogin.AppRulesApi(api_client)
    app_id = 56 # int | 
    rule_id = 'rule_id_example' # str | 
    app_rule = onelogin.AppRule() # AppRule |  (optional)

    try:
        # Update Rule
        api_response = api_instance.update_app_rule(app_id, rule_id, app_rule=app_rule)
        print("The response of AppRulesApi->update_app_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AppRulesApi->update_app_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**|  | 
 **rule_id** | **str**|  | 
 **app_rule** | [**AppRule**](AppRule.md)|  | [optional] 

### Return type

[**AppRule**](AppRule.md)

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

