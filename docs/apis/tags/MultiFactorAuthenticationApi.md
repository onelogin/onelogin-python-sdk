<a id="__pageTop"></a>
# onelogin.apis.tags.multi_factor_authentication_api.MultiFactorAuthenticationApi

All URIs are relative to *https://your-api-subdomain.onelogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_device_verification**](#create_device_verification) | **post** /api/2/mfa/users/{user_id}/verifications | Create Device Verification
[**create_factor_registration**](#create_factor_registration) | **post** /api/2/mfa/users/{user_id}/registrations | Create Factor Registration
[**delete_enrolled_factor**](#delete_enrolled_factor) | **delete** /api/2/mfa/users/{user_id}/devices/{device_id} | Delete Enrolled Factor
[**generate_otp**](#generate_otp) | **post** /api/2/mfa/users/{user_id}/mfa_token | Generate MFA token
[**get_auth_factors**](#get_auth_factors) | **get** /api/2/mfa/users/{user_id}/factors | Get User Factors
[**get_authentication_devices**](#get_authentication_devices) | **get** /api/2/mfa/users/{user_id}/devices | Get User Devices
[**get_user_registration**](#get_user_registration) | **get** /api/2/mfa/users/{user_id}/registrations/{registration_id} | Get User Registration
[**get_user_verification**](#get_user_verification) | **get** /api/2/mfa/users/{user_id}/verifications/{verification_id} | Get User Verification
[**verify_user_registration**](#verify_user_registration) | **put** /api/2/mfa/users/{user_id}/registrations/{registration_id} | Verify User Registration
[**verify_user_verification**](#verify_user_verification) | **put** /api/2/mfa/users/{user_id}/verifications/{verification_id} | Verify User Verification

# **create_device_verification**
<a id="create_device_verification"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_device_verification(user_id)

Create Device Verification

Create a new verification process

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import multi_factor_authentication_api
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
    api_instance = multi_factor_authentication_api.MultiFactorAuthenticationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'user_id': 1,
    }
    header_params = {
    }
    try:
        # Create Device Verification
        api_response = api_instance.create_device_verification(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling MultiFactorAuthenticationApi->create_device_verification: %s\n" % e)

    # example passing only optional values
    path_params = {
        'user_id': 1,
    }
    header_params = {
        'Content-Type': "application/json",
    }
    body = dict(
        device_id=58959,
        display_name="OneLogin SMS",
        expires_in="expires_in_example",
        redirect_to="redirect_to_example",
        custom_message="custom_message_example",
    )
    try:
        # Create Device Verification
        api_response = api_instance.create_device_verification(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling MultiFactorAuthenticationApi->create_device_verification: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
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
**device_id** | decimal.Decimal, int,  | decimal.Decimal,  | Specifies the factor to be verified. | 
**display_name** | str,  | str,  | A name for the users device | [optional] 
**expires_in** | str,  | str,  | Defaults to 120. Valid values are: 120-900 seconds. | [optional] 
**redirect_to** | str,  | str,  | Only applies to Email MagicLink factor. Redirects MagicLink success page to specified URL after 2 seconds. Email must already be configured by the user. | [optional] 
**custom_message** | str,  | str,  | Only applies to SMS factor. A message template that will be sent via SMS. Max length of the message after template items are inserted is 160 characters including the OTP code. SMS must already be configured by the user. The following template variables can be included in the message. - {{otp_code}} - The security code. - {{otp_expiry}} - The number of minutes until the one time code expires. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Content-Type | ContentTypeSchema | | optional

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "application/json"

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
user_id | UserIdSchema | | 

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_device_verification.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#create_device_verification.ApiResponseFor401) | Unauthorized

#### create_device_verification.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor201 |  |

# SchemaFor201ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**device_id** | decimal.Decimal, int,  | decimal.Decimal,  | Specifies the factor to be verified. | [optional] 
**display_name** | str,  | str,  | A name for the users device | [optional] 
**expires_at** | str,  | str,  | A short lived token that is required to Verify the Factor. This token expires based on the expires_in parameter passed in. | [optional] 
**redirect_to** | str,  | str,  | Only applies to Email MagicLink factor. Redirects MagicLink success page to specified URL after 2 seconds. Email must already be configured by the user. | [optional] 
**user_display_name** | str,  | str,  | Authentication factor display name assigned by users when they register the device. | [optional] 
**id** | str,  | str,  | Registration identifier. | [optional] 
**type_display_name** | str,  | str,  | Authentication factor display name as it appears to users upon initial registration, as defined by admins at Settings &gt; Authentication Factors. | [optional] 
**auth_factor_name** | str,  | str,  | Authentication factor name, as it appears to administrators in OneLogin. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]
#### ResponseHeadersFor201

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Content-Type | ContentTypeSchema | | optional

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### create_device_verification.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **create_factor_registration**
<a id="create_factor_registration"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} create_factor_registration(user_id)

Create Factor Registration

Create a new registration process

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import multi_factor_authentication_api
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
    api_instance = multi_factor_authentication_api.MultiFactorAuthenticationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'user_id': 1,
    }
    header_params = {
    }
    try:
        # Create Factor Registration
        api_response = api_instance.create_factor_registration(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling MultiFactorAuthenticationApi->create_factor_registration: %s\n" % e)

    # example passing only optional values
    path_params = {
        'user_id': 1,
    }
    header_params = {
        'Content-Type': "application/json",
    }
    body = dict(
        factor_id=58959,
        display_name="OneLogin SMS",
        expires_in="expires_in_example",
        verified=True,
        redirect_to="redirect_to_example",
        custom_message="custom_message_example",
    )
    try:
        # Create Factor Registration
        api_response = api_instance.create_factor_registration(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling MultiFactorAuthenticationApi->create_factor_registration: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
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
**factor_id** | decimal.Decimal, int,  | decimal.Decimal,  | The identifier of the factor to enroll the user with. See Get Available Factors for a list of possible id values. | 
**display_name** | str,  | str,  | A name for the users device | 
**expires_in** | str,  | str,  | Defaults to 120. Valid values are: 120-900 seconds. | [optional] 
**verified** | bool,  | BoolClass,  | Defaults to false. The following factors support verified &#x3D; true as part of the initial registration request: OneLogin SMS, OneLogin Voice, OneLogin Email. When using verified &#x3D; true it is critical that the supported factors have pre-verified values, most likely imported from an existing directory or by the users themselvdes. Factors such as Authenticator and OneLogin Protect do not support verification &#x3D; true as the user interaction is required to verify the factor. | [optional] 
**redirect_to** | str,  | str,  | Only applies to Email MagicLink factor. Redirects MagicLink success page to specified URL after 2 seconds. Email must already be configured by the user. | [optional] 
**custom_message** | str,  | str,  | Only applies to SMS factor. A message template that will be sent via SMS. Max length of the message after template items are inserted is 160 characters including the OTP code. SMS must already be configured by the user. The following template variables can be included in the message. - {{otp_code}} - The security code. - {{otp_expiry}} - The number of minutes until the one time code expires. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Content-Type | ContentTypeSchema | | optional

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "application/json"

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
user_id | UserIdSchema | | 

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_factor_registration.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#create_factor_registration.ApiResponseFor401) | Unauthorized

#### create_factor_registration.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor201 |  |

# SchemaFor201ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**device_id** | str,  | str,  | MFA device identifier. | [optional] 
**user_display_name** | str,  | str,  | Authentication factor display name assigned by users when they register the device. | [optional] 
**type_display_name** | str,  | str,  | Authentication factor display name as it appears to users upon initial registration, as defined by admins at Settings &gt; Authentication Factors. | [optional] 
**auth_factor_name** | str,  | str,  | Authentication factor name, as it appears to administrators in OneLogin. | [optional] 
**id** | str,  | str,  | Verification identifier used in subsequent verification step. | [optional] 
**user_id** | str,  | str,  | User identifier | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]
#### ResponseHeadersFor201

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Accept-Language | AcceptLanguageSchema | | optional
Cache-Control | CacheControlSchema | | optional
Content-Length | ContentLengthSchema | | optional
Content-Type | ContentTypeSchema | | optional
X-Content-Type-Options | XContentTypeOptionsSchema | | optional
X-Request-Id | XRequestIdSchema | | optional
Date | DateSchema | | optional

# AcceptLanguageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CacheControlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentLengthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XContentTypeOptionsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XRequestIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### create_factor_registration.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **delete_enrolled_factor**
<a id="delete_enrolled_factor"></a>
> delete_enrolled_factor(user_iddevice_id)

Delete Enrolled Factor

Delete a user\\'s authentication device

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import multi_factor_authentication_api
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
    api_instance = multi_factor_authentication_api.MultiFactorAuthenticationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'user_id': 1,
        'device_id': "device_id_example",
    }
    try:
        # Delete Enrolled Factor
        api_response = api_instance.delete_enrolled_factor(
            path_params=path_params,
        )
    except onelogin.ApiException as e:
        print("Exception when calling MultiFactorAuthenticationApi->delete_enrolled_factor: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
user_id | UserIdSchema | | 
device_id | DeviceIdSchema | | 

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# DeviceIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_enrolled_factor.ApiResponseFor204) | No Content

#### delete_enrolled_factor.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **generate_otp**
<a id="generate_otp"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} generate_otp(user_id)

Generate MFA token

Create new MFA token on the user's account

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import multi_factor_authentication_api
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
    api_instance = multi_factor_authentication_api.MultiFactorAuthenticationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'user_id': 1,
    }
    header_params = {
    }
    try:
        # Generate MFA token
        api_response = api_instance.generate_otp(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling MultiFactorAuthenticationApi->generate_otp: %s\n" % e)

    # example passing only optional values
    path_params = {
        'user_id': 1,
    }
    header_params = {
        'Content-Type': "application/json",
    }
    body = dict(
        expires_in=300,
        reusable=False,
    )
    try:
        # Generate MFA token
        api_response = api_instance.generate_otp(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling MultiFactorAuthenticationApi->generate_otp: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
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
**expires_in** | decimal.Decimal, int,  | decimal.Decimal,  | Set the duration of the token in seconds. Token expiration defaults to 259200 seconds &#x3D; 72 hours. 72 hours is the max value. | [optional] 
**reusable** | bool,  | BoolClass,  | Defines if the token is reusable multiple times within the expiry window. Value defaults to false. If set to true, token can be used multiple times, until it expires. | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Content-Type | ContentTypeSchema | | optional

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "application/json"

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
user_id | UserIdSchema | | 

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#generate_otp.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#generate_otp.ApiResponseFor401) | Unauthorized
422 | [ApiResponseFor422](#generate_otp.ApiResponseFor422) | Unprocessable Entity

#### generate_otp.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor201 |  |

# SchemaFor201ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**mfa_token** | str,  | str,  | Token can function as a temporary MFA token. It can be used to authenticate for any app when valid. | [optional] 
**reusable** | bool,  | BoolClass,  | true indcates the token can be used multiple times, until it expires. false indicates the token is invalid after a single use or once it expires. Defaults to false. | [optional] if omitted the server will use the default value of False
**expires_at** | str,  | str,  | Defines the expiration time and date for the token. Format is UTC time. | [optional] 
**device_id** | str,  | str,  | A unique identifier for the temp otp device that has been created for this token. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]
#### ResponseHeadersFor201

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Content-Type | ContentTypeSchema | | optional

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### generate_otp.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


#### generate_otp.ApiResponseFor422
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

# **get_auth_factors**
<a id="get_auth_factors"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_auth_factors(user_id)

Get User Factors

Get a user\\'s available authentication factors

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import multi_factor_authentication_api
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
    api_instance = multi_factor_authentication_api.MultiFactorAuthenticationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'user_id': 1,
    }
    try:
        # Get User Factors
        api_response = api_instance.get_auth_factors(
            path_params=path_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling MultiFactorAuthenticationApi->get_auth_factors: %s\n" % e)
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
user_id | UserIdSchema | | 

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_auth_factors.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#get_auth_factors.ApiResponseFor401) | Unauthorized

#### get_auth_factors.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**factor_id** | decimal.Decimal, int,  | decimal.Decimal,  | Identifier for the factor which will be used for user enrollment | [optional] 
**name** | str,  | str,  | Authentication factor name, as it appears to administrators in OneLogin. | [optional] 
**auth_factor_name** | str,  | str,  | Internal use only | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]
#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Content-Type | ContentTypeSchema | | optional

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### get_auth_factors.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_authentication_devices**
<a id="get_authentication_devices"></a>
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] get_authentication_devices(user_id)

Get User Devices

Get a user authentication devices

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import multi_factor_authentication_api
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
    api_instance = multi_factor_authentication_api.MultiFactorAuthenticationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'user_id': 1,
    }
    try:
        # Get User Devices
        api_response = api_instance.get_authentication_devices(
            path_params=path_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling MultiFactorAuthenticationApi->get_authentication_devices: %s\n" % e)
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
user_id | UserIdSchema | | 

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_authentication_devices.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#get_authentication_devices.ApiResponseFor401) | Unauthorized

#### get_authentication_devices.ApiResponseFor200
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
**device_id** | str,  | str,  | MFA device identifier. | [optional] 
**user_display_name** | str,  | str,  | Authentication factor display name assigned by users when they register the device. | [optional] 
**type_display_name** | str,  | str,  | Authentication factor display name as it appears to users upon initial registration, as defined by admins at Settings &gt; Authentication Factors. | [optional] 
**auth_factor_name** | str,  | str,  | Authentication factor name, as it appears to administrators in OneLogin. | [optional] 
**default** | bool,  | BoolClass,  | true &#x3D; is user’s default MFA device for OneLogin. | [optional] if omitted the server will use the default value of False
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_authentication_devices.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_user_registration**
<a id="get_user_registration"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_user_registration(user_idregistration_id)

Get User Registration

Get registration state by id

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import multi_factor_authentication_api
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
    api_instance = multi_factor_authentication_api.MultiFactorAuthenticationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'user_id': 1,
        'registration_id': "<UUID>",
    }
    try:
        # Get User Registration
        api_response = api_instance.get_user_registration(
            path_params=path_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling MultiFactorAuthenticationApi->get_user_registration: %s\n" % e)
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
user_id | UserIdSchema | | 
registration_id | RegistrationIdSchema | | 

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RegistrationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_user_registration.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#get_user_registration.ApiResponseFor401) | Unauthorized

#### get_user_registration.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Accept-Language | AcceptLanguageSchema | | optional
Cache-Control | CacheControlSchema | | optional
Content-Length | ContentLengthSchema | | optional
Content-Type | ContentTypeSchema | | optional
X-Content-Type-Options | XContentTypeOptionsSchema | | optional
X-Request-Id | XRequestIdSchema | | optional
Date | DateSchema | | optional

# AcceptLanguageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CacheControlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentLengthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XContentTypeOptionsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XRequestIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### get_user_registration.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_user_verification**
<a id="get_user_verification"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} get_user_verification(user_idverification_id)

Get User Verification

Get verification state by id

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import multi_factor_authentication_api
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
    api_instance = multi_factor_authentication_api.MultiFactorAuthenticationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'user_id': 1,
        'verification_id': "<UUID>",
    }
    try:
        # Get User Verification
        api_response = api_instance.get_user_verification(
            path_params=path_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling MultiFactorAuthenticationApi->get_user_verification: %s\n" % e)
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
user_id | UserIdSchema | | 
verification_id | VerificationIdSchema | | 

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VerificationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_user_verification.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#get_user_verification.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_user_verification.ApiResponseFor404) | Not Found

#### get_user_verification.ApiResponseFor200
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
**id** | str,  | str,  | registration identifier | [optional] 
**status** | str,  | str,  | pending &#x3D; has not been completed. accepted registration has successfully completed, rejected user has denied the MFA attempt or incorrectly provided the OneLogin Voice OTP code. | [optional] 
**device_id** | str,  | str,  | Device Id to be used with verify factor | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

#### get_user_verification.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


#### get_user_verification.ApiResponseFor404
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

# **verify_user_registration**
<a id="verify_user_registration"></a>
> {str: (bool, date, datetime, dict, float, int, list, str, none_type)} verify_user_registration(user_idregistration_id)

Verify User Registration

Submit an otp for verification.

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import multi_factor_authentication_api
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
    api_instance = multi_factor_authentication_api.MultiFactorAuthenticationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'user_id': 1,
        'registration_id': "<UUID>",
    }
    header_params = {
    }
    try:
        # Verify User Registration
        api_response = api_instance.verify_user_registration(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling MultiFactorAuthenticationApi->verify_user_registration: %s\n" % e)

    # example passing only optional values
    path_params = {
        'user_id': 1,
        'registration_id': "<UUID>",
    }
    header_params = {
        'Content-Type': "application/json",
    }
    body = dict(
        otp=1,
    )
    try:
        # Verify User Registration
        api_response = api_instance.verify_user_registration(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling MultiFactorAuthenticationApi->verify_user_registration: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
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
**otp** | decimal.Decimal, int,  | decimal.Decimal,  | One-Time-Password (OTP) that was sent to the user based on the chosen factor. OneLogin SMS and OneLogin Email support this OTP code. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Content-Type | ContentTypeSchema | | optional

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "application/json"

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
user_id | UserIdSchema | | 
registration_id | RegistrationIdSchema | | 

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# RegistrationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#verify_user_registration.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#verify_user_registration.ApiResponseFor401) | Unauthorized

#### verify_user_registration.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Registration identifier. | [optional] 
**status** | str,  | str,  | pending registration has not been completed successfully. accepted registration has successfully completed. | [optional] 
**device_id** | str,  | str,  | Device id to be used with Verify the Factor. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]
#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Accept-Language | AcceptLanguageSchema | | optional
Cache-Control | CacheControlSchema | | optional
Content-Length | ContentLengthSchema | | optional
Content-Type | ContentTypeSchema | | optional
X-Content-Type-Options | XContentTypeOptionsSchema | | optional
X-Request-Id | XRequestIdSchema | | optional
Date | DateSchema | | optional

# AcceptLanguageSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# CacheControlSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ContentLengthSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XContentTypeOptionsSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# XRequestIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# DateSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### verify_user_registration.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **verify_user_verification**
<a id="verify_user_verification"></a>
> Error verify_user_verification(user_idverification_id)

Verify User Verification

Submit an otp for verification.

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import multi_factor_authentication_api
from onelogin.model.error import Error
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
    api_instance = multi_factor_authentication_api.MultiFactorAuthenticationApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'user_id': 1,
        'verification_id': "<UUID>",
    }
    header_params = {
    }
    try:
        # Verify User Verification
        api_response = api_instance.verify_user_verification(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling MultiFactorAuthenticationApi->verify_user_verification: %s\n" % e)

    # example passing only optional values
    path_params = {
        'user_id': 1,
        'verification_id': "<UUID>",
    }
    header_params = {
        'Content-Type': "application/json",
    }
    body = dict(
        otp="123456",
        device_id=98765,
    )
    try:
        # Verify User Verification
        api_response = api_instance.verify_user_verification(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling MultiFactorAuthenticationApi->verify_user_verification: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
header_params | RequestHeaderParams | |
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
**otp** | str,  | str,  | OTP code provided by the device or SMS message sent to user. | [optional] 
**device_id** | decimal.Decimal, int,  | decimal.Decimal,  | ID of the specified device which has been registerd for the given user. Available on Get Devices API call. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### header_params
#### RequestHeaderParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Content-Type | ContentTypeSchema | | optional

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | if omitted the server will use the default value of "application/json"

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
user_id | UserIdSchema | | 
verification_id | VerificationIdSchema | | 

# UserIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

# VerificationIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#verify_user_verification.ApiResponseFor200) | OK
401 | [ApiResponseFor401](#verify_user_verification.ApiResponseFor401) | Unauthorized
403 | [ApiResponseFor403](#verify_user_verification.ApiResponseFor403) | Forbidden

#### verify_user_verification.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | ResponseHeadersFor200 |  |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Error**](../../models/Error.md) |  | 

#### ResponseHeadersFor200

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
Content-Type | ContentTypeSchema | | optional

# ContentTypeSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 


#### verify_user_verification.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


#### verify_user_verification.ApiResponseFor403
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor403ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor403ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

