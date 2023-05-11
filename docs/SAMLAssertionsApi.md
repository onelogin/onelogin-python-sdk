
# onelogin.SAMLAssertionsApi

All URIs are relative to *https://your-api-subdomain.onelogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_saml_assert**](SAMLAssertionsApi.md#generate_saml_assert) | **POST** /api/1/saml_assertion | Generate SAML Assertion
[**generate_saml_assert2**](SAMLAssertionsApi.md#generate_saml_assert2) | **POST** /api/2/saml_assertion | Generate SAML Assertion
[**ver_factor_saml**](SAMLAssertionsApi.md#ver_factor_saml) | **POST** /api/1/saml_assertion/verify_factor | Verify Factor SAML
[**ver_factor_saml2**](SAMLAssertionsApi.md#ver_factor_saml2) | **POST** /api/2/saml_assertion/verify_factor | Verify Factor SAML


# **generate_saml_assert**
> GenerateSamlAssert200Response generate_saml_assert(content_type=content_type, saml_assert=saml_assert)

Generate SAML Assertion

Generate SAML Assertion

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
    api_instance = onelogin.SAMLAssertionsApi(api_client)
    content_type = 'application/json' # str |  (optional) (default to 'application/json')
    saml_assert = onelogin.SamlAssert() # SamlAssert |  (optional)

    try:
        # Generate SAML Assertion
        api_response = api_instance.generate_saml_assert(content_type=content_type, saml_assert=saml_assert)
        print("The response of SAMLAssertionsApi->generate_saml_assert:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SAMLAssertionsApi->generate_saml_assert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]
 **saml_assert** | [**SamlAssert**](SamlAssert.md)|  | [optional] 

### Return type

[**GenerateSamlAssert200Response**](GenerateSamlAssert200Response.md)

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

# **generate_saml_assert2**
> GenerateSamlAssert200Response generate_saml_assert2(content_type=content_type, saml_assert=saml_assert)

Generate SAML Assertion

Generate SAML Assertion

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
    api_instance = onelogin.SAMLAssertionsApi(api_client)
    content_type = 'application/json' # str |  (optional) (default to 'application/json')
    saml_assert = onelogin.SamlAssert() # SamlAssert |  (optional)

    try:
        # Generate SAML Assertion
        api_response = api_instance.generate_saml_assert2(content_type=content_type, saml_assert=saml_assert)
        print("The response of SAMLAssertionsApi->generate_saml_assert2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SAMLAssertionsApi->generate_saml_assert2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]
 **saml_assert** | [**SamlAssert**](SamlAssert.md)|  | [optional] 

### Return type

[**GenerateSamlAssert200Response**](GenerateSamlAssert200Response.md)

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

# **ver_factor_saml**
> VerFactorSaml200Response ver_factor_saml(content_type=content_type, saml_factor=saml_factor)

Verify Factor SAML

Verify Factor: SAML

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
    api_instance = onelogin.SAMLAssertionsApi(api_client)
    content_type = 'application/json' # str |  (optional) (default to 'application/json')
    saml_factor = onelogin.SamlFactor() # SamlFactor |  (optional)

    try:
        # Verify Factor SAML
        api_response = api_instance.ver_factor_saml(content_type=content_type, saml_factor=saml_factor)
        print("The response of SAMLAssertionsApi->ver_factor_saml:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SAMLAssertionsApi->ver_factor_saml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]
 **saml_factor** | [**SamlFactor**](SamlFactor.md)|  | [optional] 

### Return type

[**VerFactorSaml200Response**](VerFactorSaml200Response.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ver_factor_saml2**
> VerFactorSaml200Response ver_factor_saml2(content_type=content_type, saml_factor=saml_factor)

Verify Factor SAML

Verify Factor: SAML

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
    api_instance = onelogin.SAMLAssertionsApi(api_client)
    content_type = 'application/json' # str |  (optional) (default to 'application/json')
    saml_factor = onelogin.SamlFactor() # SamlFactor |  (optional)

    try:
        # Verify Factor SAML
        api_response = api_instance.ver_factor_saml2(content_type=content_type, saml_factor=saml_factor)
        print("The response of SAMLAssertionsApi->ver_factor_saml2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SAMLAssertionsApi->ver_factor_saml2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]
 **saml_factor** | [**SamlFactor**](SamlFactor.md)|  | [optional] 

### Return type

[**VerFactorSaml200Response**](VerFactorSaml200Response.md)

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
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

