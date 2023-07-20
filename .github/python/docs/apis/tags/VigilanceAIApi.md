<a id="__pageTop"></a>
# onelogin.apis.tags.vigilance_ai_api.VigilanceAIApi

All URIs are relative to *https://your-api-subdomain.onelogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_risk_rule**](#create_risk_rule) | **post** /api/2/risk/rules | Create Rule
[**delete_risk_rule**](#delete_risk_rule) | **delete** /api/2/risk/rules/{rule_id} | Delete Rule
[**get_risk_rule**](#get_risk_rule) | **get** /api/2/risk/rules/{rule_id} | get Risk Rule
[**get_risk_score**](#get_risk_score) | **post** /api/2/risk/verify | Get a Risk Score
[**get_risk_scores**](#get_risk_scores) | **get** /api/2/risk/scores | Get Score Summary
[**list_risk_rules**](#list_risk_rules) | **get** /api/2/risk/rules | List Rules
[**track_risk_event**](#track_risk_event) | **post** /api/2/risk/events | Track an Event
[**update_risk_rule**](#update_risk_rule) | **put** /api/2/risk/rules/{rule_id} | Update Rule

# **create_risk_rule**
<a id="create_risk_rule"></a>
> RiskRule create_risk_rule()

Create Rule

Create Vigilance AI (Risk Service) Rule

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import vigilance_ai_api
from onelogin.model.error import Error
from onelogin.model.risk_rule import RiskRule
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
    api_instance = vigilance_ai_api.VigilanceAIApi(api_client)

    # example passing only optional values
    body = RiskRule(
        id="id_example",
        name="name_example",
        description="description_example",
        type="blacklist",
        target="location.ip",
        filters=[
            "filters_example"
        ],
        source=Source(
            id="id_example",
            name="name_example",
        ),
    )
    try:
        # Create Rule
        api_response = api_instance.create_risk_rule(
            body=body,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling VigilanceAIApi->create_risk_rule: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RiskRule**](../../models/RiskRule.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_risk_rule.ApiResponseFor201) | CREATED
400 | [ApiResponseFor400](#create_risk_rule.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#create_risk_rule.ApiResponseFor401) | Unauthorized

#### create_risk_rule.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RiskRule**](../../models/RiskRule.md) |  | 


#### create_risk_rule.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### create_risk_rule.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_risk_rule**
<a id="delete_risk_rule"></a>
> delete_risk_rule(rule_id)

Delete Rule

Delete Vigilance AI (Risk Service)

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import vigilance_ai_api
from onelogin.model.error import Error
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
    api_instance = vigilance_ai_api.VigilanceAIApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'rule_id': "rule_id_example",
    }
    try:
        # Delete Rule
        api_response = api_instance.delete_risk_rule(
            path_params=path_params,
        )
    except onelogin.ApiException as e:
        print("Exception when calling VigilanceAIApi->delete_risk_rule: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
rule_id | RuleIdSchema | | 

# RuleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_risk_rule.ApiResponseFor204) | Successful response
401 | [ApiResponseFor401](#delete_risk_rule.ApiResponseFor401) | Unauthorized

#### delete_risk_rule.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_risk_rule.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_risk_rule**
<a id="get_risk_rule"></a>
> RiskRule get_risk_rule(rule_id)

get Risk Rule

Use this API to return a single rule that has been created in the Risk Sevice.

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import vigilance_ai_api
from onelogin.model.error import Error
from onelogin.model.risk_rule import RiskRule
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
    api_instance = vigilance_ai_api.VigilanceAIApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'rule_id': "rule_id_example",
    }
    try:
        # get Risk Rule
        api_response = api_instance.get_risk_rule(
            path_params=path_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling VigilanceAIApi->get_risk_rule: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
rule_id | RuleIdSchema | | 

# RuleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_risk_rule.ApiResponseFor200) | Successful Response
401 | [ApiResponseFor401](#get_risk_rule.ApiResponseFor401) | Unauthorized

#### get_risk_rule.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RiskRule**](../../models/RiskRule.md) |  | 


#### get_risk_rule.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_risk_score**
<a id="get_risk_score"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_risk_score(any_type)

Get a Risk Score

Get Vigilance AI (Risk Service) Score

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import vigilance_ai_api
from onelogin.model.error import Error
from onelogin.model.source import Source
from onelogin.model.session import Session
from onelogin.model.risk_device import RiskDevice
from onelogin.model.risk_user import RiskUser
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
    api_instance = vigilance_ai_api.VigilanceAIApi(api_client)

    # example passing only required values which don't have defaults set
    query_params = {
    }
    body = dict(
        ip="ip_example",
        user_agent="user_agent_example",
        user=RiskUser(
            id="id_example",
            name="name_example",
            authenticated=False,
        ),
        source=Source(
            id="id_example",
            name="name_example",
        ),
        session=Session(
            id="id_example",
        ),
        device=RiskDevice(
            id="id_example",
        ),
        fp="fp_example",
    )
    try:
        # Get a Risk Score
        api_response = api_instance.get_risk_score(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling VigilanceAIApi->get_risk_score: %s\n" % e)

    # example passing only optional values
    query_params = {
        'before': "before_example",
        'after': "after_example",
    }
    body = dict(
        ip="ip_example",
        user_agent="user_agent_example",
        user=RiskUser(
            id="id_example",
            name="name_example",
            authenticated=False,
        ),
        source=Source(
            id="id_example",
            name="name_example",
        ),
        session=Session(
            id="id_example",
        ),
        device=RiskDevice(
            id="id_example",
        ),
        fp="fp_example",
    )
    try:
        # Get a Risk Score
        api_response = api_instance.get_risk_score(
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling VigilanceAIApi->get_risk_score: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
query_params | RequestQueryParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ip** | str,  | str,  | The IP address of the User&#x27;s request. | 
**user** | [**RiskUser**]({{complexTypePrefix}}RiskUser.md) | [**RiskUser**]({{complexTypePrefix}}RiskUser.md) |  | 
**user_agent** | str,  | str,  | The user agent of the User&#x27;s request. | 
**source** | [**Source**]({{complexTypePrefix}}Source.md) | [**Source**]({{complexTypePrefix}}Source.md) |  | [optional] 
**session** | [**Session**]({{complexTypePrefix}}Session.md) | [**Session**]({{complexTypePrefix}}Session.md) |  | [optional] 
**device** | [**RiskDevice**]({{complexTypePrefix}}RiskDevice.md) | [**RiskDevice**]({{complexTypePrefix}}RiskDevice.md) |  | [optional] 
**fp** | str,  | str,  | Set to the value of the __tdli_fp cookie. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
before | BeforeSchema | | optional
after | AfterSchema | | optional


# BeforeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# AfterSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_risk_score.ApiResponseFor200) | Successful response
400 | [ApiResponseFor400](#get_risk_score.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#get_risk_score.ApiResponseFor401) | Unauthorized

#### get_risk_score.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**score** | decimal.Decimal, int, float,  | decimal.Decimal,  | A risk score 0 is low risk and 100 is the highest risk level possible. | [optional] 
**[triggers](#triggers)** | list, tuple,  | tuple,  | Triggers are indicators of some of the key items that influenced the risk score. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# triggers

Triggers are indicators of some of the key items that influenced the risk score.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Triggers are indicators of some of the key items that influenced the risk score. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

#### get_risk_score.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### get_risk_score.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_risk_scores**
<a id="get_risk_scores"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_risk_scores()

Get Score Summary

Get Vigilance AI (Risk Service) Score Summary

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import vigilance_ai_api
from onelogin.model.error import Error
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
    api_instance = vigilance_ai_api.VigilanceAIApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Get Score Summary
        api_response = api_instance.get_risk_scores()
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling VigilanceAIApi->get_risk_scores: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_risk_scores.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#get_risk_scores.ApiResponseFor401) | Unauthorized

#### get_risk_scores.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[scores](#scores)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | [optional] 
**total** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# scores

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**minimal** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**low** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**medium** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**high** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**very_high** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_risk_scores.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **list_risk_rules**
<a id="list_risk_rules"></a>
> [RiskRule] list_risk_rules()

List Rules

List Vigilance AI (Risk Service) Rules

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import vigilance_ai_api
from onelogin.model.error import Error
from onelogin.model.risk_rule import RiskRule
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
    api_instance = vigilance_ai_api.VigilanceAIApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Rules
        api_response = api_instance.list_risk_rules()
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling VigilanceAIApi->list_risk_rules: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_risk_rules.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#list_risk_rules.ApiResponseFor401) | Unauthorized

#### list_risk_rules.ApiResponseFor200
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
[**RiskRule**]({{complexTypePrefix}}RiskRule.md) | [**RiskRule**]({{complexTypePrefix}}RiskRule.md) | [**RiskRule**]({{complexTypePrefix}}RiskRule.md) |  | 

#### list_risk_rules.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **track_risk_event**
<a id="track_risk_event"></a>
> track_risk_event(any_type)

Track an Event

Track Vigilance AI (Risk Service) Event

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import vigilance_ai_api
from onelogin.model.error import Error
from onelogin.model.source import Source
from onelogin.model.session import Session
from onelogin.model.risk_device import RiskDevice
from onelogin.model.risk_user import RiskUser
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
    api_instance = vigilance_ai_api.VigilanceAIApi(api_client)

    # example passing only required values which don't have defaults set
    body = dict(
        verb="verb_example",
        ip="ip_example",
        user_agent="user_agent_example",
        user=RiskUser(
            id="id_example",
            name="name_example",
            authenticated=False,
        ),
        source=Source(
            id="id_example",
            name="name_example",
        ),
        session=Session(
            id="id_example",
        ),
        device=RiskDevice(
            id="id_example",
        ),
        fp="fp_example",
        published="published_example",
    )
    try:
        # Track an Event
        api_response = api_instance.track_risk_event(
            body=body,
        )
    except onelogin.ApiException as e:
        print("Exception when calling VigilanceAIApi->track_risk_event: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson] | required |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**ip** | str,  | str,  | The IP address of the User&#x27;s request. | 
**verb** | str,  | str,  | Verbs are used to distinguish between different types of events. | 
**user** | [**RiskUser**]({{complexTypePrefix}}RiskUser.md) | [**RiskUser**]({{complexTypePrefix}}RiskUser.md) |  | 
**user_agent** | str,  | str,  | The user agent of the User&#x27;s request. | 
**source** | [**Source**]({{complexTypePrefix}}Source.md) | [**Source**]({{complexTypePrefix}}Source.md) |  | [optional] 
**session** | [**Session**]({{complexTypePrefix}}Session.md) | [**Session**]({{complexTypePrefix}}Session.md) |  | [optional] 
**device** | [**RiskDevice**]({{complexTypePrefix}}RiskDevice.md) | [**RiskDevice**]({{complexTypePrefix}}RiskDevice.md) |  | [optional] 
**fp** | str,  | str,  | Set to the value of the __tdli_fp cookie. | [optional] 
**published** | str,  | str,  | Date and time of the event in IS08601 format. Useful for preloading old events. Defaults to date time this API request is received. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#track_risk_event.ApiResponseFor200) | No content is returned. This API is fire and forget.
400 | [ApiResponseFor400](#track_risk_event.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#track_risk_event.ApiResponseFor401) | Unauthorized

#### track_risk_event.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### track_risk_event.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### track_risk_event.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_risk_rule**
<a id="update_risk_rule"></a>
> RiskRule update_risk_rule(rule_id)

Update Rule

Update Vigilance AI (Risk Service) Rule

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import vigilance_ai_api
from onelogin.model.error import Error
from onelogin.model.risk_rule import RiskRule
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
    api_instance = vigilance_ai_api.VigilanceAIApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'rule_id': "rule_id_example",
    }
    try:
        # Update Rule
        api_response = api_instance.update_risk_rule(
            path_params=path_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling VigilanceAIApi->update_risk_rule: %s\n" % e)

    # example passing only optional values
    path_params = {
        'rule_id': "rule_id_example",
    }
    body = dict(
        id="id_example",
    )
    try:
        # Update Rule
        api_response = api_instance.update_risk_rule(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling VigilanceAIApi->update_risk_rule: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
path_params | RequestPathParams | |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | The ID of the Rule to Update | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
rule_id | RuleIdSchema | | 

# RuleIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_risk_rule.ApiResponseFor200) | Successful Response
400 | [ApiResponseFor400](#update_risk_rule.ApiResponseFor400) | Bad Request
401 | [ApiResponseFor401](#update_risk_rule.ApiResponseFor401) | Unauthorized

#### update_risk_rule.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**RiskRule**](../../models/RiskRule.md) |  | 


#### update_risk_rule.ApiResponseFor400
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor400ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor400ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


#### update_risk_rule.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

