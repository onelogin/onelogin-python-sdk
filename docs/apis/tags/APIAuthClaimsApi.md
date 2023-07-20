<a id="__pageTop"></a>
# onelogin.apis.tags.api_auth_claims_api.APIAuthClaimsApi

All URIs are relative to *https://your-api-subdomain.onelogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_auth_claim**](#create_auth_claim) | **post** /api/2/api_authorizations/{api_auth_id}/claims | Create Api Auth Server Claim
[**delete_auth_claim**](#delete_auth_claim) | **delete** /api/2/api_authorizations/{api_auth_id}/claims/{claim_id} | Delete Api Auth Server Claim
[**get_authclaims**](#get_authclaims) | **get** /api/2/api_authorizations/{api_auth_id}/claims | Get Api Auth Server claims
[**update_claim**](#update_claim) | **put** /api/2/api_authorizations/{api_auth_id}/claims/{claim_id} | Update Api Auth Server Claim

# **create_auth_claim**
<a id="create_auth_claim"></a>
> int create_auth_claim(api_auth_id)

Create Api Auth Server Claim

Create Authorization Claim

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import api_auth_claims_api
from onelogin.model.auth_claim import AuthClaim
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
    api_instance = api_auth_claims_api.APIAuthClaimsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'api_auth_id': "api_auth_id_example",
    }
    header_params = {
    }
    try:
        # Create Api Auth Server Claim
        api_response = api_instance.create_auth_claim(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling APIAuthClaimsApi->create_auth_claim: %s\n" % e)

    # example passing only optional values
    path_params = {
        'api_auth_id': "api_auth_id_example",
    }
    header_params = {
        'Content-Type': "application/json",
    }
    body = AuthClaim(
        name="email_address",
        user_attribute_mappings="email",
        user_attribute_macros="user_attribute_macros_example",
    )
    try:
        # Create Api Auth Server Claim
        api_response = api_instance.create_auth_claim(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling APIAuthClaimsApi->create_auth_claim: %s\n" % e)
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
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthClaim**](../../models/AuthClaim.md) |  | 


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
api_auth_id | ApiAuthIdSchema | | 

# ApiAuthIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#create_auth_claim.ApiResponseFor200) | Successful response
401 | [ApiResponseFor401](#create_auth_claim.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#create_auth_claim.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#create_auth_claim.ApiResponseFor422) | Unprocessable Entity

#### create_auth_claim.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

#### create_auth_claim.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


#### create_auth_claim.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


#### create_auth_claim.ApiResponseFor422
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

# **delete_auth_claim**
<a id="delete_auth_claim"></a>
> delete_auth_claim(api_auth_idclaim_id)

Delete Api Auth Server Claim

Delete Authorization Claim

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import api_auth_claims_api
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
    api_instance = api_auth_claims_api.APIAuthClaimsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'api_auth_id': "api_auth_id_example",
        'claim_id': 1,
    }
    header_params = {
    }
    try:
        # Delete Api Auth Server Claim
        api_response = api_instance.delete_auth_claim(
            path_params=path_params,
            header_params=header_params,
        )
    except onelogin.ApiException as e:
        print("Exception when calling APIAuthClaimsApi->delete_auth_claim: %s\n" % e)

    # example passing only optional values
    path_params = {
        'api_auth_id': "api_auth_id_example",
        'claim_id': 1,
    }
    header_params = {
        'Content-Type': "application/json",
    }
    try:
        # Delete Api Auth Server Claim
        api_response = api_instance.delete_auth_claim(
            path_params=path_params,
            header_params=header_params,
        )
    except onelogin.ApiException as e:
        print("Exception when calling APIAuthClaimsApi->delete_auth_claim: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

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
api_auth_id | ApiAuthIdSchema | | 
claim_id | ClaimIdSchema | | 

# ApiAuthIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ClaimIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_auth_claim.ApiResponseFor204) | Success. The claim is deleted. No content is returned.
401 | [ApiResponseFor401](#delete_auth_claim.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#delete_auth_claim.ApiResponseFor404) | Not Found

#### delete_auth_claim.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_auth_claim.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


#### delete_auth_claim.ApiResponseFor404
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

# **get_authclaims**
<a id="get_authclaims"></a>
> [TokenClaim] get_authclaims(api_auth_id)

Get Api Auth Server claims

Get Authorization claims

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import api_auth_claims_api
from onelogin.model.token_claim import TokenClaim
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
    api_instance = api_auth_claims_api.APIAuthClaimsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'api_auth_id': "api_auth_id_example",
    }
    header_params = {
    }
    try:
        # Get Api Auth Server claims
        api_response = api_instance.get_authclaims(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling APIAuthClaimsApi->get_authclaims: %s\n" % e)

    # example passing only optional values
    path_params = {
        'api_auth_id': "api_auth_id_example",
    }
    header_params = {
        'Content-Type': "application/json",
    }
    try:
        # Get Api Auth Server claims
        api_response = api_instance.get_authclaims(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling APIAuthClaimsApi->get_authclaims: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
header_params | RequestHeaderParams | |
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

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
api_auth_id | ApiAuthIdSchema | | 

# ApiAuthIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_authclaims.ApiResponseFor200) | Successful response
401 | [ApiResponseFor401](#get_authclaims.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_authclaims.ApiResponseFor404) | Not Found

#### get_authclaims.ApiResponseFor200
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
[**TokenClaim**]({{complexTypePrefix}}TokenClaim.md) | [**TokenClaim**]({{complexTypePrefix}}TokenClaim.md) | [**TokenClaim**]({{complexTypePrefix}}TokenClaim.md) |  | 

#### get_authclaims.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


#### get_authclaims.ApiResponseFor404
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

# **update_claim**
<a id="update_claim"></a>
> AuthId update_claim(api_auth_idclaim_id)

Update Api Auth Server Claim

Update Authorization Server Claim

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import api_auth_claims_api
from onelogin.model.auth_claim import AuthClaim
from onelogin.model.auth_id import AuthId
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
    api_instance = api_auth_claims_api.APIAuthClaimsApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'api_auth_id': "api_auth_id_example",
        'claim_id': 1,
    }
    header_params = {
    }
    try:
        # Update Api Auth Server Claim
        api_response = api_instance.update_claim(
            path_params=path_params,
            header_params=header_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling APIAuthClaimsApi->update_claim: %s\n" % e)

    # example passing only optional values
    path_params = {
        'api_auth_id': "api_auth_id_example",
        'claim_id': 1,
    }
    header_params = {
        'Content-Type': "application/json",
    }
    body = AuthClaim(
        name="email_address",
        user_attribute_mappings="email",
        user_attribute_macros="user_attribute_macros_example",
    )
    try:
        # Update Api Auth Server Claim
        api_response = api_instance.update_claim(
            path_params=path_params,
            header_params=header_params,
            body=body,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling APIAuthClaimsApi->update_claim: %s\n" % e)
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
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthClaim**](../../models/AuthClaim.md) |  | 


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
api_auth_id | ApiAuthIdSchema | | 
claim_id | ClaimIdSchema | | 

# ApiAuthIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

# ClaimIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#update_claim.ApiResponseFor200) | Successful response
401 | [ApiResponseFor401](#update_claim.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#update_claim.ApiResponseFor404) | Not Found
422 | [ApiResponseFor422](#update_claim.ApiResponseFor422) | Unprocessable Entity

#### update_claim.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AuthId**](../../models/AuthId.md) |  | 


#### update_claim.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


#### update_claim.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor404ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor404ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


#### update_claim.ApiResponseFor422
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

