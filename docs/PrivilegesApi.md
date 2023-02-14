# openapi_client.PrivilegesApi

All URIs are relative to *https://your-api-subdomain.onelogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_privilege_to_role**](PrivilegesApi.md#add_privilege_to_role) | **POST** /api/1/privileges/{privilege_id}/roles | Assign a Privilege to Roles
[**assign_users_to_privilege**](PrivilegesApi.md#assign_users_to_privilege) | **POST** /api/1/privileges/{privilege_id}/users | Assign Users to a Privilege
[**create_privilege**](PrivilegesApi.md#create_privilege) | **POST** /api/1/privileges | Create a Privilege
[**delete_privilege**](PrivilegesApi.md#delete_privilege) | **DELETE** /api/1/privileges/{privilege_id} | Delete a Privilege
[**delete_role_from_privilege**](PrivilegesApi.md#delete_role_from_privilege) | **DELETE** /api/1/privileges/{privilege_id}/roles/{role_id} | Remove a Privilege from a Role
[**get_assigned_user**](PrivilegesApi.md#get_assigned_user) | **GET** /api/1/privileges/{privilege_id}/users | Get Users assigned to a Privilege
[**get_privilege**](PrivilegesApi.md#get_privilege) | **GET** /api/1/privileges/{privilege_id} | Get a Privilege
[**list_privelege_roles**](PrivilegesApi.md#list_privelege_roles) | **GET** /api/1/privileges/{privilege_id}/roles | Get Roles assigned to Privilege
[**list_priveleges**](PrivilegesApi.md#list_priveleges) | **GET** /api/1/privileges | List Privileges
[**remove_user_from_privilege**](PrivilegesApi.md#remove_user_from_privilege) | **DELETE** /api/1/privileges/{privilege_id}/users/{user_id} | Remove a Privilege from Users
[**update_privilege**](PrivilegesApi.md#update_privilege) | **PUT** /api/1/privileges/{privilege_id} | Update a Privilege


# **add_privilege_to_role**
> AddPrivilegeToRole201Response add_privilege_to_role(privilege_id, content_type=content_type, add_privilege_to_role_request=add_privilege_to_role_request)

Assign a Privilege to Roles

Add roles to privilege 

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
    api_instance = openapi_client.PrivilegesApi(api_client)
    privilege_id = 'privilege_id_example' # str | 
    content_type = 'application/json' # str |  (optional) (default to 'application/json')
    add_privilege_to_role_request = openapi_client.AddPrivilegeToRoleRequest() # AddPrivilegeToRoleRequest |  (optional)

    try:
        # Assign a Privilege to Roles
        api_response = api_instance.add_privilege_to_role(privilege_id, content_type=content_type, add_privilege_to_role_request=add_privilege_to_role_request)
        print("The response of PrivilegesApi->add_privilege_to_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivilegesApi->add_privilege_to_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **privilege_id** | **str**|  | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]
 **add_privilege_to_role_request** | [**AddPrivilegeToRoleRequest**](AddPrivilegeToRoleRequest.md)|  | [optional] 

### Return type

[**AddPrivilegeToRole201Response**](AddPrivilegeToRole201Response.md)

### Authorization

[OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_users_to_privilege**
> AddPrivilegeToRole201Response assign_users_to_privilege(privilege_id, content_type=content_type, assign_users_to_privilege_request=assign_users_to_privilege_request)

Assign Users to a Privilege

Assign Users to Privilege

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
    api_instance = openapi_client.PrivilegesApi(api_client)
    privilege_id = 'privilege_id_example' # str | 
    content_type = 'application/json' # str |  (optional) (default to 'application/json')
    assign_users_to_privilege_request = openapi_client.AssignUsersToPrivilegeRequest() # AssignUsersToPrivilegeRequest |  (optional)

    try:
        # Assign Users to a Privilege
        api_response = api_instance.assign_users_to_privilege(privilege_id, content_type=content_type, assign_users_to_privilege_request=assign_users_to_privilege_request)
        print("The response of PrivilegesApi->assign_users_to_privilege:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivilegesApi->assign_users_to_privilege: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **privilege_id** | **str**|  | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]
 **assign_users_to_privilege_request** | [**AssignUsersToPrivilegeRequest**](AssignUsersToPrivilegeRequest.md)|  | [optional] 

### Return type

[**AddPrivilegeToRole201Response**](AddPrivilegeToRole201Response.md)

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

# **create_privilege**
> CreatePrivilege200Response create_privilege(content_type=content_type, list_priveleges200_response_inner=list_priveleges200_response_inner)

Create a Privilege

Create privilege

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
    api_instance = openapi_client.PrivilegesApi(api_client)
    content_type = 'application/json' # str |  (optional) (default to 'application/json')
    list_priveleges200_response_inner = {"name":"User Helpdesk","description":"Can administer helpdesk users","privilege":{"Version":"2018-05-18","Statement":[{"Effect":"Allow","Action":["Users:List","Users:Get","Users:Unlock","Users:ResetPassword","Users:GenerateTempMfaToken"],"Scope":["*"]}]}} # ListPriveleges200ResponseInner |  (optional)

    try:
        # Create a Privilege
        api_response = api_instance.create_privilege(content_type=content_type, list_priveleges200_response_inner=list_priveleges200_response_inner)
        print("The response of PrivilegesApi->create_privilege:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivilegesApi->create_privilege: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]
 **list_priveleges200_response_inner** | [**ListPriveleges200ResponseInner**](ListPriveleges200ResponseInner.md)|  | [optional] 

### Return type

[**CreatePrivilege200Response**](CreatePrivilege200Response.md)

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

# **delete_privilege**
> delete_privilege(privilege_id, content_type=content_type)

Delete a Privilege

Delete

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
    api_instance = openapi_client.PrivilegesApi(api_client)
    privilege_id = 'privilege_id_example' # str | 
    content_type = 'application/json' # str |  (optional) (default to 'application/json')

    try:
        # Delete a Privilege
        api_instance.delete_privilege(privilege_id, content_type=content_type)
    except Exception as e:
        print("Exception when calling PrivilegesApi->delete_privilege: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **privilege_id** | **str**|  | 
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
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role_from_privilege**
> delete_role_from_privilege(privilege_id, role_id, content_type=content_type)

Remove a Privilege from a Role

Add roles to privilege

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
    api_instance = openapi_client.PrivilegesApi(api_client)
    privilege_id = 'privilege_id_example' # str | 
    role_id = 'role_id_example' # str | 
    content_type = 'application/json' # str |  (optional) (default to 'application/json')

    try:
        # Remove a Privilege from a Role
        api_instance.delete_role_from_privilege(privilege_id, role_id, content_type=content_type)
    except Exception as e:
        print("Exception when calling PrivilegesApi->delete_role_from_privilege: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **privilege_id** | **str**|  | 
 **role_id** | **str**|  | 
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
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assigned_user**
> GetAssignedUser200Response get_assigned_user(privilege_id, content_type=content_type)

Get Users assigned to a Privilege

Get Assigned Users

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
    api_instance = openapi_client.PrivilegesApi(api_client)
    privilege_id = 'privilege_id_example' # str | 
    content_type = 'application/json' # str |  (optional) (default to 'application/json')

    try:
        # Get Users assigned to a Privilege
        api_response = api_instance.get_assigned_user(privilege_id, content_type=content_type)
        print("The response of PrivilegesApi->get_assigned_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivilegesApi->get_assigned_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **privilege_id** | **str**|  | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]

### Return type

[**GetAssignedUser200Response**](GetAssignedUser200Response.md)

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

# **get_privilege**
> ListPriveleges200ResponseInner get_privilege(privilege_id, content_type=content_type)

Get a Privilege

Get a Privilige

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
    api_instance = openapi_client.PrivilegesApi(api_client)
    privilege_id = 'privilege_id_example' # str | 
    content_type = 'application/json' # str |  (optional) (default to 'application/json')

    try:
        # Get a Privilege
        api_response = api_instance.get_privilege(privilege_id, content_type=content_type)
        print("The response of PrivilegesApi->get_privilege:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivilegesApi->get_privilege: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **privilege_id** | **str**|  | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]

### Return type

[**ListPriveleges200ResponseInner**](ListPriveleges200ResponseInner.md)

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

# **list_privelege_roles**
> ListPrivelegeRoles200Response list_privelege_roles(privilege_id, content_type=content_type)

Get Roles assigned to Privilege

List roles for privilege

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
    api_instance = openapi_client.PrivilegesApi(api_client)
    privilege_id = 'privilege_id_example' # str | 
    content_type = 'application/json' # str |  (optional) (default to 'application/json')

    try:
        # Get Roles assigned to Privilege
        api_response = api_instance.list_privelege_roles(privilege_id, content_type=content_type)
        print("The response of PrivilegesApi->list_privelege_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivilegesApi->list_privelege_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **privilege_id** | **str**|  | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]

### Return type

[**ListPrivelegeRoles200Response**](ListPrivelegeRoles200Response.md)

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

# **list_priveleges**
> List[ListPriveleges200ResponseInner] list_priveleges(content_type=content_type)

List Privileges

List Privileges

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
    api_instance = openapi_client.PrivilegesApi(api_client)
    content_type = 'application/json' # str |  (optional) (default to 'application/json')

    try:
        # List Privileges
        api_response = api_instance.list_priveleges(content_type=content_type)
        print("The response of PrivilegesApi->list_priveleges:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivilegesApi->list_priveleges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]

### Return type

[**List[ListPriveleges200ResponseInner]**](ListPriveleges200ResponseInner.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_from_privilege**
> remove_user_from_privilege(privilege_id, user_id, content_type=content_type)

Remove a Privilege from Users

Remove a Privilege from Users

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
    api_instance = openapi_client.PrivilegesApi(api_client)
    privilege_id = 'privilege_id_example' # str | 
    user_id = 56 # int | Set to the id of the user that you want to return.
    content_type = 'application/json' # str |  (optional) (default to 'application/json')

    try:
        # Remove a Privilege from Users
        api_instance.remove_user_from_privilege(privilege_id, user_id, content_type=content_type)
    except Exception as e:
        print("Exception when calling PrivilegesApi->remove_user_from_privilege: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **privilege_id** | **str**|  | 
 **user_id** | **int**| Set to the id of the user that you want to return. | 
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
**204** | No Content |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_privilege**
> UpdatePrivilege200Response update_privilege(privilege_id, content_type=content_type, list_priveleges200_response_inner=list_priveleges200_response_inner)

Update a Privilege

Update privilege

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
    api_instance = openapi_client.PrivilegesApi(api_client)
    privilege_id = 'privilege_id_example' # str | 
    content_type = 'application/json' # str |  (optional) (default to 'application/json')
    list_priveleges200_response_inner = {"name":"User Administrator","description":"Can administer users","privilege":{"Version":"2018-05-18","Statement":[{"Effect":"Allow","Action":["Users:List","Users:Get","Users:Unlock","Users:ResetPassword","Users:GenerateTempMfaToken"],"Scope":["*"]}]}} # ListPriveleges200ResponseInner |  (optional)

    try:
        # Update a Privilege
        api_response = api_instance.update_privilege(privilege_id, content_type=content_type, list_priveleges200_response_inner=list_priveleges200_response_inner)
        print("The response of PrivilegesApi->update_privilege:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivilegesApi->update_privilege: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **privilege_id** | **str**|  | 
 **content_type** | **str**|  | [optional] [default to &#39;application/json&#39;]
 **list_priveleges200_response_inner** | [**ListPriveleges200ResponseInner**](ListPriveleges200ResponseInner.md)|  | [optional] 

### Return type

[**UpdatePrivilege200Response**](UpdatePrivilege200Response.md)

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

