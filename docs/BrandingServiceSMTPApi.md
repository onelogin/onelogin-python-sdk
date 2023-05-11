# onelogin.BrandingServiceSMTPApi

All URIs are relative to *https://your-api-subdomain.onelogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_email_settings**](BrandingServiceSMTPApi.md#delete_email_settings) | **DELETE** /api/2/branding/email_settings | Delete Custom Email Settings
[**get_email_settings**](BrandingServiceSMTPApi.md#get_email_settings) | **GET** /api/2/branding/email_settings | Get Email Settings
[**update_email_settings**](BrandingServiceSMTPApi.md#update_email_settings) | **PUT** /api/2/branding/email_settings | Update Email Settings


# **delete_email_settings**
> AltErr delete_email_settings()

Delete Custom Email Settings

Reset Email Setting config

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
    api_instance = onelogin.BrandingServiceSMTPApi(api_client)

    try:
        # Delete Custom Email Settings
        api_response = api_instance.delete_email_settings()
        print("The response of BrandingServiceSMTPApi->delete_email_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingServiceSMTPApi->delete_email_settings: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**AltErr**](AltErr.md)

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

# **get_email_settings**
> GetEmailSettings200Response get_email_settings()

Get Email Settings

Get Email Settings Config

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
    api_instance = onelogin.BrandingServiceSMTPApi(api_client)

    try:
        # Get Email Settings
        api_response = api_instance.get_email_settings()
        print("The response of BrandingServiceSMTPApi->get_email_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingServiceSMTPApi->get_email_settings: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**GetEmailSettings200Response**](GetEmailSettings200Response.md)

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

# **update_email_settings**
> AltErr update_email_settings(email_config=email_config)

Update Email Settings

Update Email Settings Config

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
    api_instance = onelogin.BrandingServiceSMTPApi(api_client)
    email_config = onelogin.EmailConfig() # EmailConfig |  (optional)

    try:
        # Update Email Settings
        api_response = api_instance.update_email_settings(email_config=email_config)
        print("The response of BrandingServiceSMTPApi->update_email_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingServiceSMTPApi->update_email_settings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_config** | [**EmailConfig**](EmailConfig.md)|  | [optional] 

### Return type

[**AltErr**](AltErr.md)

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

