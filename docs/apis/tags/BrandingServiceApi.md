<a id="__pageTop"></a>
# onelogin.apis.tags.branding_service_api.BrandingServiceApi

All URIs are relative to *https://your-api-subdomain.onelogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_brand**](#create_brand) | **post** /api/2/branding/brands | Create Brand
[**delete_brand**](#delete_brand) | **delete** /api/2/branding/brands/{brand_id} | Delete Brand
[**get_brand**](#get_brand) | **get** /api/2/branding/brands/{brand_id} | Get Brand
[**get_brand_apps**](#get_brand_apps) | **get** /api/2/branding/brands/{brand_id}/apps | Get Brand Apps
[**list_brands**](#list_brands) | **get** /api/2/branding/brands | List Account Brands
[**update_brand**](#update_brand) | **put** /api/2/branding/brands/{brand_id} | Update Brand

# **create_brand**
<a id="create_brand"></a>
> Brand create_brand()

Create Brand

Create a new Account Brand

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import branding_service_api
from onelogin.model.brand import Brand
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
    api_instance = branding_service_api.BrandingServiceApi(api_client)

    # example passing only optional values
    body = Brand(
        id=1,
        enabled=True,
        custom_support_enabled=False,
        custom_color="#1298b4",
        custom_accent_color="#b60012",
        custom_masking_color="#beefed",
        custom_masking_opacity=40,
        mfa_enrollment_message="You must register with the OneLogin Protect app in order to login",
        enable_custom_label_for_login_screen=True,
        custom_label_text_for_login_screen="ACME Username or Email",
        login_instruction="To login, enter your ACME Username or Email. Reach out to help.desk@acme.org if you have trouble logging in.",
        login_instruction_title="ACME Login Instructions",
        hide_onelogin_footer=True,
        background=dict(
            urls=dict(
                original="original_example",
                login="login_example",
                branding="branding_example",
            ),
            file_size=1,
            updated_at="updated_at_example",
            content_type="content_type_example",
        ),
        logo=dict(
            urls=dict(
                original="original_example",
                login="login_example",
                navigation="navigation_example",
            ),
            file_size=1,
            updated_at="updated_at_example",
            content_type="content_type_example",
        ),
    )
    try:
        # Create Brand
        api_response = api_instance.create_brand(
            body=body,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling BrandingServiceApi->create_brand: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/json' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('application/json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Brand**](../../models/Brand.md) |  | 


### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
201 | [ApiResponseFor201](#create_brand.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#create_brand.ApiResponseFor401) | Unauthorized
422 | [ApiResponseFor422](#create_brand.ApiResponseFor422) | Unprocessable Entity

#### create_brand.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Brand**](../../models/Brand.md) |  | 


#### create_brand.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


#### create_brand.ApiResponseFor422
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

# **delete_brand**
<a id="delete_brand"></a>
> delete_brand(brand_id)

Delete Brand

Delete Brand

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import branding_service_api
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
    api_instance = branding_service_api.BrandingServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'brand_id': 9,
    }
    try:
        # Delete Brand
        api_response = api_instance.delete_brand(
            path_params=path_params,
        )
    except onelogin.ApiException as e:
        print("Exception when calling BrandingServiceApi->delete_brand: %s\n" % e)
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

# BrandIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
204 | [ApiResponseFor204](#delete_brand.ApiResponseFor204) | No Content
401 | [ApiResponseFor401](#delete_brand.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#delete_brand.ApiResponseFor404) | Not Found

#### delete_brand.ApiResponseFor204
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

#### delete_brand.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


#### delete_brand.ApiResponseFor404
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

# **get_brand**
<a id="get_brand"></a>
> Brand get_brand(brand_id)

Get Brand

Retrieve a single brand via ID

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import branding_service_api
from onelogin.model.brand import Brand
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
    api_instance = branding_service_api.BrandingServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'brand_id': 9,
    }
    try:
        # Get Brand
        api_response = api_instance.get_brand(
            path_params=path_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling BrandingServiceApi->get_brand: %s\n" % e)
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

# BrandIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_brand.ApiResponseFor200) | Successful response
401 | [ApiResponseFor401](#get_brand.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_brand.ApiResponseFor404) | Not Found

#### get_brand.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Brand**](../../models/Brand.md) |  | 


#### get_brand.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


#### get_brand.ApiResponseFor404
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

# **get_brand_apps**
<a id="get_brand_apps"></a>
> [BrandApp] get_brand_apps(brand_id)

Get Brand Apps

Get Apps Associated with Account Brand

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import branding_service_api
from onelogin.model.brand_app import BrandApp
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
    api_instance = branding_service_api.BrandingServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'brand_id': 9,
    }
    try:
        # Get Brand Apps
        api_response = api_instance.get_brand_apps(
            path_params=path_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling BrandingServiceApi->get_brand_apps: %s\n" % e)
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

# BrandIdSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
decimal.Decimal, int,  | decimal.Decimal,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_brand_apps.ApiResponseFor200) | Successful response
401 | [ApiResponseFor401](#get_brand_apps.ApiResponseFor401) | Unauthorized
404 | [ApiResponseFor404](#get_brand_apps.ApiResponseFor404) | Not Found

#### get_brand_apps.ApiResponseFor200
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
[**BrandApp**]({{complexTypePrefix}}BrandApp.md) | [**BrandApp**]({{complexTypePrefix}}BrandApp.md) | [**BrandApp**]({{complexTypePrefix}}BrandApp.md) |  | 

#### get_brand_apps.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


#### get_brand_apps.ApiResponseFor404
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

# **list_brands**
<a id="list_brands"></a>
> [BrandReq] list_brands()

List Account Brands

List Account Brands

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import branding_service_api
from onelogin.model.brand_req import BrandReq
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
    api_instance = branding_service_api.BrandingServiceApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # List Account Brands
        api_response = api_instance.list_brands()
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling BrandingServiceApi->list_brands: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#list_brands.ApiResponseFor200) | Successful response

#### list_brands.ApiResponseFor200
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
[**BrandReq**]({{complexTypePrefix}}BrandReq.md) | [**BrandReq**]({{complexTypePrefix}}BrandReq.md) | [**BrandReq**]({{complexTypePrefix}}BrandReq.md) |  | 

### Authorization

[OAuth2](../../../README.md#OAuth2)

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **update_brand**
<a id="update_brand"></a>
> Brand update_brand(brand_id)

Update Brand

Update Account Brand

### Example

* OAuth Authentication (OAuth2):
```python
import onelogin
from onelogin.apis.tags import branding_service_api
from onelogin.model.brand import Brand
from onelogin.model.alt_err import AltErr
from onelogin.model.request_brand import RequestBrand
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
    api_instance = branding_service_api.BrandingServiceApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'brand_id': 9,
    }
    try:
        # Update Brand
        api_response = api_instance.update_brand(
            path_params=path_params,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling BrandingServiceApi->update_brand: %s\n" % e)

    # example passing only optional values
    path_params = {
        'brand_id': 9,
    }
    body = RequestBrand(
        enabled=True,
        name="Acme Branding",
        custom_support_enabled=False,
        custom_color="#1298b4",
        custom_accent_color="#b60012",
        custom_masking_color="#beefed",
        custom_masking_opacity=40,
        enable_custom_label_for_login_screen=True,
        custom_label_text_for_login_screen="ACME Username or Email",
        login_instruction_title="ACME Login Instructions",
        login_instruction="To login, enter your ACME Username or Email. Reach out to help.desk@acme.org if you have trouble logging in.",
        hide_onelogin_footer=True,
        mfa_enrollment_message="You must register with the OneLogin Protect app in order to login",
        background="/9j/4AAQSkZJRgAB...J3a+IvMu7D8T/9k=",
        logo="iVBORw0KGgoAAAAN...AABJRU5ErkJggg==",
    )
    try:
        # Update Brand
        api_response = api_instance.update_brand(
            path_params=path_params,
            body=body,
        )
        pprint(api_response)
    except onelogin.ApiException as e:
        print("Exception when calling BrandingServiceApi->update_brand: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationJson, Unset] | optional, default is unset |
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
[**RequestBrand**](../../models/RequestBrand.md) |  | 


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
201 | [ApiResponseFor201](#update_brand.ApiResponseFor201) | Created
401 | [ApiResponseFor401](#update_brand.ApiResponseFor401) | Unauthorized
422 | [ApiResponseFor422](#update_brand.ApiResponseFor422) | Unprocessable Entity

#### update_brand.ApiResponseFor201
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor201ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor201ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**Brand**](../../models/Brand.md) |  | 


#### update_brand.ApiResponseFor401
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor401ResponseBodyApplicationJson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor401ResponseBodyApplicationJson
Type | Description  | Notes
------------- | ------------- | -------------
[**AltErr**](../../models/AltErr.md) |  | 


#### update_brand.ApiResponseFor422
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

