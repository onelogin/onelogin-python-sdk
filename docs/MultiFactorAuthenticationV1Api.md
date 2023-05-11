# onelogin.MultiFactorAuthenticationV1Api

All URIs are relative to *https://your-api-subdomain.onelogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_mfa_factors**](MultiFactorAuthenticationV1Api.md#activate_mfa_factors) | **POST** /api/1/users/{user_id}/otp_devices/{device_id}/trigger | Activate a Factor
[**enroll_mfa_factor**](MultiFactorAuthenticationV1Api.md#enroll_mfa_factor) | **POST** /api/1/users/{user_id}/otp_devices | Enroll a Factor
[**generate_mf_atoken**](MultiFactorAuthenticationV1Api.md#generate_mf_atoken) | **POST** /api/1/users/{user_id}/mfa_token | Generate Temp MFA Token
[**get_enrolled_factors**](MultiFactorAuthenticationV1Api.md#get_enrolled_factors) | **GET** /api/1/users/{user_id}/otp_devices | Get Enrolled Factors
[**get_mfa_factors**](MultiFactorAuthenticationV1Api.md#get_mfa_factors) | **GET** /api/1/users/{user_id}/auth_factor | Get Available Factors
[**remove_mfa_factors**](MultiFactorAuthenticationV1Api.md#remove_mfa_factors) | **DELETE** /api/1/users/{user_id}/otp_devices/{device_id} | Remove an Enrolled Factor
[**verify_mfa_factor**](MultiFactorAuthenticationV1Api.md#verify_mfa_factor) | **POST** /api/1/users/{user_id}/otp_devices/{device_id}/verify | Verify a Factor


# **activate_mfa_factors**
> GetEnrolledFactors200Response activate_mfa_factors(user_id, device_id, activate_mfa_factors_request=activate_mfa_factors_request)

Activate a Factor

Activate a Factor

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
    api_instance = onelogin.MultiFactorAuthenticationV1Api(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.
    device_id = 'device_id_example' # str | 
    activate_mfa_factors_request = onelogin.ActivateMfaFactorsRequest() # ActivateMfaFactorsRequest |  (optional)

    try:
        # Activate a Factor
        api_response = api_instance.activate_mfa_factors(user_id, device_id, activate_mfa_factors_request=activate_mfa_factors_request)
        print("The response of MultiFactorAuthenticationV1Api->activate_mfa_factors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiFactorAuthenticationV1Api->activate_mfa_factors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Set to the id of the user that you want to return. | 
 **device_id** | **str**|  | 
 **activate_mfa_factors_request** | [**ActivateMfaFactorsRequest**](ActivateMfaFactorsRequest.md)|  | [optional] 

### Return type

[**GetEnrolledFactors200Response**](GetEnrolledFactors200Response.md)

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

# **enroll_mfa_factor**
> EnrollMfaFactor200Response enroll_mfa_factor(user_id, otp_device=otp_device)

Enroll a Factor

 Enroll an Authentication Factor

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
    api_instance = onelogin.MultiFactorAuthenticationV1Api(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.
    otp_device = onelogin.OtpDevice() # OtpDevice |  (optional)

    try:
        # Enroll a Factor
        api_response = api_instance.enroll_mfa_factor(user_id, otp_device=otp_device)
        print("The response of MultiFactorAuthenticationV1Api->enroll_mfa_factor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiFactorAuthenticationV1Api->enroll_mfa_factor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Set to the id of the user that you want to return. | 
 **otp_device** | [**OtpDevice**](OtpDevice.md)|  | [optional] 

### Return type

[**EnrollMfaFactor200Response**](EnrollMfaFactor200Response.md)

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

# **generate_mf_atoken**
> GenerateMFAtoken200Response generate_mf_atoken(user_id, generate_mf_atoken_request=generate_mf_atoken_request)

Generate Temp MFA Token

Generate MFA Token

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
    api_instance = onelogin.MultiFactorAuthenticationV1Api(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.
    generate_mf_atoken_request = onelogin.GenerateMFAtokenRequest() # GenerateMFAtokenRequest |  (optional)

    try:
        # Generate Temp MFA Token
        api_response = api_instance.generate_mf_atoken(user_id, generate_mf_atoken_request=generate_mf_atoken_request)
        print("The response of MultiFactorAuthenticationV1Api->generate_mf_atoken:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiFactorAuthenticationV1Api->generate_mf_atoken: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Set to the id of the user that you want to return. | 
 **generate_mf_atoken_request** | [**GenerateMFAtokenRequest**](GenerateMFAtokenRequest.md)|  | [optional] 

### Return type

[**GenerateMFAtoken200Response**](GenerateMFAtoken200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enrolled_factors**
> GetEnrolledFactors200Response get_enrolled_factors(user_id)

Get Enrolled Factors

Get Enrolled Factors

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
    api_instance = onelogin.MultiFactorAuthenticationV1Api(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.

    try:
        # Get Enrolled Factors
        api_response = api_instance.get_enrolled_factors(user_id)
        print("The response of MultiFactorAuthenticationV1Api->get_enrolled_factors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiFactorAuthenticationV1Api->get_enrolled_factors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Set to the id of the user that you want to return. | 

### Return type

[**GetEnrolledFactors200Response**](GetEnrolledFactors200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mfa_factors**
> GetMFAFactors200Response get_mfa_factors(user_id)

Get Available Factors

Get MFA Factors

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
    api_instance = onelogin.MultiFactorAuthenticationV1Api(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.

    try:
        # Get Available Factors
        api_response = api_instance.get_mfa_factors(user_id)
        print("The response of MultiFactorAuthenticationV1Api->get_mfa_factors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiFactorAuthenticationV1Api->get_mfa_factors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Set to the id of the user that you want to return. | 

### Return type

[**GetMFAFactors200Response**](GetMFAFactors200Response.md)

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

# **remove_mfa_factors**
> remove_mfa_factors(user_id, device_id)

Remove an Enrolled Factor

Remove an enrolled MFA device for a user

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
    api_instance = onelogin.MultiFactorAuthenticationV1Api(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.
    device_id = 'device_id_example' # str | 

    try:
        # Remove an Enrolled Factor
        api_instance.remove_mfa_factors(user_id, device_id)
    except Exception as e:
        print("Exception when calling MultiFactorAuthenticationV1Api->remove_mfa_factors: %s\n" % e)
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
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_mfa_factor**
> Error verify_mfa_factor(user_id, device_id, verify_mfa_factor_request=verify_mfa_factor_request)

Verify a Factor

Verify a Factor

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
    api_instance = onelogin.MultiFactorAuthenticationV1Api(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.
    device_id = 'device_id_example' # str | 
    verify_mfa_factor_request = onelogin.VerifyMfaFactorRequest() # VerifyMfaFactorRequest |  (optional)

    try:
        # Verify a Factor
        api_response = api_instance.verify_mfa_factor(user_id, device_id, verify_mfa_factor_request=verify_mfa_factor_request)
        print("The response of MultiFactorAuthenticationV1Api->verify_mfa_factor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MultiFactorAuthenticationV1Api->verify_mfa_factor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Set to the id of the user that you want to return. | 
 **device_id** | **str**|  | 
 **verify_mfa_factor_request** | [**VerifyMfaFactorRequest**](VerifyMfaFactorRequest.md)|  | [optional] 

### Return type

[**Error**](Error.md)

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

