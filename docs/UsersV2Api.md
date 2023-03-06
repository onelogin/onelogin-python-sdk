# onelogin.UsersV2Api

All URIs are relative to *https://your-api-subdomain.onelogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user2**](UsersV2Api.md#create_user2) | **POST** /api/2/users | Create User
[**delete_user2**](UsersV2Api.md#delete_user2) | **DELETE** /api/2/users/{user_id} | Delete User
[**get_user2**](UsersV2Api.md#get_user2) | **GET** /api/2/users/{user_id} | Get User
[**get_user_apps2**](UsersV2Api.md#get_user_apps2) | **GET** /api/2/users/{user_id}/apps | Get User Apps
[**list_users2**](UsersV2Api.md#list_users2) | **GET** /api/2/users | List Users
[**update_user2**](UsersV2Api.md#update_user2) | **PUT** /api/2/users/{user_id} | Update User


# **create_user2**
> User create_user2(mappings=mappings, validate_policy=validate_policy, user=user)

Create User

Create User

### Example

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


# Enter a context with an instance of the API client
with onelogin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onelogin.UsersV2Api(api_client)
    mappings = 'mappings_example' # str | Controls how mappings will be applied to the user on creation. Defaults to async. (optional)
    validate_policy = True # bool | Will passwords validate against the User Policy? Defaults to true. (optional)
    user = onelogin.User() # User |  (optional)

    try:
        # Create User
        api_response = api_instance.create_user2(mappings=mappings, validate_policy=validate_policy, user=user)
        print("The response of UsersV2Api->create_user2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV2Api->create_user2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mappings** | **str**| Controls how mappings will be applied to the user on creation. Defaults to async. | [optional] 
 **validate_policy** | **bool**| Will passwords validate against the User Policy? Defaults to true. | [optional] 
 **user** | [**User**](User.md)|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

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

# **delete_user2**
> delete_user2(user_id)

Delete User

Delete User

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
    api_instance = onelogin.UsersV2Api(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.

    try:
        # Delete User
        api_instance.delete_user2(user_id)
    except Exception as e:
        print("Exception when calling UsersV2Api->delete_user2: %s\n" % e)
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

# **get_user2**
> User get_user2(user_id)

Get User

Get User

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
    api_instance = onelogin.UsersV2Api(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.

    try:
        # Get User
        api_response = api_instance.get_user2(user_id)
        print("The response of UsersV2Api->get_user2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV2Api->get_user2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Set to the id of the user that you want to return. | 

### Return type

[**User**](User.md)

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

# **get_user_apps2**
> List[GetUserApps200ResponseInner] get_user_apps2(user_id, ignore_visibility=ignore_visibility)

Get User Apps

Get User Apps

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
    api_instance = onelogin.UsersV2Api(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.
    ignore_visibility = False # bool | Defaults to `false`. When `true` will show all apps that are assigned to a user regardless of their portal visibility setting. (optional) (default to False)

    try:
        # Get User Apps
        api_response = api_instance.get_user_apps2(user_id, ignore_visibility=ignore_visibility)
        print("The response of UsersV2Api->get_user_apps2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV2Api->get_user_apps2: %s\n" % e)
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

# **list_users2**
> List[User] list_users2(limit=limit, page=page, cursor=cursor, created_since=created_since, created_until=created_until, updated_since=updated_since, updated_until=updated_until, last_login_since=last_login_since, last_login_until=last_login_until, firstname=firstname, lastname=lastname, email=email, username=username, samaccountname=samaccountname, directory_id=directory_id, external_id=external_id, user_ids=user_ids, custom_attributes_attribute_name=custom_attributes_attribute_name, fields=fields)

List Users

Get a list of users

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
    api_instance = onelogin.UsersV2Api(api_client)
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
    fields = 'fields_example' # str | Optional. Comma delimited list of fields to return. (optional)

    try:
        # List Users
        api_response = api_instance.list_users2(limit=limit, page=page, cursor=cursor, created_since=created_since, created_until=created_until, updated_since=updated_since, updated_until=updated_until, last_login_since=last_login_since, last_login_until=last_login_until, firstname=firstname, lastname=lastname, email=email, username=username, samaccountname=samaccountname, directory_id=directory_id, external_id=external_id, user_ids=user_ids, custom_attributes_attribute_name=custom_attributes_attribute_name, fields=fields)
        print("The response of UsersV2Api->list_users2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV2Api->list_users2: %s\n" % e)
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
 **fields** | **str**| Optional. Comma delimited list of fields to return. | [optional] 

### Return type

[**List[User]**](User.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Current-Page -  <br>  * Page-Items -  <br>  * Total-Count -  <br>  * Total-Pages -  <br>  * Link -  <br>  * Before-Cursor -  <br>  * After-Cursor -  <br>  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**422** | Unprocessable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user2**
> User update_user2(user_id, mappings=mappings, validate_policy=validate_policy, user=user)

Update User

Update User

### Example

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


# Enter a context with an instance of the API client
with onelogin.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = onelogin.UsersV2Api(api_client)
    user_id = 56 # int | Set to the id of the user that you want to return.
    mappings = 'mappings_example' # str | Controls how mappings will be applied to the user on creation. Defaults to async. (optional)
    validate_policy = True # bool | Will passwords validate against the User Policy? Defaults to true. (optional)
    user = onelogin.User() # User |  (optional)

    try:
        # Update User
        api_response = api_instance.update_user2(user_id, mappings=mappings, validate_policy=validate_policy, user=user)
        print("The response of UsersV2Api->update_user2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersV2Api->update_user2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**| Set to the id of the user that you want to return. | 
 **mappings** | **str**| Controls how mappings will be applied to the user on creation. Defaults to async. | [optional] 
 **validate_policy** | **bool**| Will passwords validate against the User Policy? Defaults to true. | [optional] 
 **user** | [**User**](User.md)|  | [optional] 

### Return type

[**User**](User.md)

### Authorization

No authorization required

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

