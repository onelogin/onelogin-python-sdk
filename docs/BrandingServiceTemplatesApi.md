# onelogin.BrandingServiceTemplatesApi

All URIs are relative to *https://your-api-subdomain.onelogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_message_template**](BrandingServiceTemplatesApi.md#create_message_template) | **POST** /api/2/branding/brands/{brand_id}/templates | Create Message Template
[**delete_message_template**](BrandingServiceTemplatesApi.md#delete_message_template) | **DELETE** /api/2/branding/brands/{brand_id}/templates/{template_id} | Delete Message Template
[**get_master_by_type**](BrandingServiceTemplatesApi.md#get_master_by_type) | **GET** /api/2/branding/brands/master/templates/{template_type} | Get Master Template by Type
[**get_message_template_by_id**](BrandingServiceTemplatesApi.md#get_message_template_by_id) | **GET** /api/2/branding/brands/{brand_id}/templates/{template_id} | Get Message Template
[**get_template_by_locale**](BrandingServiceTemplatesApi.md#get_template_by_locale) | **GET** /api/2/branding/brands/{brand_id}/templates/{template_type}/{locale} | Get Template by Type &amp; Locale
[**list_message_templates**](BrandingServiceTemplatesApi.md#list_message_templates) | **GET** /api/2/branding/brands/{brand_id}/templates | List Message Templates
[**update_message_template_by_id**](BrandingServiceTemplatesApi.md#update_message_template_by_id) | **PUT** /api/2/branding/brands/{brand_id}/templates/{template_id} | Update Message Template
[**update_template_by_locale**](BrandingServiceTemplatesApi.md#update_template_by_locale) | **PUT** /api/2/branding/brands/{brand_id}/templates/{template_type}/{locale} | Update Template by Type &amp; Locale


# **create_message_template**
> CreateMessageTemplateRequest create_message_template(brand_id, locale, create_message_template_request=create_message_template_request)

Create Message Template

Create Message Template

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
    api_instance = onelogin.BrandingServiceTemplatesApi(api_client)
    brand_id = 9 # int | Unique identifier for the branding object.
    locale = 'en' # str | The 2 character language locale for the template. e.g. en = English, es = Spanish
    create_message_template_request = {"type":"email_forgot_password","locale":"es","template":{"subject":"Password Reset","html":"<html><head></head><body><p>Please update your password by clicking <a href={{url}}>this link</a></p></body></html>","plain":"Please update your password by visiting this url: {{url}}"}} # CreateMessageTemplateRequest |  (optional)

    try:
        # Create Message Template
        api_response = api_instance.create_message_template(brand_id, locale, create_message_template_request=create_message_template_request)
        print("The response of BrandingServiceTemplatesApi->create_message_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingServiceTemplatesApi->create_message_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **int**| Unique identifier for the branding object. | 
 **locale** | **str**| The 2 character language locale for the template. e.g. en &#x3D; English, es &#x3D; Spanish | 
 **create_message_template_request** | [**CreateMessageTemplateRequest**](CreateMessageTemplateRequest.md)|  | [optional] 

### Return type

[**CreateMessageTemplateRequest**](CreateMessageTemplateRequest.md)

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

# **delete_message_template**
> delete_message_template(brand_id, template_id)

Delete Message Template

Delete Message Template

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
    api_instance = onelogin.BrandingServiceTemplatesApi(api_client)
    brand_id = 9 # int | Unique identifier for the branding object.
    template_id = 25 # int | Unique identifier for the template to return.

    try:
        # Delete Message Template
        api_instance.delete_message_template(brand_id, template_id)
    except Exception as e:
        print("Exception when calling BrandingServiceTemplatesApi->delete_message_template: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **int**| Unique identifier for the branding object. | 
 **template_id** | **int**| Unique identifier for the template to return. | 

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_master_by_type**
> CreateMessageTemplateRequest get_master_by_type(template_type)

Get Master Template by Type

Get Master Template by Type

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
    api_instance = onelogin.BrandingServiceTemplatesApi(api_client)
    template_type = 'email_template' # str | The message template type to return.

    try:
        # Get Master Template by Type
        api_response = api_instance.get_master_by_type(template_type)
        print("The response of BrandingServiceTemplatesApi->get_master_by_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingServiceTemplatesApi->get_master_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_type** | **str**| The message template type to return. | 

### Return type

[**CreateMessageTemplateRequest**](CreateMessageTemplateRequest.md)

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

# **get_message_template_by_id**
> CreateMessageTemplateRequest get_message_template_by_id(brand_id, template_id)

Get Message Template

Get Message Template by ID

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
    api_instance = onelogin.BrandingServiceTemplatesApi(api_client)
    brand_id = 9 # int | Unique identifier for the branding object.
    template_id = 25 # int | Unique identifier for the template to return.

    try:
        # Get Message Template
        api_response = api_instance.get_message_template_by_id(brand_id, template_id)
        print("The response of BrandingServiceTemplatesApi->get_message_template_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingServiceTemplatesApi->get_message_template_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **int**| Unique identifier for the branding object. | 
 **template_id** | **int**| Unique identifier for the template to return. | 

### Return type

[**CreateMessageTemplateRequest**](CreateMessageTemplateRequest.md)

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

# **get_template_by_locale**
> CreateMessageTemplateRequest get_template_by_locale(brand_id, template_type, locale)

Get Template by Type & Locale

Get Template by Type and Locale

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
    api_instance = onelogin.BrandingServiceTemplatesApi(api_client)
    brand_id = 9 # int | Unique identifier for the branding object.
    template_type = 'email_template' # str | The message template type to return.
    locale = 'en' # str | The 2 character language locale for the template. e.g. en = English, es = Spanish

    try:
        # Get Template by Type & Locale
        api_response = api_instance.get_template_by_locale(brand_id, template_type, locale)
        print("The response of BrandingServiceTemplatesApi->get_template_by_locale:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingServiceTemplatesApi->get_template_by_locale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **int**| Unique identifier for the branding object. | 
 **template_type** | **str**| The message template type to return. | 
 **locale** | **str**| The 2 character language locale for the template. e.g. en &#x3D; English, es &#x3D; Spanish | 

### Return type

[**CreateMessageTemplateRequest**](CreateMessageTemplateRequest.md)

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

# **list_message_templates**
> List[ListMessageTemplates200ResponseInner] list_message_templates(brand_id, locale)

List Message Templates

List Message Templates

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
    api_instance = onelogin.BrandingServiceTemplatesApi(api_client)
    brand_id = 9 # int | Unique identifier for the branding object.
    locale = 'en' # str | The 2 character language locale for the template. e.g. en = English, es = Spanish

    try:
        # List Message Templates
        api_response = api_instance.list_message_templates(brand_id, locale)
        print("The response of BrandingServiceTemplatesApi->list_message_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingServiceTemplatesApi->list_message_templates: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **int**| Unique identifier for the branding object. | 
 **locale** | **str**| The 2 character language locale for the template. e.g. en &#x3D; English, es &#x3D; Spanish | 

### Return type

[**List[ListMessageTemplates200ResponseInner]**](ListMessageTemplates200ResponseInner.md)

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
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_message_template_by_id**
> CreateMessageTemplateRequest update_message_template_by_id(brand_id, template_id)

Update Message Template

Update Message Template by ID

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
    api_instance = onelogin.BrandingServiceTemplatesApi(api_client)
    brand_id = 9 # int | Unique identifier for the branding object.
    template_id = 25 # int | Unique identifier for the template to return.

    try:
        # Update Message Template
        api_response = api_instance.update_message_template_by_id(brand_id, template_id)
        print("The response of BrandingServiceTemplatesApi->update_message_template_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingServiceTemplatesApi->update_message_template_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **int**| Unique identifier for the branding object. | 
 **template_id** | **int**| Unique identifier for the template to return. | 

### Return type

[**CreateMessageTemplateRequest**](CreateMessageTemplateRequest.md)

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
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template_by_locale**
> CreateMessageTemplateRequest update_template_by_locale(brand_id, template_type, locale)

Update Template by Type & Locale

Update Template by Type and Locale

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
    api_instance = onelogin.BrandingServiceTemplatesApi(api_client)
    brand_id = 9 # int | Unique identifier for the branding object.
    template_type = 'email_template' # str | The message template type to return.
    locale = 'en' # str | The 2 character language locale for the template. e.g. en = English, es = Spanish

    try:
        # Update Template by Type & Locale
        api_response = api_instance.update_template_by_locale(brand_id, template_type, locale)
        print("The response of BrandingServiceTemplatesApi->update_template_by_locale:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingServiceTemplatesApi->update_template_by_locale: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **int**| Unique identifier for the branding object. | 
 **template_type** | **str**| The message template type to return. | 
 **locale** | **str**| The 2 character language locale for the template. e.g. en &#x3D; English, es &#x3D; Spanish | 

### Return type

[**CreateMessageTemplateRequest**](CreateMessageTemplateRequest.md)

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

