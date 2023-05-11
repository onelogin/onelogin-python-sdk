# onelogin.RolesApi

All URIs are relative to *https://your-api-subdomain.onelogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_role_admins**](RolesApi.md#add_role_admins) | **POST** /api/2/roles/{role_id}/admins | Add Role Admins
[**add_role_users**](RolesApi.md#add_role_users) | **POST** /api/2/roles/{role_id}/users | Add Role Users
[**create_role**](RolesApi.md#create_role) | **POST** /api/2/roles | Create Role
[**delete_role**](RolesApi.md#delete_role) | **DELETE** /api/2/roles/{role_id} | Delete Role by ID
[**get_role**](RolesApi.md#get_role) | **GET** /api/2/roles/{role_id} | Get Role by ID
[**get_role_admins**](RolesApi.md#get_role_admins) | **GET** /api/2/roles/{role_id}/admins | Get Role Admins
[**get_role_apps**](RolesApi.md#get_role_apps) | **GET** /api/2/roles/{role_id}/apps | Get all Apps assigned to Role
[**get_role_by_id**](RolesApi.md#get_role_by_id) | **GET** /api/1/roles/{role_id} | Get Role by ID
[**get_role_by_name**](RolesApi.md#get_role_by_name) | **GET** /api/1/roles | Get Role by Name
[**get_role_users**](RolesApi.md#get_role_users) | **GET** /api/2/roles/{role_id}/users | Get Role Users
[**list_roles**](RolesApi.md#list_roles) | **GET** /api/2/roles | List Roles
[**remove_role_admins**](RolesApi.md#remove_role_admins) | **DELETE** /api/2/roles/{role_id}/admins | Remove Role Admins
[**remove_role_users**](RolesApi.md#remove_role_users) | **DELETE** /api/2/roles/{role_id}/users | Remove Role Users
[**set_role_apps**](RolesApi.md#set_role_apps) | **PUT** /api/2/roles/{role_id}/apps | Set Role Apps
[**update_role**](RolesApi.md#update_role) | **PUT** /api/2/roles/{role_id} | Update Role


# **add_role_admins**
> List[CreateRole201ResponseInner] add_role_admins(role_id, request_body)

Add Role Admins

Add Role Admins

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
    api_instance = onelogin.RolesApi(api_client)
    role_id = 'role_id_example' # str | Set to the id of the role you want to return.
    request_body = [56] # List[int] | 

    try:
        # Add Role Admins
        api_response = api_instance.add_role_admins(role_id, request_body)
        print("The response of RolesApi->add_role_admins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->add_role_admins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| Set to the id of the role you want to return. | 
 **request_body** | [**List[int]**](int.md)|  | 

### Return type

[**List[CreateRole201ResponseInner]**](CreateRole201ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_role_users**
> List[CreateRole201ResponseInner] add_role_users(role_id, request_body)

Add Role Users

Add Role Users

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
    api_instance = onelogin.RolesApi(api_client)
    role_id = 'role_id_example' # str | Set to the id of the role you want to return.
    request_body = [56] # List[int] | 

    try:
        # Add Role Users
        api_response = api_instance.add_role_users(role_id, request_body)
        print("The response of RolesApi->add_role_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->add_role_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| Set to the id of the role you want to return. | 
 **request_body** | [**List[int]**](int.md)|  | 

### Return type

[**List[CreateRole201ResponseInner]**](CreateRole201ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_role**
> List[CreateRole201ResponseInner] create_role(role=role)

Create Role

Create Role

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
    api_instance = onelogin.RolesApi(api_client)
    role = onelogin.Role() # Role |  (optional)

    try:
        # Create Role
        api_response = api_instance.create_role(role=role)
        print("The response of RolesApi->create_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->create_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role** | [**Role**](Role.md)|  | [optional] 

### Return type

[**List[CreateRole201ResponseInner]**](CreateRole201ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CREATED |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role**
> delete_role(role_id)

Delete Role by ID

Delete Role

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
    api_instance = onelogin.RolesApi(api_client)
    role_id = 'role_id_example' # str | Set to the id of the role you want to return.

    try:
        # Delete Role by ID
        api_instance.delete_role(role_id)
    except Exception as e:
        print("Exception when calling RolesApi->delete_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| Set to the id of the role you want to return. | 

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
**204** | NO CONTENT |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**
> Role get_role(role_id)

Get Role by ID

Get Role

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
    api_instance = onelogin.RolesApi(api_client)
    role_id = 'role_id_example' # str | Set to the id of the role you want to return.

    try:
        # Get Role by ID
        api_response = api_instance.get_role(role_id)
        print("The response of RolesApi->get_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->get_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| Set to the id of the role you want to return. | 

### Return type

[**Role**](Role.md)

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

# **get_role_admins**
> List[User] get_role_admins(role_id, limit=limit, page=page, cursor=cursor, name=name, include_unassigned=include_unassigned)

Get Role Admins

Get Role Admins

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
    api_instance = onelogin.RolesApi(api_client)
    role_id = 'role_id_example' # str | Set to the id of the role you want to return.
    limit = 56 # int | How many items to return at one time (max 100) (optional)
    page = 56 # int | The page number of results to return. (optional)
    cursor = 'cursor_example' # str | Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. (optional)
    name = 'name_example' # str | Allows you to filter on first name, last name, username, and email address. (optional)
    include_unassigned = True # bool | Optional. Defaults to false. Include users that aren’t assigned to the role. (optional)

    try:
        # Get Role Admins
        api_response = api_instance.get_role_admins(role_id, limit=limit, page=page, cursor=cursor, name=name, include_unassigned=include_unassigned)
        print("The response of RolesApi->get_role_admins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->get_role_admins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| Set to the id of the role you want to return. | 
 **limit** | **int**| How many items to return at one time (max 100) | [optional] 
 **page** | **int**| The page number of results to return. | [optional] 
 **cursor** | **str**| Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. | [optional] 
 **name** | **str**| Allows you to filter on first name, last name, username, and email address. | [optional] 
 **include_unassigned** | **bool**| Optional. Defaults to false. Include users that aren’t assigned to the role. | [optional] 

### Return type

[**List[User]**](User.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: applcation/json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Current-Page -  <br>  * Page-Items -  <br>  * Total-Count -  <br>  * Total-Pages -  <br>  * Link -  <br>  * Before-Cursor -  <br>  * After-Cursor -  <br>  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_apps**
> List[GetRoleApps200ResponseInner] get_role_apps(role_id, limit=limit, page=page, cursor=cursor, assigned=assigned)

Get all Apps assigned to Role

Get Role Apps

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
    api_instance = onelogin.RolesApi(api_client)
    role_id = 'role_id_example' # str | Set to the id of the role you want to return.
    limit = 56 # int | How many items to return at one time (max 100) (optional)
    page = 56 # int | The page number of results to return. (optional)
    cursor = 'cursor_example' # str | Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. (optional)
    assigned = True # bool | Optional. Defaults to true. Returns all apps not yet assigned to the role. (optional)

    try:
        # Get all Apps assigned to Role
        api_response = api_instance.get_role_apps(role_id, limit=limit, page=page, cursor=cursor, assigned=assigned)
        print("The response of RolesApi->get_role_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->get_role_apps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| Set to the id of the role you want to return. | 
 **limit** | **int**| How many items to return at one time (max 100) | [optional] 
 **page** | **int**| The page number of results to return. | [optional] 
 **cursor** | **str**| Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. | [optional] 
 **assigned** | **bool**| Optional. Defaults to true. Returns all apps not yet assigned to the role. | [optional] 

### Return type

[**List[GetRoleApps200ResponseInner]**](GetRoleApps200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: applcation/json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Current-Page -  <br>  * Page-Items -  <br>  * Total-Count -  <br>  * Total-Pages -  <br>  * Link -  <br>  * Before-Cursor -  <br>  * After-Cursor -  <br>  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_by_id**
> GetRoleById200Response get_role_by_id(role_id)

Get Role by ID

Get Role By ID

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
    api_instance = onelogin.RolesApi(api_client)
    role_id = 'role_id_example' # str | Set to the id of the role you want to return.

    try:
        # Get Role by ID
        api_response = api_instance.get_role_by_id(role_id)
        print("The response of RolesApi->get_role_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->get_role_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| Set to the id of the role you want to return. | 

### Return type

[**GetRoleById200Response**](GetRoleById200Response.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_by_name**
> GetRoleByName200Response get_role_by_name(name=name)

Get Role by Name

Get Role by Name

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
    api_instance = onelogin.RolesApi(api_client)
    name = 'name_example' # str |  (optional)

    try:
        # Get Role by Name
        api_response = api_instance.get_role_by_name(name=name)
        print("The response of RolesApi->get_role_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->get_role_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 

### Return type

[**GetRoleByName200Response**](GetRoleByName200Response.md)

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

# **get_role_users**
> List[User] get_role_users(role_id, limit=limit, page=page, cursor=cursor, name=name, include_unassigned=include_unassigned)

Get Role Users

Get Role Users

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
    api_instance = onelogin.RolesApi(api_client)
    role_id = 'role_id_example' # str | Set to the id of the role you want to return.
    limit = 56 # int | How many items to return at one time (max 100) (optional)
    page = 56 # int | The page number of results to return. (optional)
    cursor = 'cursor_example' # str | Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. (optional)
    name = 'name_example' # str | Allows you to filter on first name, last name, username, and email address. (optional)
    include_unassigned = True # bool | Optional. Defaults to false. Include users that aren’t assigned to the role. (optional)

    try:
        # Get Role Users
        api_response = api_instance.get_role_users(role_id, limit=limit, page=page, cursor=cursor, name=name, include_unassigned=include_unassigned)
        print("The response of RolesApi->get_role_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->get_role_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| Set to the id of the role you want to return. | 
 **limit** | **int**| How many items to return at one time (max 100) | [optional] 
 **page** | **int**| The page number of results to return. | [optional] 
 **cursor** | **str**| Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. | [optional] 
 **name** | **str**| Allows you to filter on first name, last name, username, and email address. | [optional] 
 **include_unassigned** | **bool**| Optional. Defaults to false. Include users that aren’t assigned to the role. | [optional] 

### Return type

[**List[User]**](User.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: applcation/json, application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Current-Page -  <br>  * Page-Items -  <br>  * Total-Count -  <br>  * Total-Pages -  <br>  * Link -  <br>  * Before-Cursor -  <br>  * After-Cursor -  <br>  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_roles**
> List[Role] list_roles(limit=limit, page=page, cursor=cursor, role_name=role_name, app_id=app_id, app_name=app_name, fields=fields)

List Roles

List Roles

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
    api_instance = onelogin.RolesApi(api_client)
    limit = 56 # int | How many items to return at one time (max 100) (optional)
    page = 56 # int | The page number of results to return. (optional)
    cursor = 'cursor_example' # str | Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. (optional)
    role_name = 'role_name_example' # str | Optional. Filters by role name. (optional)
    app_id = 56 # int |  (optional)
    app_name = 'app_name_example' # str | Optional. Returns roles that contain this app name. (optional)
    fields = 'fields_example' # str | Optional. Comma delimited list of fields to return. (optional)

    try:
        # List Roles
        api_response = api_instance.list_roles(limit=limit, page=page, cursor=cursor, role_name=role_name, app_id=app_id, app_name=app_name, fields=fields)
        print("The response of RolesApi->list_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->list_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many items to return at one time (max 100) | [optional] 
 **page** | **int**| The page number of results to return. | [optional] 
 **cursor** | **str**| Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. | [optional] 
 **role_name** | **str**| Optional. Filters by role name. | [optional] 
 **app_id** | **int**|  | [optional] 
 **app_name** | **str**| Optional. Returns roles that contain this app name. | [optional] 
 **fields** | **str**| Optional. Comma delimited list of fields to return. | [optional] 

### Return type

[**List[Role]**](Role.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Current-Page -  <br>  * Page-Items -  <br>  * Total-Count -  <br>  * Total-Pages -  <br>  * Link -  <br>  * Before-Cursor -  <br>  * After-Cursor -  <br>  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_role_admins**
> remove_role_admins(role_id, remove_role_users_request)

Remove Role Admins

Remove Role Admins

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
    api_instance = onelogin.RolesApi(api_client)
    role_id = 'role_id_example' # str | Set to the id of the role you want to return.
    remove_role_users_request = onelogin.RemoveRoleUsersRequest() # RemoveRoleUsersRequest | 

    try:
        # Remove Role Admins
        api_instance.remove_role_admins(role_id, remove_role_users_request)
    except Exception as e:
        print("Exception when calling RolesApi->remove_role_admins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| Set to the id of the role you want to return. | 
 **remove_role_users_request** | [**RemoveRoleUsersRequest**](RemoveRoleUsersRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | NO CONTENT |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_role_users**
> remove_role_users(role_id, remove_role_users_request)

Remove Role Users

Remove Role Users

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
    api_instance = onelogin.RolesApi(api_client)
    role_id = 'role_id_example' # str | Set to the id of the role you want to return.
    remove_role_users_request = onelogin.RemoveRoleUsersRequest() # RemoveRoleUsersRequest | 

    try:
        # Remove Role Users
        api_instance.remove_role_users(role_id, remove_role_users_request)
    except Exception as e:
        print("Exception when calling RolesApi->remove_role_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| Set to the id of the role you want to return. | 
 **remove_role_users_request** | [**RemoveRoleUsersRequest**](RemoveRoleUsersRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | NO CONTENT |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_role_apps**
> List[CreateRole201ResponseInner] set_role_apps(role_id, request_body)

Set Role Apps

Set Role Apps

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
    api_instance = onelogin.RolesApi(api_client)
    role_id = 'role_id_example' # str | Set to the id of the role you want to return.
    request_body = [56] # List[int] | 

    try:
        # Set Role Apps
        api_response = api_instance.set_role_apps(role_id, request_body)
        print("The response of RolesApi->set_role_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->set_role_apps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| Set to the id of the role you want to return. | 
 **request_body** | [**List[int]**](int.md)|  | 

### Return type

[**List[CreateRole201ResponseInner]**](CreateRole201ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response returns an array of app IDs sent in the request. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> UpdateRole200Response update_role(role_id, role=role)

Update Role

Update Role

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
    api_instance = onelogin.RolesApi(api_client)
    role_id = 'role_id_example' # str | Set to the id of the role you want to return.
    role = onelogin.Role() # Role |  (optional)

    try:
        # Update Role
        api_response = api_instance.update_role(role_id, role=role)
        print("The response of RolesApi->update_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RolesApi->update_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_id** | **str**| Set to the id of the role you want to return. | 
 **role** | [**Role**](Role.md)|  | [optional] 

### Return type

[**UpdateRole200Response**](UpdateRole200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |
**422** | Unprocessable Entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

