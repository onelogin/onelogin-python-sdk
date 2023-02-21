# onelogin.MultiFactorAuthenticationApi

All URIs are relative to *https://your-api-subdomain.onelogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device_verification**](MultiFactorAuthenticationApi.md#create_device_verification) | **POST** /api/2/mfa/users/{user_id}/verifications | Create Device Verification
[**create_factor_registration**](MultiFactorAuthenticationApi.md#create_factor_registration) | **POST** /api/2/mfa/users/{user_id}/registrations | Create Factor Registration
[**delete_enrolled_factor**](MultiFactorAuthenticationApi.md#delete_enrolled_factor) | **DELETE** /api/2/mfa/users/{user_id}/devices/{device_id} | Delete Enrolled Factor
[**generate_otp**](MultiFactorAuthenticationApi.md#generate_otp) | **POST** /api/2/mfa/users/{user_id}/mfa_token | Generate MFA token
[**get_auth_factors**](MultiFactorAuthenticationApi.md#get_auth_factors) | **GET** /api/2/mfa/users/{user_id}/factors | Get User Factors
[**get_authentication_devices**](MultiFactorAuthenticationApi.md#get_authentication_devices) | **GET** /api/2/mfa/users/{user_id}/devices | Get User Devices
[**get_user_registration**](MultiFactorAuthenticationApi.md#get_user_registration) | **GET** /api/2/mfa/users/{user_id}/registrations/{registration_id} | Get User Registration
[**get_user_verification**](MultiFactorAuthenticationApi.md#get_user_verification) | **GET** /api/2/mfa/users/{user_id}/verifications/{verification_id} | Get User Verification
[**verify_user_registration**](MultiFactorAuthenticationApi.md#verify_user_registration) | **PUT** /api/2/mfa/users/{user_id}/registrations/{registration_id} | Verify User Registration
[**verify_user_verification**](MultiFactorAuthenticationApi.md#verify_user_verification) | **PUT** /api/2/mfa/users/{user_id}/verifications/{verification_id} | Verify User Verification


# **create_device_verification**
> CreateDeviceVerification201Response create_device_verification(user_id, content_type=content_type, create_device_verification_request=create_device_verification_request)

Create Device Verification

Create a new verification process

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
    api_instance = onelogin.MultiFactorAuthenticationApi(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.
    content_type = 'application/json' # str |  (optional) (default to 'application/json')
    create_device_verification_request = onelogin.CreateDeviceVerificationRequest() # CreateDeviceVerificationRequest |  (optional)

    try:
        # Create Device Verification
        api_response = api_instance.create_device_verification(user_id, content_type=content_type, create_device_verification_request=create_device_verification_request)
        print("The response of MultiFactorAuthenticationApi->create_device_verification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiFactorAuthenticationApi->create_device_verification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Set to the id of the user that you want to return. | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]
 **create_device_verification_request** | [**CreateDeviceVerificationRequest**](CreateDeviceVerificationRequest.md)|  | [optional] 

### Return type

[**CreateDeviceVerification201Response**](CreateDeviceVerification201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Content-Type -  <br>  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_factor_registration**
> CreateFactorRegistration201Response create_factor_registration(user_id, content_type=content_type, create_factor_registration_request=create_factor_registration_request)

Create Factor Registration

Create a new registration process

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
    api_instance = onelogin.MultiFactorAuthenticationApi(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.
    content_type = 'application/json' # str |  (optional) (default to 'application/json')
    create_factor_registration_request = onelogin.CreateFactorRegistrationRequest() # CreateFactorRegistrationRequest |  (optional)

    try:
        # Create Factor Registration
        api_response = api_instance.create_factor_registration(user_id, content_type=content_type, create_factor_registration_request=create_factor_registration_request)
        print("The response of MultiFactorAuthenticationApi->create_factor_registration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiFactorAuthenticationApi->create_factor_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Set to the id of the user that you want to return. | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]
 **create_factor_registration_request** | [**CreateFactorRegistrationRequest**](CreateFactorRegistrationRequest.md)|  | [optional] 

### Return type

[**CreateFactorRegistration201Response**](CreateFactorRegistration201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Accept-Language -  <br>  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * X-Content-Type-Options -  <br>  * X-Request-Id -  <br>  * Date -  <br>  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_enrolled_factor**
> delete_enrolled_factor(user_id, device_id)

Delete Enrolled Factor

Delete a user\\'s authentication device

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
    api_instance = onelogin.MultiFactorAuthenticationApi(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.
    device_id = 'device_id_example' # str | 

    try:
        # Delete Enrolled Factor
        api_instance.delete_enrolled_factor(user_id, device_id)
    except Exception as e:
        print("Exception when calling MultiFactorAuthenticationApi->delete_enrolled_factor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Set to the id of the user that you want to return. | 
 **device_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_otp**
> GenerateOTP201Response generate_otp(user_id, content_type=content_type, generate_otp_request=generate_otp_request)

Generate MFA token

Create new MFA token on the user's account

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
    api_instance = onelogin.MultiFactorAuthenticationApi(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.
    content_type = 'application/json' # str |  (optional) (default to 'application/json')
    generate_otp_request = onelogin.GenerateOTPRequest() # GenerateOTPRequest |  (optional)

    try:
        # Generate MFA token
        api_response = api_instance.generate_otp(user_id, content_type=content_type, generate_otp_request=generate_otp_request)
        print("The response of MultiFactorAuthenticationApi->generate_otp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiFactorAuthenticationApi->generate_otp: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Set to the id of the user that you want to return. | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]
 **generate_otp_request** | [**GenerateOTPRequest**](GenerateOTPRequest.md)|  | [optional] 

### Return type

[**GenerateOTP201Response**](GenerateOTP201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Content-Type -  <br>  |
**401** | Unauthorized |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_factors**
> GetAuthFactors200Response get_auth_factors(user_id)

Get User Factors

Get a user\\'s available authentication factors

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
    api_instance = onelogin.MultiFactorAuthenticationApi(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.

    try:
        # Get User Factors
        api_response = api_instance.get_auth_factors(user_id)
        print("The response of MultiFactorAuthenticationApi->get_auth_factors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiFactorAuthenticationApi->get_auth_factors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Set to the id of the user that you want to return. | 

### Return type

[**GetAuthFactors200Response**](GetAuthFactors200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Content-Type -  <br>  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authentication_devices**
> List[GetAuthenticationDevices200ResponseInner] get_authentication_devices(user_id)

Get User Devices

Get a user authentication devices

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
    api_instance = onelogin.MultiFactorAuthenticationApi(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.

    try:
        # Get User Devices
        api_response = api_instance.get_authentication_devices(user_id)
        print("The response of MultiFactorAuthenticationApi->get_authentication_devices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiFactorAuthenticationApi->get_authentication_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Set to the id of the user that you want to return. | 

### Return type

[**List[GetAuthenticationDevices200ResponseInner]**](GetAuthenticationDevices200ResponseInner.md)

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

# **get_user_registration**
> object get_user_registration(user_id, registration_id)

Get User Registration

Get registration state by id

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
    api_instance = onelogin.MultiFactorAuthenticationApi(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.
    registration_id = '<UUID>' # str | The id of a registration

    try:
        # Get User Registration
        api_response = api_instance.get_user_registration(user_id, registration_id)
        print("The response of MultiFactorAuthenticationApi->get_user_registration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiFactorAuthenticationApi->get_user_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Set to the id of the user that you want to return. | 
 **registration_id** | **str**| The id of a registration | 

### Return type

**object**

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Accept-Language -  <br>  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * X-Content-Type-Options -  <br>  * X-Request-Id -  <br>  * Date -  <br>  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_verification**
> GetUserVerification200Response get_user_verification(user_id, verification_id)

Get User Verification

Get verification state by id

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
    api_instance = onelogin.MultiFactorAuthenticationApi(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.
    verification_id = '<UUID>' # str | The verification_id is returned on activation of the factor or you can get the device_id using the Activate Factor API call.

    try:
        # Get User Verification
        api_response = api_instance.get_user_verification(user_id, verification_id)
        print("The response of MultiFactorAuthenticationApi->get_user_verification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiFactorAuthenticationApi->get_user_verification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Set to the id of the user that you want to return. | 
 **verification_id** | **str**| The verification_id is returned on activation of the factor or you can get the device_id using the Activate Factor API call. | 

### Return type

[**GetUserVerification200Response**](GetUserVerification200Response.md)

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

# **verify_user_registration**
> VerifyUserRegistration200Response verify_user_registration(user_id, registration_id, content_type=content_type, verify_user_registration_request=verify_user_registration_request)

Verify User Registration

Submit an otp for verification.

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
    api_instance = onelogin.MultiFactorAuthenticationApi(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.
    registration_id = '<UUID>' # str | The id of a registration
    content_type = 'application/json' # str |  (optional) (default to 'application/json')
    verify_user_registration_request = onelogin.VerifyUserRegistrationRequest() # VerifyUserRegistrationRequest |  (optional)

    try:
        # Verify User Registration
        api_response = api_instance.verify_user_registration(user_id, registration_id, content_type=content_type, verify_user_registration_request=verify_user_registration_request)
        print("The response of MultiFactorAuthenticationApi->verify_user_registration:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiFactorAuthenticationApi->verify_user_registration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Set to the id of the user that you want to return. | 
 **registration_id** | **str**| The id of a registration | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]
 **verify_user_registration_request** | [**VerifyUserRegistrationRequest**](VerifyUserRegistrationRequest.md)|  | [optional] 

### Return type

[**VerifyUserRegistration200Response**](VerifyUserRegistration200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Accept-Language -  <br>  * Cache-Control -  <br>  * Content-Length -  <br>  * Content-Type -  <br>  * X-Content-Type-Options -  <br>  * X-Request-Id -  <br>  * Date -  <br>  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_user_verification**
> GenerateToken400Response verify_user_verification(user_id, verification_id, content_type=content_type, verify_user_verification_request=verify_user_verification_request)

Verify User Verification

Submit an otp for verification.

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
    api_instance = onelogin.MultiFactorAuthenticationApi(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.
    verification_id = '<UUID>' # str | The verification_id is returned on activation of the factor or you can get the device_id using the Activate Factor API call.
    content_type = 'application/json' # str |  (optional) (default to 'application/json')
    verify_user_verification_request = onelogin.VerifyUserVerificationRequest() # VerifyUserVerificationRequest |  (optional)

    try:
        # Verify User Verification
        api_response = api_instance.verify_user_verification(user_id, verification_id, content_type=content_type, verify_user_verification_request=verify_user_verification_request)
        print("The response of MultiFactorAuthenticationApi->verify_user_verification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiFactorAuthenticationApi->verify_user_verification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Set to the id of the user that you want to return. | 
 **verification_id** | **str**| The verification_id is returned on activation of the factor or you can get the device_id using the Activate Factor API call. | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]
 **verify_user_verification_request** | [**VerifyUserVerificationRequest**](VerifyUserVerificationRequest.md)|  | [optional] 

### Return type

[**GenerateToken400Response**](GenerateToken400Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Content-Type -  <br>  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

