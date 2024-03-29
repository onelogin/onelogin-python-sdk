# onelogin.BrandingServiceApi

All URIs are relative to *https://your-api-subdomain.onelogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_brand**](BrandingServiceApi.md#create_brand) | **POST** /api/2/branding/brands | Create Brand
[**delete_brand**](BrandingServiceApi.md#delete_brand) | **DELETE** /api/2/branding/brands/{brand_id} | Delete Brand
[**get_brand**](BrandingServiceApi.md#get_brand) | **GET** /api/2/branding/brands/{brand_id} | Get Brand
[**get_brand_apps**](BrandingServiceApi.md#get_brand_apps) | **GET** /api/2/branding/brands/{brand_id}/apps | Get Brand Apps
[**list_brands**](BrandingServiceApi.md#list_brands) | **GET** /api/2/branding/brands | List Account Brands
[**update_brand**](BrandingServiceApi.md#update_brand) | **PUT** /api/2/branding/brands/{brand_id} | Update Brand


# **create_brand**
> Brand create_brand(brand=brand)

Create Brand

Create a new Account Brand

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
    api_instance = onelogin.BrandingServiceApi(api_client)
    brand = onelogin.Brand() # Brand |  (optional)

    try:
        # Create Brand
        api_response = api_instance.create_brand(brand=brand)
        print("The response of BrandingServiceApi->create_brand:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingServiceApi->create_brand: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand** | [**Brand**](Brand.md)|  | [optional] 

### Return type

[**Brand**](Brand.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_brand**
> delete_brand(brand_id)

Delete Brand

Delete Brand

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
    api_instance = onelogin.BrandingServiceApi(api_client)
    brand_id = 9 # int | Unique identifier for the branding object.

    try:
        # Delete Brand
        api_instance.delete_brand(brand_id)
    except Exception as e:
        print("Exception when calling BrandingServiceApi->delete_brand: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **int**| Unique identifier for the branding object. | 

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
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_brand**
> Brand get_brand(brand_id)

Get Brand

Retrieve a single brand via ID

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
    api_instance = onelogin.BrandingServiceApi(api_client)
    brand_id = 9 # int | Unique identifier for the branding object.

    try:
        # Get Brand
        api_response = api_instance.get_brand(brand_id)
        print("The response of BrandingServiceApi->get_brand:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingServiceApi->get_brand: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **int**| Unique identifier for the branding object. | 

### Return type

[**Brand**](Brand.md)

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

# **get_brand_apps**
> List[BrandApp] get_brand_apps(brand_id)

Get Brand Apps

Get Apps Associated with Account Brand

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
    api_instance = onelogin.BrandingServiceApi(api_client)
    brand_id = 9 # int | Unique identifier for the branding object.

    try:
        # Get Brand Apps
        api_response = api_instance.get_brand_apps(brand_id)
        print("The response of BrandingServiceApi->get_brand_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingServiceApi->get_brand_apps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **int**| Unique identifier for the branding object. | 

### Return type

[**List[BrandApp]**](BrandApp.md)

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

# **list_brands**
> List[BrandReq] list_brands()

List Account Brands

List Account Brands

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
    api_instance = onelogin.BrandingServiceApi(api_client)

    try:
        # List Account Brands
        api_response = api_instance.list_brands()
        print("The response of BrandingServiceApi->list_brands:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingServiceApi->list_brands: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**List[BrandReq]**](BrandReq.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_brand**
> Brand update_brand(brand_id, request_brand=request_brand)

Update Brand

Update Account Brand

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
    api_instance = onelogin.BrandingServiceApi(api_client)
    brand_id = 9 # int | Unique identifier for the branding object.
    request_brand = onelogin.RequestBrand() # RequestBrand |  (optional)

    try:
        # Update Brand
        api_response = api_instance.update_brand(brand_id, request_brand=request_brand)
        print("The response of BrandingServiceApi->update_brand:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BrandingServiceApi->update_brand: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **brand_id** | **int**| Unique identifier for the branding object. | 
 **request_brand** | [**RequestBrand**](RequestBrand.md)|  | [optional] 

### Return type

[**Brand**](Brand.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**401** | Unauthorized |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

