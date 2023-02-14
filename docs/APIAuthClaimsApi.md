# openapi_client.APIAuthClaimsApi

All URIs are relative to *https://your-api-subdomain.onelogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_auth_claim**](APIAuthClaimsApi.md#create_auth_claim) | **POST** /api/2/api_authorizations/{api_auth_id}/claims | Create Api Auth Server Claim
[**delete_auth_claim**](APIAuthClaimsApi.md#delete_auth_claim) | **DELETE** /api/2/api_authorizations/{api_auth_id}/claims/{claim_id} | Delete Api Auth Server Claim
[**get_authclaims**](APIAuthClaimsApi.md#get_authclaims) | **GET** /api/2/api_authorizations/{api_auth_id}/claims | Get Api Auth Server claims
[**update_claim**](APIAuthClaimsApi.md#update_claim) | **PUT** /api/2/api_authorizations/{api_auth_id}/claims/{claim_id} | Update Api Auth Server Claim


# **create_auth_claim**
> int create_auth_claim(content_type, api_auth_id, create_auth_claim_request=create_auth_claim_request)

Create Api Auth Server Claim

Create Authorization Claim

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://your-api-subdomain.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://your-api-subdomain.onelogin.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.APIAuthClaimsApi(api_client)
    content_type = 'application/json' # str |  (default to 'application/json')
    api_auth_id = 'api_auth_id_example' # str | 
    create_auth_claim_request = openapi_client.CreateAuthClaimRequest() # CreateAuthClaimRequest |  (optional)

    try:
        # Create Api Auth Server Claim
        api_response = api_instance.create_auth_claim(content_type, api_auth_id, create_auth_claim_request=create_auth_claim_request)
        print("The response of APIAuthClaimsApi->create_auth_claim:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIAuthClaimsApi->create_auth_claim: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to &#39;application/json&#39;]
 **api_auth_id** | **str**|  | 
 **create_auth_claim_request** | [**CreateAuthClaimRequest**](CreateAuthClaimRequest.md)|  | [optional] 

### Return type

**int**

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_auth_claim**
> delete_auth_claim(api_auth_id, claim_id, content_type=content_type)

Delete Api Auth Server Claim

Delete Authorization Claim

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://your-api-subdomain.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://your-api-subdomain.onelogin.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.APIAuthClaimsApi(api_client)
    api_auth_id = 'api_auth_id_example' # str | 
    claim_id = 56 # int | 
    content_type = 'application/json' # str |  (optional) (default to 'application/json')

    try:
        # Delete Api Auth Server Claim
        api_instance.delete_auth_claim(api_auth_id, claim_id, content_type=content_type)
    except Exception as e:
        print("Exception when calling APIAuthClaimsApi->delete_auth_claim: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_auth_id** | **str**|  | 
 **claim_id** | **int**|  | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]

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
**204** | Success. The claim is deleted. No content is returned. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authclaims**
> List[GetAuthclaims200ResponseInner] get_authclaims(api_auth_id, content_type=content_type)

Get Api Auth Server claims

Get Authorization claims

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://your-api-subdomain.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://your-api-subdomain.onelogin.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.APIAuthClaimsApi(api_client)
    api_auth_id = 'api_auth_id_example' # str | 
    content_type = 'application/json' # str |  (optional) (default to 'application/json')

    try:
        # Get Api Auth Server claims
        api_response = api_instance.get_authclaims(api_auth_id, content_type=content_type)
        print("The response of APIAuthClaimsApi->get_authclaims:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIAuthClaimsApi->get_authclaims: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_auth_id** | **str**|  | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]

### Return type

[**List[GetAuthclaims200ResponseInner]**](GetAuthclaims200ResponseInner.md)

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

# **update_claim**
> CreateScope200Response update_claim(content_type, api_auth_id, claim_id, create_auth_claim_request=create_auth_claim_request)

Update Api Auth Server Claim

Update Authorization Server Claim

### Example

* OAuth Authentication (OAuth2):
```python
from __future__ import print_function
import time
import os
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://your-api-subdomain.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://your-api-subdomain.onelogin.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.APIAuthClaimsApi(api_client)
    content_type = 'application/json' # str |  (default to 'application/json')
    api_auth_id = 'api_auth_id_example' # str | 
    claim_id = 56 # int | 
    create_auth_claim_request = openapi_client.CreateAuthClaimRequest() # CreateAuthClaimRequest |  (optional)

    try:
        # Update Api Auth Server Claim
        api_response = api_instance.update_claim(content_type, api_auth_id, claim_id, create_auth_claim_request=create_auth_claim_request)
        print("The response of APIAuthClaimsApi->update_claim:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIAuthClaimsApi->update_claim: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [default to &#39;application/json&#39;]
 **api_auth_id** | **str**|  | 
 **claim_id** | **int**|  | 
 **create_auth_claim_request** | [**CreateAuthClaimRequest**](CreateAuthClaimRequest.md)|  | [optional] 

### Return type

[**CreateScope200Response**](CreateScope200Response.md)

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
**404** | Not Found |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

