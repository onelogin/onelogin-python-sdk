# onelogin.UsersV1Api

All URIs are relative to *https://your-api-subdomain.onelogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_roles_to_user**](UsersV1Api.md#add_roles_to_user) | **PUT** /api/1/users/{user_id}/add_roles | Add Roles for a User
[**create_user**](UsersV1Api.md#create_user) | **POST** /api/1/users | Create a User
[**delete_user**](UsersV1Api.md#delete_user) | **DELETE** /api/1/users/{user_id} | Delete a User
[**get_custom_attributes**](UsersV1Api.md#get_custom_attributes) | **GET** /api/1/users/custom_attributes | Get Custom Attributes
[**get_user_apps**](UsersV1Api.md#get_user_apps) | **GET** /api/1/users/{user_id}/apps | Get Apps for a User
[**get_user_by_id**](UsersV1Api.md#get_user_by_id) | **GET** /api/1/users/{user_id} | Get User by ID
[**get_user_roles**](UsersV1Api.md#get_user_roles) | **GET** /api/1/users/{user_id}/roles | Get Roles for a User
[**list_users**](UsersV1Api.md#list_users) | **GET** /api/1/users | List Users
[**lock_account_user**](UsersV1Api.md#lock_account_user) | **PUT** /api/1/users/{user_id}/lock_user | Lock User Account
[**log_out_user**](UsersV1Api.md#log_out_user) | **PUT** /api/1/users/{user_id}/logout | Log User Out
[**remove_user_role**](UsersV1Api.md#remove_user_role) | **PUT** /api/1/users/{user_id}/remove_roles | Remove Roles for a User
[**set_user_state**](UsersV1Api.md#set_user_state) | **PUT** /api/1/users/{user_id}/set_state | Set User State
[**update_password_insecure**](UsersV1Api.md#update_password_insecure) | **PUT** /api/1/users/set_password_clear_text/{user_id} | Set Password Using ID in Cleartext
[**update_password_secure**](UsersV1Api.md#update_password_secure) | **PUT** /api/1/users/set_password_using_salt/{user_id} | Set Password Using ID and SHA-256 and Salt
[**update_user**](UsersV1Api.md#update_user) | **PUT** /api/1/users/{user_id} | Update a User


# **add_roles_to_user**
> GenerateToken400Response add_roles_to_user(user_id, content_type=content_type, add_roles_to_user_request=add_roles_to_user_request)

Add Roles for a User

Add Roles for a User

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
    api_instance = onelogin.UsersV1Api(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.
    content_type = 'application/json' # str |  (optional) (default to 'application/json')
    add_roles_to_user_request = onelogin.AddRolesToUserRequest() # AddRolesToUserRequest |  (optional)

    try:
        # Add Roles for a User
        api_response = api_instance.add_roles_to_user(user_id, content_type=content_type, add_roles_to_user_request=add_roles_to_user_request)
        print("The response of UsersV1Api->add_roles_to_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->add_roles_to_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Set to the id of the user that you want to return. | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]
 **add_roles_to_user_request** | [**AddRolesToUserRequest**](AddRolesToUserRequest.md)|  | [optional] 

### Return type

[**GenerateToken400Response**](GenerateToken400Response.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> ListUsers200ResponseInner create_user(list_users200_response_inner, mappings=mappings, validate_policy=validate_policy)

Create a User

Create a User

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
    api_instance = onelogin.UsersV1Api(api_client)
    list_users200_response_inner = onelogin.ListUsers200ResponseInner() # ListUsers200ResponseInner | 
    mappings = 'mappings_example' # str | Controls how mappings will be applied to the user on creation. Defaults to async. (optional)
    validate_policy = True # bool | Will passwords validate against the User Policy? Defaults to true. (optional)

    try:
        # Create a User
        api_response = api_instance.create_user(list_users200_response_inner, mappings=mappings, validate_policy=validate_policy)
        print("The response of UsersV1Api->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list_users200_response_inner** | [**ListUsers200ResponseInner**](ListUsers200ResponseInner.md)|  | 
 **mappings** | **str**| Controls how mappings will be applied to the user on creation. Defaults to async. | [optional] 
 **validate_policy** | **bool**| Will passwords validate against the User Policy? Defaults to true. | [optional] 

### Return type

[**ListUsers200ResponseInner**](ListUsers200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The full user resource is returned |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**422** | Unprocessable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(user_id)

Delete a User

Delete A User

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
    api_instance = onelogin.UsersV1Api(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.

    try:
        # Delete a User
        api_instance.delete_user(user_id)
    except Exception as e:
        print("Exception when calling UsersV1Api->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Set to the id of the user that you want to return. | 

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
**204** | On success, no content is returned in the response body. |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_attributes**
> GetCustomAttributes200Response get_custom_attributes()

Get Custom Attributes

Get Custom Attributes

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
    api_instance = onelogin.UsersV1Api(api_client)

    try:
        # Get Custom Attributes
        api_response = api_instance.get_custom_attributes()
        print("The response of UsersV1Api->get_custom_attributes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->get_custom_attributes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetCustomAttributes200Response**](GetCustomAttributes200Response.md)

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

# **get_user_apps**
> List[GetUserApps200ResponseInner] get_user_apps(user_id, ignore_visibility=ignore_visibility)

Get Apps for a User

Get Apps for User

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
    api_instance = onelogin.UsersV1Api(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.
    ignore_visibility = False # bool | Defaults to `false`. When `true` will show all apps that are assigned to a user regardless of their portal visibility setting. (optional) (default to False)

    try:
        # Get Apps for a User
        api_response = api_instance.get_user_apps(user_id, ignore_visibility=ignore_visibility)
        print("The response of UsersV1Api->get_user_apps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->get_user_apps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Set to the id of the user that you want to return. | 
 **ignore_visibility** | **bool**| Defaults to &#x60;false&#x60;. When &#x60;true&#x60; will show all apps that are assigned to a user regardless of their portal visibility setting. | [optional] [default to False]

### Return type

[**List[GetUserApps200ResponseInner]**](GetUserApps200ResponseInner.md)

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

# **get_user_by_id**
> ListUsers200ResponseInner get_user_by_id(user_id)

Get User by ID

Get User By ID

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
    api_instance = onelogin.UsersV1Api(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.

    try:
        # Get User by ID
        api_response = api_instance.get_user_by_id(user_id)
        print("The response of UsersV1Api->get_user_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->get_user_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Set to the id of the user that you want to return. | 

### Return type

[**ListUsers200ResponseInner**](ListUsers200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_roles**
> GetUserRoles200Response get_user_roles(user_id)

Get Roles for a User

Get User Roles

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
    api_instance = onelogin.UsersV1Api(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.

    try:
        # Get Roles for a User
        api_response = api_instance.get_user_roles(user_id)
        print("The response of UsersV1Api->get_user_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->get_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Set to the id of the user that you want to return. | 

### Return type

[**GetUserRoles200Response**](GetUserRoles200Response.md)

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

# **list_users**
> List[ListUsers200ResponseInner] list_users(limit=limit, page=page, cursor=cursor, created_since=created_since, created_until=created_until, updated_since=updated_since, updated_until=updated_until, last_login_since=last_login_since, last_login_until=last_login_until, firstname=firstname, lastname=lastname, email=email, username=username, samaccountname=samaccountname, directory_id=directory_id, external_id=external_id, user_ids=user_ids, custom_attributes_attribute_name=custom_attributes_attribute_name, fields=fields)

List Users

List Users

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
    api_instance = onelogin.UsersV1Api(api_client)
    limit = 56 # int | How many items to return at one time (max 100) (optional)
    page = 56 # int | The page number of results to return. (optional)
    cursor = 'cursor_example' # str | Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. (optional)
    created_since = 'created_since_example' # str | An ISO8601 timestamp value that returns all users created after a given date & time. (optional)
    created_until = 'created_until_example' # str | An ISO8601 timestamp value that returns all users created before a given date & time. (optional)
    updated_since = 'updated_since_example' # str | An ISO8601 timestamp value that returns all users updated after a given date & time. (optional)
    updated_until = 'updated_until_example' # str | An ISO8601 timestamp value that returns all users updated before a given date & time. (optional)
    last_login_since = 'last_login_since_example' # str | An ISO8601 timestamp value that returns all users that logged in after a given date & time. (optional)
    last_login_until = 'last_login_until_example' # str | An ISO8601 timestamp value that returns all users that logged in before a given date & time. (optional)
    firstname = 'firstname_example' # str | The first name of the user (optional)
    lastname = 'lastname_example' # str | The last name of the user (optional)
    email = 'email_example' # str | The email address of the user (optional)
    username = 'username_example' # str | The username for the user (optional)
    samaccountname = 'samaccountname_example' # str | The AD login name for the user (optional)
    directory_id = 56 # int |  (optional)
    external_id = 'external_id_example' # str | An external identifier that has been set on the user (optional)
    user_ids = 'user_ids_example' # str | A comma separated list of OneLogin User IDs (optional)
    custom_attributes_attribute_name = 'custom_attributes_attribute_name_example' # str | The short name of a custom attribute. Note that the attribute name is prefixed with custom_attributes. (optional)
    fields = 'fields_example' # str | A comma separated list user attributes to return. (optional)

    try:
        # List Users
        api_response = api_instance.list_users(limit=limit, page=page, cursor=cursor, created_since=created_since, created_until=created_until, updated_since=updated_since, updated_until=updated_until, last_login_since=last_login_since, last_login_until=last_login_until, firstname=firstname, lastname=lastname, email=email, username=username, samaccountname=samaccountname, directory_id=directory_id, external_id=external_id, user_ids=user_ids, custom_attributes_attribute_name=custom_attributes_attribute_name, fields=fields)
        print("The response of UsersV1Api->list_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->list_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many items to return at one time (max 100) | [optional] 
 **page** | **int**| The page number of results to return. | [optional] 
 **cursor** | **str**| Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. | [optional] 
 **created_since** | **str**| An ISO8601 timestamp value that returns all users created after a given date &amp; time. | [optional] 
 **created_until** | **str**| An ISO8601 timestamp value that returns all users created before a given date &amp; time. | [optional] 
 **updated_since** | **str**| An ISO8601 timestamp value that returns all users updated after a given date &amp; time. | [optional] 
 **updated_until** | **str**| An ISO8601 timestamp value that returns all users updated before a given date &amp; time. | [optional] 
 **last_login_since** | **str**| An ISO8601 timestamp value that returns all users that logged in after a given date &amp; time. | [optional] 
 **last_login_until** | **str**| An ISO8601 timestamp value that returns all users that logged in before a given date &amp; time. | [optional] 
 **firstname** | **str**| The first name of the user | [optional] 
 **lastname** | **str**| The last name of the user | [optional] 
 **email** | **str**| The email address of the user | [optional] 
 **username** | **str**| The username for the user | [optional] 
 **samaccountname** | **str**| The AD login name for the user | [optional] 
 **directory_id** | **int**|  | [optional] 
 **external_id** | **str**| An external identifier that has been set on the user | [optional] 
 **user_ids** | **str**| A comma separated list of OneLogin User IDs | [optional] 
 **custom_attributes_attribute_name** | **str**| The short name of a custom attribute. Note that the attribute name is prefixed with custom_attributes. | [optional] 
 **fields** | **str**| A comma separated list user attributes to return. | [optional] 

### Return type

[**List[ListUsers200ResponseInner]**](ListUsers200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Current-Page - The index number of the current page being returned. <br>  * Page-Items - The number of items returned in the response. <br>  * Total-Count - The total number of items across all pages. <br>  * Total-Pages - The total number of pages to return all results. <br>  * Link - A set of urls which contains premade links for first, next <br>  * Before-Cursor - A string that can be used to request the page of results that preceed the current page using the same set of search filters and pagination options. <br>  * After-Cursor - A string that can be used to request the page of results that follows the current page using the same set of search filters and pagination options. <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**422** | Unprocessable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lock_account_user**
> GenerateToken400Response lock_account_user(user_id, content_type=content_type, lock_account_user_request=lock_account_user_request)

Lock User Account

Lock User Account

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
    api_instance = onelogin.UsersV1Api(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.
    content_type = 'application/json' # str |  (optional) (default to 'application/json')
    lock_account_user_request = onelogin.LockAccountUserRequest() # LockAccountUserRequest |  (optional)

    try:
        # Lock User Account
        api_response = api_instance.lock_account_user(user_id, content_type=content_type, lock_account_user_request=lock_account_user_request)
        print("The response of UsersV1Api->lock_account_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->lock_account_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Set to the id of the user that you want to return. | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]
 **lock_account_user_request** | [**LockAccountUserRequest**](LockAccountUserRequest.md)|  | [optional] 

### Return type

[**GenerateToken400Response**](GenerateToken400Response.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **log_out_user**
> GenerateToken400Response log_out_user(user_id, body=body)

Log User Out

Log Out User

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
    api_instance = onelogin.UsersV1Api(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.
    body = None # object |  (optional)

    try:
        # Log User Out
        api_response = api_instance.log_out_user(user_id, body=body)
        print("The response of UsersV1Api->log_out_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->log_out_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Set to the id of the user that you want to return. | 
 **body** | **object**|  | [optional] 

### Return type

[**GenerateToken400Response**](GenerateToken400Response.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_role**
> GenerateToken400Response remove_user_role(user_id, content_type=content_type, remove_user_role_request=remove_user_role_request)

Remove Roles for a User

Remove Roles for a User

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
    api_instance = onelogin.UsersV1Api(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.
    content_type = 'application/json' # str |  (optional) (default to 'application/json')
    remove_user_role_request = onelogin.RemoveUserRoleRequest() # RemoveUserRoleRequest |  (optional)

    try:
        # Remove Roles for a User
        api_response = api_instance.remove_user_role(user_id, content_type=content_type, remove_user_role_request=remove_user_role_request)
        print("The response of UsersV1Api->remove_user_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->remove_user_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Set to the id of the user that you want to return. | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]
 **remove_user_role_request** | [**RemoveUserRoleRequest**](RemoveUserRoleRequest.md)|  | [optional] 

### Return type

[**GenerateToken400Response**](GenerateToken400Response.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_user_state**
> GenerateToken400Response set_user_state(user_id, content_type=content_type, set_user_state_request=set_user_state_request)

Set User State

Set User State

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
    api_instance = onelogin.UsersV1Api(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.
    content_type = 'application/json' # str |  (optional) (default to 'application/json')
    set_user_state_request = onelogin.SetUserStateRequest() # SetUserStateRequest |  (optional)

    try:
        # Set User State
        api_response = api_instance.set_user_state(user_id, content_type=content_type, set_user_state_request=set_user_state_request)
        print("The response of UsersV1Api->set_user_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->set_user_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Set to the id of the user that you want to return. | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]
 **set_user_state_request** | [**SetUserStateRequest**](SetUserStateRequest.md)|  | [optional] 

### Return type

[**GenerateToken400Response**](GenerateToken400Response.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_password_insecure**
> GenerateToken400Response update_password_insecure(user_id, content_type=content_type, update_password_insecure_request=update_password_insecure_request)

Set Password Using ID in Cleartext

Update User password using their ID. This is done in cleartext and is insecure.

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
    api_instance = onelogin.UsersV1Api(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.
    content_type = 'application/json' # str |  (optional) (default to 'application/json')
    update_password_insecure_request = onelogin.UpdatePasswordInsecureRequest() # UpdatePasswordInsecureRequest |  (optional)

    try:
        # Set Password Using ID in Cleartext
        api_response = api_instance.update_password_insecure(user_id, content_type=content_type, update_password_insecure_request=update_password_insecure_request)
        print("The response of UsersV1Api->update_password_insecure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->update_password_insecure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Set to the id of the user that you want to return. | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]
 **update_password_insecure_request** | [**UpdatePasswordInsecureRequest**](UpdatePasswordInsecureRequest.md)|  | [optional] 

### Return type

[**GenerateToken400Response**](GenerateToken400Response.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_password_secure**
> GenerateToken400Response update_password_secure(user_id, content_type=content_type, update_password_secure_request=update_password_secure_request)

Set Password Using ID and SHA-256 and Salt

Update User Password Using ID and SHA-256 with salt.

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
    api_instance = onelogin.UsersV1Api(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.
    content_type = 'application/json' # str |  (optional) (default to 'application/json')
    update_password_secure_request = onelogin.UpdatePasswordSecureRequest() # UpdatePasswordSecureRequest |  (optional)

    try:
        # Set Password Using ID and SHA-256 and Salt
        api_response = api_instance.update_password_secure(user_id, content_type=content_type, update_password_secure_request=update_password_secure_request)
        print("The response of UsersV1Api->update_password_secure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->update_password_secure: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Set to the id of the user that you want to return. | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]
 **update_password_secure_request** | [**UpdatePasswordSecureRequest**](UpdatePasswordSecureRequest.md)|  | [optional] 

### Return type

[**GenerateToken400Response**](GenerateToken400Response.md)

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> ListUsers200ResponseInner update_user(user_id, list_users200_response_inner, mappings=mappings, validate_policy=validate_policy)

Update a User

Update a User

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
    api_instance = onelogin.UsersV1Api(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.
    list_users200_response_inner = onelogin.ListUsers200ResponseInner() # ListUsers200ResponseInner | 
    mappings = 'mappings_example' # str | Controls how mappings will be applied to the user on creation. Defaults to async. (optional)
    validate_policy = True # bool | Will passwords validate against the User Policy? Defaults to true. (optional)

    try:
        # Update a User
        api_response = api_instance.update_user(user_id, list_users200_response_inner, mappings=mappings, validate_policy=validate_policy)
        print("The response of UsersV1Api->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV1Api->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Set to the id of the user that you want to return. | 
 **list_users200_response_inner** | [**ListUsers200ResponseInner**](ListUsers200ResponseInner.md)|  | 
 **mappings** | **str**| Controls how mappings will be applied to the user on creation. Defaults to async. | [optional] 
 **validate_policy** | **bool**| Will passwords validate against the User Policy? Defaults to true. | [optional] 

### Return type

[**ListUsers200ResponseInner**](ListUsers200ResponseInner.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The full user resource is returned |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |
**422** | Unprocessable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

