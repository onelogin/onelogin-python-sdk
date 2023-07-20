<a id="__pageTop"></a>
# onelogin.apis.tags.branding_service_templates_api.BrandingServiceTemplatesApi

All URIs are relative to *https://your-api-subdomain.onelogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_message_template**](#create_message_template) | **post** /api/2/branding/brands/{brand_id}/templates | Create Message Template
[**delete_message_template**](#delete_message_template) | **delete** /api/2/branding/brands/{brand_id}/templates/{template_id} | Delete Message Template
[**get_master_by_type**](#get_master_by_type) | **get** /api/2/branding/brands/master/templates/{template_type} | Get Master Template by Type
[**get_message_template_by_id**](#get_message_template_by_id) | **get** /api/2/branding/brands/{brand_id}/templates/{template_id} | Get Message Template
[**get_template_by_locale**](#get_template_by_locale) | **get** /api/2/branding/brands/{brand_id}/templates/{template_type}/{locale} | Get Template by Type &amp; Locale
[**list_message_templates**](#list_message_templates) | **get** /api/2/branding/brands/{brand_id}/templates | List Message Templates
[**update_message_template_by_id**](#update_message_template_by_id) | **put** /api/2/branding/brands/{brand_id}/templates/{template_id} | Update Message Template
[**update_template_by_locale**](#update_template_by_locale) | **put** /api/2/branding/brands/{brand_id}/templates/{template_type}/{locale} | Update Template by Type &amp; Locale

# **create_message_template**
<a id="create_message_template"></a>
> MessageTemplate create_message_template(brand_id)

Create Message Template

Create Message Template

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import branding_service_templates_api
from onelogin.model.message_template import MessageTemplate
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
    api_instance = branding_service_templates_api.BrandingServiceTemplatesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'brand_id': 9,
    }
    query_params = {
    }
    try:
        # Create Message Template
        api_response = api_instance.create_message_template(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling BrandingServiceTemplatesApi->create_message_template: %s\n" % e)

    # example passing only optional values
    path_params = {
        'brand_id': 9,
    }
    query_params = {
        'locale': "en",
    }
    body = MessageTemplate(
        id=544880,
        account_id=118462,
        type="email_forgot_password",
        locale="en",
        template=None,
        template_class="email_template",
        updated_at="2021-11-24T21:25:29.480Z",
        brand_id=5,
    )
    try:
        # Create Message Template
        api_response = api_instance.create_message_template(
            path_params=path_params,
            query_params=query_params,
            body=body,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling BrandingServiceTemplatesApi->create_message_template: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
query_params | RequestQueryParams | |
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
[**MessageTemplate**](../../models/MessageTemplate.md) |  | 


### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
locale | LocaleSchema | | optional


# LocaleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
brand_id | BrandIdSchema | | 

# BrandIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_message_template.ApiResponseFor200) | Successful response
401 | [ApiResponseFor401](#create_message_template.ApiResponseFor401) | Unauthorized
422 | [ApiResponseFor422](#create_message_template.ApiResponseFor422) | Unprocessable Entity

#### create_message_template.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MessageTemplate**](../../models/MessageTemplate.md) |  | 


#### create_message_template.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


#### create_message_template.ApiResponseFor422
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

# **delete_message_template**
<a id="delete_message_template"></a>
> delete_message_template(brand_idtemplate_id)

Delete Message Template

Delete Message Template

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import branding_service_templates_api
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
    api_instance = branding_service_templates_api.BrandingServiceTemplatesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'brand_id': 9,
        'template_id': 25,
    }
    try:
        # Delete Message Template
        api_response = api_instance.delete_message_template(
            path_params=path_params,
        )
    except onelogin.ApiException as e:
        print("Exception when calling BrandingServiceTemplatesApi->delete_message_template: %s\n" % e)
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
brand_id | BrandIdSchema | | 
template_id | TemplateIdSchema | | 

# BrandIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TemplateIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_message_template.ApiResponseFor204) | No Content
404 | [ApiResponseFor404](#delete_message_template.ApiResponseFor404) | Not Found

#### delete_message_template.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_message_template.ApiResponseFor404
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

# **get_master_by_type**
<a id="get_master_by_type"></a>
> MessageTemplate get_master_by_type(template_type)

Get Master Template by Type

Get Master Template by Type

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import branding_service_templates_api
from onelogin.model.message_template import MessageTemplate
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
    api_instance = branding_service_templates_api.BrandingServiceTemplatesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'template_type': "email_template",
    }
    try:
        # Get Master Template by Type
        api_response = api_instance.get_master_by_type(
            path_params=path_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling BrandingServiceTemplatesApi->get_master_by_type: %s\n" % e)
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
template_type | TemplateTypeSchema | | 

# TemplateTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_master_by_type.ApiResponseFor200) | Successful response
401 | [ApiResponseFor401](#get_master_by_type.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_master_by_type.ApiResponseFor404) | Not Found

#### get_master_by_type.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MessageTemplate**](../../models/MessageTemplate.md) |  | 


#### get_master_by_type.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


#### get_master_by_type.ApiResponseFor404
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

# **get_message_template_by_id**
<a id="get_message_template_by_id"></a>
> MessageTemplate get_message_template_by_id(brand_idtemplate_id)

Get Message Template

Get Message Template by ID

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import branding_service_templates_api
from onelogin.model.message_template import MessageTemplate
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
    api_instance = branding_service_templates_api.BrandingServiceTemplatesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'brand_id': 9,
        'template_id': 25,
    }
    try:
        # Get Message Template
        api_response = api_instance.get_message_template_by_id(
            path_params=path_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling BrandingServiceTemplatesApi->get_message_template_by_id: %s\n" % e)
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
brand_id | BrandIdSchema | | 
template_id | TemplateIdSchema | | 

# BrandIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TemplateIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_message_template_by_id.ApiResponseFor200) | Successful response
401 | [ApiResponseFor401](#get_message_template_by_id.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_message_template_by_id.ApiResponseFor404) | Not Found

#### get_message_template_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MessageTemplate**](../../models/MessageTemplate.md) |  | 


#### get_message_template_by_id.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


#### get_message_template_by_id.ApiResponseFor404
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

# **get_template_by_locale**
<a id="get_template_by_locale"></a>
> MessageTemplate get_template_by_locale(brand_idtemplate_typelocale)

Get Template by Type & Locale

Get Template by Type and Locale

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import branding_service_templates_api
from onelogin.model.message_template import MessageTemplate
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
    api_instance = branding_service_templates_api.BrandingServiceTemplatesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'brand_id': 9,
        'template_type': "email_template",
        'locale': "en",
    }
    try:
        # Get Template by Type & Locale
        api_response = api_instance.get_template_by_locale(
            path_params=path_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling BrandingServiceTemplatesApi->get_template_by_locale: %s\n" % e)
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
brand_id | BrandIdSchema | | 
template_type | TemplateTypeSchema | | 
locale | LocaleSchema | | 

# BrandIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TemplateTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LocaleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_template_by_locale.ApiResponseFor200) | Successful response
401 | [ApiResponseFor401](#get_template_by_locale.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_template_by_locale.ApiResponseFor404) | Not Found

#### get_template_by_locale.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MessageTemplate**](../../models/MessageTemplate.md) |  | 


#### get_template_by_locale.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


#### get_template_by_locale.ApiResponseFor404
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

# **list_message_templates**
<a id="list_message_templates"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] list_message_templates(brand_id)

List Message Templates

List Message Templates

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import branding_service_templates_api
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
    api_instance = branding_service_templates_api.BrandingServiceTemplatesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'brand_id': 9,
    }
    query_params = {
    }
    try:
        # List Message Templates
        api_response = api_instance.list_message_templates(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling BrandingServiceTemplatesApi->list_message_templates: %s\n" % e)

    # example passing only optional values
    path_params = {
        'brand_id': 9,
    }
    query_params = {
        'locale': "en",
    }
    try:
        # List Message Templates
        api_response = api_instance.list_message_templates(
            path_params=path_params,
            query_params=query_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling BrandingServiceTemplatesApi->list_message_templates: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
query_params | RequestQueryParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### query_params
#### RequestQueryParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
locale | LocaleSchema | | optional


# LocaleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
brand_id | BrandIdSchema | | 

# BrandIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_message_templates.ApiResponseFor200) | Successful response
401 | [ApiResponseFor401](#list_message_templates.ApiResponseFor401) | Unauthorized
422 | [ApiResponseFor422](#list_message_templates.ApiResponseFor422) | Unprocessable Entity

#### list_message_templates.ApiResponseFor200
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
[items](#items) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# items

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  | template ID | [optional] 
**enabled** | bool,  | BoolClass,  | indicator if template is enabled | [optional] 
**name** | str,  | str,  | name of message template | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### list_message_templates.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


#### list_message_templates.ApiResponseFor422
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

# **update_message_template_by_id**
<a id="update_message_template_by_id"></a>
> MessageTemplate update_message_template_by_id(brand_idtemplate_id)

Update Message Template

Update Message Template by ID

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import branding_service_templates_api
from onelogin.model.message_template import MessageTemplate
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
    api_instance = branding_service_templates_api.BrandingServiceTemplatesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'brand_id': 9,
        'template_id': 25,
    }
    try:
        # Update Message Template
        api_response = api_instance.update_message_template_by_id(
            path_params=path_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling BrandingServiceTemplatesApi->update_message_template_by_id: %s\n" % e)
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
brand_id | BrandIdSchema | | 
template_id | TemplateIdSchema | | 

# BrandIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TemplateIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_message_template_by_id.ApiResponseFor200) | Successful response
401 | [ApiResponseFor401](#update_message_template_by_id.ApiResponseFor401) | Unauthorized
422 | [ApiResponseFor422](#update_message_template_by_id.ApiResponseFor422) | Unprocessable Entity

#### update_message_template_by_id.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MessageTemplate**](../../models/MessageTemplate.md) |  | 


#### update_message_template_by_id.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


#### update_message_template_by_id.ApiResponseFor422
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

# **update_template_by_locale**
<a id="update_template_by_locale"></a>
> MessageTemplate update_template_by_locale(brand_idtemplate_typelocale)

Update Template by Type & Locale

Update Template by Type and Locale

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import branding_service_templates_api
from onelogin.model.message_template import MessageTemplate
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
    api_instance = branding_service_templates_api.BrandingServiceTemplatesApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'brand_id': 9,
        'template_type': "email_template",
        'locale': "en",
    }
    try:
        # Update Template by Type & Locale
        api_response = api_instance.update_template_by_locale(
            path_params=path_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling BrandingServiceTemplatesApi->update_template_by_locale: %s\n" % e)
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
brand_id | BrandIdSchema | | 
template_type | TemplateTypeSchema | | 
locale | LocaleSchema | | 

# BrandIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# TemplateTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# LocaleSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_template_by_locale.ApiResponseFor200) | Successful response
401 | [ApiResponseFor401](#update_template_by_locale.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#update_template_by_locale.ApiResponseFor404) | Not Found

#### update_template_by_locale.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**MessageTemplate**](../../models/MessageTemplate.md) |  | 


#### update_template_by_locale.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


#### update_template_by_locale.ApiResponseFor404
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

