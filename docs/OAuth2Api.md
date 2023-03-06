# onelogin.OAuth2Api

All URIs are relative to *https://your-api-subdomain.onelogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_token**](OAuth2Api.md#generate_token) | **POST** /auth/oauth2/v2/token | Generate Token
[**get_rate_limit**](OAuth2Api.md#get_rate_limit) | **GET** /auth/rate_limit | Get Rate Limit
[**revoke_tokens**](OAuth2Api.md#revoke_tokens) | **POST** /auth/oauth2/revoke | Revoke Tokens


# **generate_token**
> OauthToken generate_token(generate_token_request, content_type=content_type)

Generate Token

Generate Token

### Example

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
configuration = onelogin.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with onelogin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onelogin.OAuth2Api(api_client)
    generate_token_request = {"grant_type":"client_credentials"} # GenerateTokenRequest | Request Body to Generate OAuth Token
    content_type = 'application/json' # str |  (optional) (default to 'application/json')

    try:
        # Generate Token
        api_response = api_instance.generate_token(generate_token_request, content_type=content_type)
        print("The response of OAuth2Api->generate_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth2Api->generate_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_token_request** | [**GenerateTokenRequest**](GenerateTokenRequest.md)| Request Body to Generate OAuth Token | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]

### Return type

[**OauthToken**](OauthToken.md)

### Authorization

[basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rate_limit**
> GetRateLimit200Response get_rate_limit()

Get Rate Limit

Get Rate Limit

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
    api_instance = onelogin.OAuth2Api(api_client)

    try:
        # Get Rate Limit
        api_response = api_instance.get_rate_limit()
        print("The response of OAuth2Api->get_rate_limit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth2Api->get_rate_limit: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetRateLimit200Response**](GetRateLimit200Response.md)

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

# **revoke_tokens**
> Error revoke_tokens(content_type=content_type, revoke_tokens_request=revoke_tokens_request)

Revoke Tokens

Revoke Tokens

### Example

* Basic Authentication (basicAuth):
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

# Configure HTTP basic authorization: basicAuth
configuration = onelogin.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
with onelogin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onelogin.OAuth2Api(api_client)
    content_type = 'application/json' # str |  (optional) (default to 'application/json')
    revoke_tokens_request = onelogin.RevokeTokensRequest() # RevokeTokensRequest |  (optional)

    try:
        # Revoke Tokens
        api_response = api_instance.revoke_tokens(content_type=content_type, revoke_tokens_request=revoke_tokens_request)
        print("The response of OAuth2Api->revoke_tokens:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth2Api->revoke_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]
 **revoke_tokens_request** | [**RevokeTokensRequest**](RevokeTokensRequest.md)|  | [optional] 

### Return type

[**Error**](Error.md)

### Authorization

[basicAuth](../README.md#basicAuth)

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

