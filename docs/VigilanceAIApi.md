# onelogin.VigilanceAIApi

All URIs are relative to *https://your-api-subdomain.onelogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_risk_rule**](VigilanceAIApi.md#create_risk_rule) | **POST** /api/2/risk/rules | Create Rule
[**delete_risk_rule**](VigilanceAIApi.md#delete_risk_rule) | **DELETE** /api/2/risk/rules/{rule_id} | Delete Rule
[**get_risk_rule**](VigilanceAIApi.md#get_risk_rule) | **GET** /api/2/risk/rules/{rule_id} | get Risk Rule
[**get_risk_score**](VigilanceAIApi.md#get_risk_score) | **POST** /api/2/risk/verify | Get a Risk Score
[**get_risk_scores**](VigilanceAIApi.md#get_risk_scores) | **GET** /api/2/risk/scores | Get Score Summary
[**list_risk_rules**](VigilanceAIApi.md#list_risk_rules) | **GET** /api/2/risk/rules | List Rules
[**track_risk_event**](VigilanceAIApi.md#track_risk_event) | **POST** /api/2/risk/events | Track an Event
[**update_risk_rule**](VigilanceAIApi.md#update_risk_rule) | **PUT** /api/2/risk/rules/{rule_id} | Update Rule


# **create_risk_rule**
> ListRiskRules200ResponseInner create_risk_rule(list_risk_rules200_response_inner, content_type=content_type)

Create Rule

Create Vigilance AI (Risk Service) Rule

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
    api_instance = onelogin.VigilanceAIApi(api_client)
    list_risk_rules200_response_inner = onelogin.ListRiskRules200ResponseInner() # ListRiskRules200ResponseInner | 
    content_type = 'application/json' # str |  (optional) (default to 'application/json')

    try:
        # Create Rule
        api_response = api_instance.create_risk_rule(list_risk_rules200_response_inner, content_type=content_type)
        print("The response of VigilanceAIApi->create_risk_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VigilanceAIApi->create_risk_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_risk_rules200_response_inner** | [**ListRiskRules200ResponseInner**](ListRiskRules200ResponseInner.md)|  | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]

### Return type

[**ListRiskRules200ResponseInner**](ListRiskRules200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CREATED |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_risk_rule**
> delete_risk_rule(rule_id)

Delete Rule

Delete Vigilance AI (Risk Service)

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
    api_instance = onelogin.VigilanceAIApi(api_client)
    rule_id = 'rule_id_example' # str | 

    try:
        # Delete Rule
        api_instance.delete_risk_rule(rule_id)
    except Exception as e:
        print("Exception when calling VigilanceAIApi->delete_risk_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**200** | Successful response |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_risk_rule**
> ListRiskRules200ResponseInner get_risk_rule(rule_id)

get Risk Rule

Use this API to return a single rule that has been created in the Risk Sevice.

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
    api_instance = onelogin.VigilanceAIApi(api_client)
    rule_id = 'rule_id_example' # str | 

    try:
        # get Risk Rule
        api_response = api_instance.get_risk_rule(rule_id)
        print("The response of VigilanceAIApi->get_risk_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VigilanceAIApi->get_risk_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 

### Return type

[**ListRiskRules200ResponseInner**](ListRiskRules200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_risk_score**
> GetRiskScore200Response get_risk_score(get_risk_score_request, content_type=content_type, before=before, after=after)

Get a Risk Score

Get Vigilance AI (Risk Service) Score

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
    api_instance = onelogin.VigilanceAIApi(api_client)
    get_risk_score_request = onelogin.GetRiskScoreRequest() # GetRiskScoreRequest | 
    content_type = 'application/json' # str |  (optional) (default to 'application/json')
    before = 'before_example' # str | Optional ISO8601 formatted date string. Defaults to current date. Maximum date is 90 days ago. (optional)
    after = 'after_example' # str | Optional ISO8601 formatted date string. Defaults to 30 days ago. Maximum date is 90 days ago. (optional)

    try:
        # Get a Risk Score
        api_response = api_instance.get_risk_score(get_risk_score_request, content_type=content_type, before=before, after=after)
        print("The response of VigilanceAIApi->get_risk_score:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VigilanceAIApi->get_risk_score: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_risk_score_request** | [**GetRiskScoreRequest**](GetRiskScoreRequest.md)|  | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]
 **before** | **str**| Optional ISO8601 formatted date string. Defaults to current date. Maximum date is 90 days ago. | [optional] 
 **after** | **str**| Optional ISO8601 formatted date string. Defaults to 30 days ago. Maximum date is 90 days ago. | [optional] 

### Return type

[**GetRiskScore200Response**](GetRiskScore200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_risk_scores**
> GetRiskScores200Response get_risk_scores(content_type=content_type)

Get Score Summary

Get Vigilance AI (Risk Service) Score Summary

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
    api_instance = onelogin.VigilanceAIApi(api_client)
    content_type = 'application/json' # str |  (optional) (default to 'application/json')

    try:
        # Get Score Summary
        api_response = api_instance.get_risk_scores(content_type=content_type)
        print("The response of VigilanceAIApi->get_risk_scores:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VigilanceAIApi->get_risk_scores: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]

### Return type

[**GetRiskScores200Response**](GetRiskScores200Response.md)

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

# **list_risk_rules**
> List[ListRiskRules200ResponseInner] list_risk_rules(content_type=content_type)

List Rules

List Vigilance AI (Risk Service) Rules

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
    api_instance = onelogin.VigilanceAIApi(api_client)
    content_type = 'application/json' # str |  (optional) (default to 'application/json')

    try:
        # List Rules
        api_response = api_instance.list_risk_rules(content_type=content_type)
        print("The response of VigilanceAIApi->list_risk_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VigilanceAIApi->list_risk_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]

### Return type

[**List[ListRiskRules200ResponseInner]**](ListRiskRules200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **track_risk_event**
> track_risk_event(track_risk_event_request, content_type=content_type)

Track an Event

Track Vigilance AI (Risk Service) Event

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
    api_instance = onelogin.VigilanceAIApi(api_client)
    track_risk_event_request = onelogin.TrackRiskEventRequest() # TrackRiskEventRequest | 
    content_type = 'application/json' # str |  (optional) (default to 'application/json')

    try:
        # Track an Event
        api_instance.track_risk_event(track_risk_event_request, content_type=content_type)
    except Exception as e:
        print("Exception when calling VigilanceAIApi->track_risk_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **track_risk_event_request** | [**TrackRiskEventRequest**](TrackRiskEventRequest.md)|  | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No content is returned. This API is fire and forget. |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_risk_rule**
> ListRiskRules200ResponseInner update_risk_rule(rule_id, update_risk_rule_request=update_risk_rule_request)

Update Rule

Update Vigilance AI (Risk Service) Rule

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
    api_instance = onelogin.VigilanceAIApi(api_client)
    rule_id = 'rule_id_example' # str | 
    update_risk_rule_request = onelogin.UpdateRiskRuleRequest() # UpdateRiskRuleRequest |  (optional)

    try:
        # Update Rule
        api_response = api_instance.update_risk_rule(rule_id, update_risk_rule_request=update_risk_rule_request)
        print("The response of VigilanceAIApi->update_risk_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VigilanceAIApi->update_risk_rule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rule_id** | **str**|  | 
 **update_risk_rule_request** | [**UpdateRiskRuleRequest**](UpdateRiskRuleRequest.md)|  | [optional] 

### Return type

[**ListRiskRules200ResponseInner**](ListRiskRules200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

