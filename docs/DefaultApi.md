# openapi_client.DefaultApi

All URIs are relative to *https://onelogininc.onelogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_factor**](DefaultApi.md#activate_factor) | **POST** /api/2/mfa/users/{user_id}/verifications | 
[**add_access_token_claim**](DefaultApi.md#add_access_token_claim) | **POST** /api/2/api_authorizations/{id}/claims | 
[**add_client_app**](DefaultApi.md#add_client_app) | **POST** /api/2/api_authorizations/{id}/clients | 
[**add_role_admins**](DefaultApi.md#add_role_admins) | **POST** /api/2/roles/{role_id}/admins | 
[**add_role_users**](DefaultApi.md#add_role_users) | **POST** /api/2/roles/{role_id}/users | 
[**add_scope**](DefaultApi.md#add_scope) | **POST** /api/2/api_authorizations/{id}/scopes | 
[**bulk_mapping_sort**](DefaultApi.md#bulk_mapping_sort) | **PUT** /api/2/apps/mappings/sort | 
[**bulk_sort**](DefaultApi.md#bulk_sort) | **PUT** /api/2/apps/{app_id}/rules/sort | 
[**create_app**](DefaultApi.md#create_app) | **POST** /api/2/apps | 
[**create_authorization_server**](DefaultApi.md#create_authorization_server) | **POST** /api/2/api_authorizations | 
[**create_environment_variable**](DefaultApi.md#create_environment_variable) | **POST** /api/2/hooks/envs | 
[**create_hook**](DefaultApi.md#create_hook) | **POST** /api/2/hooks | 
[**create_mapping**](DefaultApi.md#create_mapping) | **POST** /api/2/mappings | 
[**create_risk_rule**](DefaultApi.md#create_risk_rule) | **POST** /api/2/risk/rules | 
[**create_roles**](DefaultApi.md#create_roles) | **POST** /api/2/roles | 
[**create_rule**](DefaultApi.md#create_rule) | **POST** /api/2/apps/{app_id}/rules | 
[**create_user**](DefaultApi.md#create_user) | **POST** /api/2/users | 
[**delete_access_token_claim**](DefaultApi.md#delete_access_token_claim) | **DELETE** /api/2/api_authorizations/{id}/claims/{claim_id} | 
[**delete_app**](DefaultApi.md#delete_app) | **DELETE** /api/2/apps/{app_id} | 
[**delete_app_parameter**](DefaultApi.md#delete_app_parameter) | **DELETE** /api/2/apps/{app_id}/parameters/{parameter_id} | 
[**delete_authorization_server**](DefaultApi.md#delete_authorization_server) | **DELETE** /api/2/api_authorizations/{id} | 
[**delete_environment_variable**](DefaultApi.md#delete_environment_variable) | **DELETE** /api/2/hooks/envs/{envvar_id} | 
[**delete_factor**](DefaultApi.md#delete_factor) | **DELETE** /api/2/mfa/users/{user_id}/devices/{device_id} | 
[**delete_hook**](DefaultApi.md#delete_hook) | **DELETE** /api/2/hooks/{hook_id} | 
[**delete_mapping**](DefaultApi.md#delete_mapping) | **DELETE** /api/2/mappings/{mapping_id} | 
[**delete_risk_rule**](DefaultApi.md#delete_risk_rule) | **DELETE** /api/2/risk/rules/{risk_rule_id} | 
[**delete_role**](DefaultApi.md#delete_role) | **DELETE** /api/2/roles/{role_id} | 
[**delete_rule**](DefaultApi.md#delete_rule) | **DELETE** /api/2/apps/{app_id}/rules/{rule_id} | 
[**delete_scope**](DefaultApi.md#delete_scope) | **DELETE** /api/2/api_authorizations/{id}/scopes/{scope_id} | 
[**delete_user**](DefaultApi.md#delete_user) | **DELETE** /api/2/users/{user_id} | 
[**dry_run_mapping**](DefaultApi.md#dry_run_mapping) | **POST** /api/2/mappings/{mapping_id}/dryrun | 
[**enroll_factor**](DefaultApi.md#enroll_factor) | **POST** /api/2/mfa/users/{user_id}/registrations | 
[**generate_mfa_token**](DefaultApi.md#generate_mfa_token) | **POST** /api/2/mfs/users/{user_id}/mfa_token | 
[**generate_saml_assertion**](DefaultApi.md#generate_saml_assertion) | **POST** /api/2/saml_assertion | 
[**generate_token**](DefaultApi.md#generate_token) | **POST** /auth/oauth2/v2/token | 
[**get_app**](DefaultApi.md#get_app) | **GET** /api/2/apps/{app_id} | 
[**get_authorization_server**](DefaultApi.md#get_authorization_server) | **GET** /api/2/api_authorizations/{id} | 
[**get_available_factors**](DefaultApi.md#get_available_factors) | **GET** /api/2/mfa/users/{user_id}/factors | 
[**get_client_apps**](DefaultApi.md#get_client_apps) | **GET** /api/2/api_authorizations/{id}/clients | 
[**get_enrolled_factors**](DefaultApi.md#get_enrolled_factors) | **GET** /api/2/mfa/users/{user_id}/devices | 
[**get_environment_variable**](DefaultApi.md#get_environment_variable) | **GET** /api/2/hooks/envs/{envvar_id} | 
[**get_hook**](DefaultApi.md#get_hook) | **GET** /api/2/hooks/{hook_id} | 
[**get_logs**](DefaultApi.md#get_logs) | **GET** /api/2/hooks/{hook_id}/logs | 
[**get_mapping**](DefaultApi.md#get_mapping) | **GET** /api/2/mappings/{mapping_id} | 
[**get_rate_limit**](DefaultApi.md#get_rate_limit) | **GET** /auth/rate_limit | 
[**get_risk_rule**](DefaultApi.md#get_risk_rule) | **GET** /api/2/risk/rules/{risk_rule_id} | 
[**get_risk_score**](DefaultApi.md#get_risk_score) | **POST** /api/2/risk/verify | 
[**get_role**](DefaultApi.md#get_role) | **GET** /api/2/roles/{role_id} | 
[**get_role_admins**](DefaultApi.md#get_role_admins) | **GET** /api/2/roles/{role_id}/admins | 
[**get_role_apps**](DefaultApi.md#get_role_apps) | **GET** /api/2/roles/{role_id}/apps | 
[**get_role_users**](DefaultApi.md#get_role_users) | **GET** /api/2/roles/{role_id}/users | 
[**get_rule**](DefaultApi.md#get_rule) | **GET** /api/2/apps/{app_id}/rules/{rule_id} | 
[**get_score_insights**](DefaultApi.md#get_score_insights) | **GET** /api/2/risk/scores | 
[**get_user**](DefaultApi.md#get_user) | **GET** /api/2/users/{user_id} | 
[**get_user_apps**](DefaultApi.md#get_user_apps) | **GET** /api/2/users/{user_id}/apps | 
[**list_access_token_claims**](DefaultApi.md#list_access_token_claims) | **GET** /api/2/api_authorizations/{id}/claims | 
[**list_action_values**](DefaultApi.md#list_action_values) | **GET** /api/2/apps/{app_id}/rules/actions/{actuion_value}/values | 
[**list_actions**](DefaultApi.md#list_actions) | **GET** /api/2/apps/{app_id}/rules/actions | 
[**list_app_users**](DefaultApi.md#list_app_users) | **GET** /api/2/apps/{app_id}/users | 
[**list_apps**](DefaultApi.md#list_apps) | **GET** /api/2/apps | 
[**list_authorization_servers**](DefaultApi.md#list_authorization_servers) | **GET** /api/2/api_authorizations | 
[**list_condition_operators**](DefaultApi.md#list_condition_operators) | **GET** /api/2/apps/{app_id}/rules/conditions/{condition_value}/operators | 
[**list_condition_values**](DefaultApi.md#list_condition_values) | **GET** /api/2/apps/{app_id}/rules/conditions/{condition_value}/values | 
[**list_conditions**](DefaultApi.md#list_conditions) | **GET** /api/2/apps/{app_id}/rules/conditions | 
[**list_connectors**](DefaultApi.md#list_connectors) | **GET** /api/2/connectors | 
[**list_environment_variables**](DefaultApi.md#list_environment_variables) | **GET** /api/2/hooks/envs | 
[**list_hooks**](DefaultApi.md#list_hooks) | **GET** /api/2/hooks | 
[**list_mapping_action_values**](DefaultApi.md#list_mapping_action_values) | **GET** /api/2/apps/mappings/actions/{actuion_value}/values | 
[**list_mapping_actions**](DefaultApi.md#list_mapping_actions) | **GET** /api/2/apps/mappings/actions | 
[**list_mapping_condition_operators**](DefaultApi.md#list_mapping_condition_operators) | **GET** /api/2/apps/mappings/conditions/{condition_value}/operators | 
[**list_mapping_condition_values**](DefaultApi.md#list_mapping_condition_values) | **GET** /api/2/apps/mappings/conditions/{condition_value}/values | 
[**list_mapping_conditions**](DefaultApi.md#list_mapping_conditions) | **GET** /api/2/apps/mappings/conditions | 
[**list_mappings**](DefaultApi.md#list_mappings) | **GET** /api/2/mappings | 
[**list_risk_rules**](DefaultApi.md#list_risk_rules) | **GET** /api/2/risk/rules | 
[**list_roles**](DefaultApi.md#list_roles) | **GET** /api/2/roles | 
[**list_rules**](DefaultApi.md#list_rules) | **GET** /api/2/apps/{app_id}/rules | 
[**list_scopes**](DefaultApi.md#list_scopes) | **GET** /api/2/api_authorizations/{id}/scopes | 
[**list_users**](DefaultApi.md#list_users) | **GET** /api/2/users | 
[**remove_client_app**](DefaultApi.md#remove_client_app) | **DELETE** /api/2/api_authorizations/{id}/clients/{client_app_id} | 
[**remove_role_admins**](DefaultApi.md#remove_role_admins) | **DELETE** /api/2/roles/{role_id}/admins | 
[**remove_role_users**](DefaultApi.md#remove_role_users) | **DELETE** /api/2/roles/{role_id}/users | 
[**revoke_token**](DefaultApi.md#revoke_token) | **POST** /auth/oauth2/revoke | 
[**set_role_apps**](DefaultApi.md#set_role_apps) | **PUT** /api/2/roles/{role_id}/apps | 
[**track_event**](DefaultApi.md#track_event) | **POST** /api/2/risk/events | 
[**update_access_token_claim**](DefaultApi.md#update_access_token_claim) | **PUT** /api/2/api_authorizations/{id}/claims/{claim_id} | 
[**update_app**](DefaultApi.md#update_app) | **PUT** /api/2/apps/{app_id} | 
[**update_authorization_server**](DefaultApi.md#update_authorization_server) | **PUT** /api/2/api_authorizations/{id} | 
[**update_client_app**](DefaultApi.md#update_client_app) | **PUT** /api/2/api_authorizations/{id}/clients/{client_app_id} | 
[**update_environment_variable**](DefaultApi.md#update_environment_variable) | **PUT** /api/2/hooks/envs/{envvar_id} | 
[**update_hook**](DefaultApi.md#update_hook) | **PUT** /api/2/hooks/{hook_id} | 
[**update_mapping**](DefaultApi.md#update_mapping) | **PUT** /api/2/mappings/{mapping_id} | 
[**update_risk_rule**](DefaultApi.md#update_risk_rule) | **PUT** /api/2/risk/rules/{risk_rule_id} | 
[**update_role**](DefaultApi.md#update_role) | **PUT** /api/2/roles/{role_id} | 
[**update_rule**](DefaultApi.md#update_rule) | **PUT** /api/2/apps/{app_id}/rules/{rule_id} | 
[**update_scope**](DefaultApi.md#update_scope) | **PUT** /api/2/api_authorizations/{id}/scopes/{scope_id} | 
[**update_user**](DefaultApi.md#update_user) | **PUT** /api/2/users/{user_id} | 
[**verify_enrollment**](DefaultApi.md#verify_enrollment) | **PUT** /api/2/mfa/users/{user_id}/registrations/{registration_id} | 
[**verify_enrollment_voice_protect**](DefaultApi.md#verify_enrollment_voice_protect) | **GET** /api/2/mfa/users/{user_id}/registrations/{registration_id} | 
[**verify_factor**](DefaultApi.md#verify_factor) | **PUT** /api/2/mfa/users/{user_id}/verifications/{verification_id} | 
[**verify_factor_saml**](DefaultApi.md#verify_factor_saml) | **POST** /api/2/saml_assertion/verify_factor | 
[**verify_factor_voice**](DefaultApi.md#verify_factor_voice) | **GET** /api/2/mfa/users/{user_id}/verifications/{verification_id} | 


# **activate_factor**
> activate_factor(authorization, user_id, activate_factor_request)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.activate_factor_request import ActivateFactorRequest
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    user_id = 1 # int | Set to the id of the user.
    activate_factor_request = ActivateFactorRequest(
        device_id=1,
        expires_in=1,
        redirect_to="redirect_to_example",
        custom_message="custom_message_example",
    ) # ActivateFactorRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.activate_factor(authorization, user_id, activate_factor_request)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->activate_factor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **user_id** | **int**| Set to the id of the user. |
 **activate_factor_request** | [**ActivateFactorRequest**](ActivateFactorRequest.md)|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CREATED |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_access_token_claim**
> Id add_access_token_claim(authorization, id, add_access_token_claim_request)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.add_access_token_claim_request import AddAccessTokenClaimRequest
from openapi_client.model.status1 import Status1
from openapi_client.model.id import Id
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    id = 1 # int | 
    add_access_token_claim_request = AddAccessTokenClaimRequest(
        name="name_example",
        user_attribute_mappings="user_attribute_mappings_example",
        user_attribute_macros="user_attribute_macros_example",
    ) # AddAccessTokenClaimRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_access_token_claim(authorization, id, add_access_token_claim_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->add_access_token_claim: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **id** | **int**|  |
 **add_access_token_claim_request** | [**AddAccessTokenClaimRequest**](AddAccessTokenClaimRequest.md)|  |

### Return type

[**Id**](Id.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |
**422** | This name already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_client_app**
> ClientApp add_client_app(authorization, id, add_client_app_request)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.client_app import ClientApp
from openapi_client.model.status1 import Status1
from openapi_client.model.add_client_app_request import AddClientAppRequest
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    id = 1 # int | 
    add_client_app_request = AddClientAppRequest(
        app_id=1,
        scopes=[
            1,
        ],
    ) # AddClientAppRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_client_app(authorization, id, add_client_app_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->add_client_app: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **id** | **int**|  |
 **add_client_app_request** | [**AddClientAppRequest**](AddClientAppRequest.md)|  |

### Return type

[**ClientApp**](ClientApp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CREATED |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |
**422** | An invalid scope id has been provided |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_role_admins**
> [AddRoleUsers200ResponseInner] add_role_admins(authorization, role_id, request_body)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.add_role_users200_response_inner import AddRoleUsers200ResponseInner
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    role_id = 1 # int | Set to the id of the role you want to return.
    request_body = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_role_admins(authorization, role_id, request_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->add_role_admins: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **role_id** | **int**| Set to the id of the role you want to return. |
 **request_body** | **[int]**|  |

### Return type

[**[AddRoleUsers200ResponseInner]**](AddRoleUsers200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_role_users**
> [AddRoleUsers200ResponseInner] add_role_users(authorization, role_id, request_body)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.add_role_users200_response_inner import AddRoleUsers200ResponseInner
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    role_id = 1 # int | Set to the id of the role you want to return.
    request_body = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_role_users(authorization, role_id, request_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->add_role_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **role_id** | **int**| Set to the id of the role you want to return. |
 **request_body** | **[int]**|  |

### Return type

[**[AddRoleUsers200ResponseInner]**](AddRoleUsers200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**422** | Indicates that the syntax of the request is good but a value supplied is not valid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_scope**
> Id add_scope(authorization, id, add_scope_request)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.add_scope_request import AddScopeRequest
from openapi_client.model.status1 import Status1
from openapi_client.model.id import Id
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    id = 1 # int | 
    add_scope_request = AddScopeRequest(
        value="value_example",
        description="description_example",
    ) # AddScopeRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.add_scope(authorization, id, add_scope_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->add_scope: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **id** | **int**|  |
 **add_scope_request** | [**AddScopeRequest**](AddScopeRequest.md)|  |

### Return type

[**Id**](Id.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |
**422** | This name already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_mapping_sort**
> MappingIdList bulk_mapping_sort(authorization, mapping_id_list)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.mapping_id_list import MappingIdList
from openapi_client.model.status1 import Status1
from openapi_client.model.error_status import ErrorStatus
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    mapping_id_list = MappingIdList([
        1,
    ]) # MappingIdList | The request body must contain an array of User Mapping IDs in the desired order.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.bulk_mapping_sort(authorization, mapping_id_list)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->bulk_mapping_sort: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **mapping_id_list** | [**MappingIdList**](MappingIdList.md)| The request body must contain an array of User Mapping IDs in the desired order. |

### Return type

[**MappingIdList**](MappingIdList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | On success a complete list of ordered mappings is returned. |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**422** | Indicates that not all mapping IDs were included in the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_sort**
> RuleIdList bulk_sort(authorization, app_id, rule_id_list)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.rule_id_list import RuleIdList
from openapi_client.model.status1 import Status1
from openapi_client.model.error_status import ErrorStatus
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    app_id = 1 # int | 
    rule_id_list = RuleIdList([
        1,
    ]) # RuleIdList | The request body must contain an array of App Rule IDs in the desired order.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.bulk_sort(authorization, app_id, rule_id_list)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->bulk_sort: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **app_id** | **int**|  |
 **rule_id_list** | [**RuleIdList**](RuleIdList.md)| The request body must contain an array of App Rule IDs in the desired order. |

### Return type

[**RuleIdList**](RuleIdList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | On success a complete list of ordered rules is returned. |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**422** | Indicates that not all rule IDs were included in the request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_app**
> Schema create_app(authorization, schema)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.schema import Schema
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    schema = Schema(
        id=1,
        connector_id=1,
        name="name_example",
        description="description_example",
        notes="notes_example",
        policy_id=1,
        brand_id=1,
        icon_url="icon_url_example",
        visible=True,
        auth_method=0,
        tab_id=1,
        created_at="created_at_example",
        updated_at="updated_at_example",
        role_ids=[
            1,
        ],
        allow_assumed_signin=True,
        provisioning=SchemaProvisioning(
            enabled=True,
        ),
        sso={},
        configuration={},
        parameters={},
        enforcement_point={},
    ) # Schema | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_app(authorization, schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_app: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **schema** | [**Schema**](Schema.md)|  |

### Return type

[**Schema**](Schema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CREATED |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**422** | Indicates that the syntax of the request is good but a value supplied is not valid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_authorization_server**
> Id create_authorization_server(authorization, create_authorization_server_request)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.create_authorization_server_request import CreateAuthorizationServerRequest
from openapi_client.model.status1 import Status1
from openapi_client.model.id import Id
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    create_authorization_server_request = CreateAuthorizationServerRequest(
        name="name_example",
        description="description_example",
        configuration=AuthServerConfiguration(
            audiences=[
                "audiences_example",
            ],
            refresh_token_expiration_minutes=1,
            resource_identifier="resource_identifier_example",
            access_token_expiration_minutes=1,
        ),
    ) # CreateAuthorizationServerRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_authorization_server(authorization, create_authorization_server_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_authorization_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **create_authorization_server_request** | [**CreateAuthorizationServerRequest**](CreateAuthorizationServerRequest.md)|  |

### Return type

[**Id**](Id.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CREATED |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**422** | Audiences are required |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_environment_variable**
> Envvar create_environment_variable(authorization, create_environment_variable_request)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.create_environment_variable_request import CreateEnvironmentVariableRequest
from openapi_client.model.envvar import Envvar
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    create_environment_variable_request = CreateEnvironmentVariableRequest(
        name="name_example",
        value="value_example",
    ) # CreateEnvironmentVariableRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_environment_variable(authorization, create_environment_variable_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_environment_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **create_environment_variable_request** | [**CreateEnvironmentVariableRequest**](CreateEnvironmentVariableRequest.md)|  |

### Return type

[**Envvar**](Envvar.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CREATED |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**422** | Indicates that the syntax of the request is good but a value supplied is not valid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_hook**
> create_hook(authorization, hook)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.hook import Hook
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    hook = Hook(
        id="id_example",
        type="type_example",
        disabled=True,
        timeout=1,
        env_vars=[
            "env_vars_example",
        ],
        runtime="runtime_example",
        retries=0,
        packages={},
        function="function_example",
        context_version="context_version_example",
        status="ready",
        options=HookOptions(
            risk_enabled=True,
            location_enabled=True,
            mfa_device_info_enabled=True,
        ),
        conditions=[
            HookConditionsInner(
                source="source_example",
                operator="operator_example",
                value="value_example",
            ),
        ],
        created_at="created_at_example",
        updated_at="updated_at_example",
    ) # Hook | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.create_hook(authorization, hook)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_hook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **hook** | [**Hook**](Hook.md)|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_mapping**
> int create_mapping(authorization, mapping)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.status1 import Status1
from openapi_client.model.error_status import ErrorStatus
from openapi_client.model.mapping import Mapping
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    mapping = Mapping(
        id=1,
        name="name_example",
        enabled=True,
        match="all",
        position=1,
        conditions=[
            Condition(
                source="source_example",
                operator="operator_example",
                value="value_example",
            ),
        ],
        actions=[
            Action(
                action="action_example",
                value=[
                    "value_example",
                ],
                expression="expression_example",
                scriplet="scriplet_example",
                macro="macro_example",
            ),
        ],
    ) # Mapping | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_mapping(authorization, mapping)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_mapping: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **mapping** | [**Mapping**](Mapping.md)|  |

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CREATED |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**422** | UNPROCESSABLE_ENTRY |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_risk_rule**
> create_risk_rule(authorization, risk_rule)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.risk_rule import RiskRule
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    risk_rule = RiskRule(
        id="id_example",
        name="name_example",
        description="description_example",
        type="blacklist",
        target="location.ip",
        filters=[
            "filters_example",
        ],
        source=Source(
            id="id_example",
            name="name_example",
        ),
    ) # RiskRule | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.create_risk_rule(authorization, risk_rule)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_risk_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **risk_rule** | [**RiskRule**](RiskRule.md)|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_roles**
> [CreateRoles201ResponseInner] create_roles(authorization)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.status1 import Status1
from openapi_client.model.create_roles201_response_inner import CreateRoles201ResponseInner
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_roles(authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_roles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |

### Return type

[**[CreateRoles201ResponseInner]**](CreateRoles201ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CREATED |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_rule**
> RuleId create_rule(authorization, app_id, rule)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.rule_id import RuleId
from openapi_client.model.rule import Rule
from openapi_client.model.status1 import Status1
from openapi_client.model.error_status import ErrorStatus
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    app_id = 1 # int | 
    rule = Rule(
        id=1,
        name="name_example",
        match="all",
        enabled=True,
        position=1,
        conditions=[
            Condition(
                source="source_example",
                operator="operator_example",
                value="value_example",
            ),
        ],
        actions=[
            Action(
                action="action_example",
                value=[
                    "value_example",
                ],
                expression="expression_example",
                scriplet="scriplet_example",
                macro="macro_example",
            ),
        ],
    ) # Rule | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_rule(authorization, app_id, rule)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **app_id** | **int**|  |
 **rule** | [**Rule**](Rule.md)|  |

### Return type

[**RuleId**](RuleId.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | CREATED |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**422** | UNPROCESSABLE ENTRY |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> User create_user(authorization, user)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.user import User
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    user = User(
        id=1,
        username="username_example",
        email="email_example",
        firstname="firstname_example",
        lastname="lastname_example",
        title="title_example",
        department="department_example",
        company="company_example",
        comment="comment_example",
        group_id=1,
        role_ids=[
            1,
        ],
        phone="phone_example",
        state=0,
        status=0,
        directory_id=1,
        trusted_idp_id=1,
        manager_ad_id="manager_ad_id_example",
        manager_user_id="manager_user_id_example",
        samaccount_name="samaccount_name_example",
        member_of="member_of_example",
        userprincipalname="userprincipalname_example",
        distinguished_name="distinguished_name_example",
        external_id="external_id_example",
        activated_at="activated_at_example",
        last_login="last_login_example",
        invitation_sent_at="invitation_sent_at_example",
        updated_at="updated_at_example",
        preferred_locale_code="preferred_locale_code_example",
        created_at="created_at_example",
        custom_attributes={},
        invalid_login_attempts=1,
        locked_until="locked_until_example",
        password_changed_at="password_changed_at_example",
        password="password_example",
        password_confirmation="password_confirmation_example",
        password_algorithm="password_algorithm_example",
        salt="salt_example",
    ) # User | 
    mappings = "async" # str | Controls how mappings will be applied to the user on creation. Defaults to async. (optional)
    validate_policy = True # bool | Will passwords validate against the User Policy? Defaults to true. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.create_user(authorization, user)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.create_user(authorization, user, mappings=mappings, validate_policy=validate_policy)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->create_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **user** | [**User**](User.md)|  |
 **mappings** | **str**| Controls how mappings will be applied to the user on creation. Defaults to async. | [optional]
 **validate_policy** | **bool**| Will passwords validate against the User Policy? Defaults to true. | [optional]

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
**400** | BAD REQUEST |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**422** | Indicates that the syntax of the request is good but a value supplied is not valid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_access_token_claim**
> delete_access_token_claim(authorization, id, claim_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    id = 1 # int | 
    claim_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_access_token_claim(authorization, id, claim_id)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_access_token_claim: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **id** | **int**|  |
 **claim_id** | **int**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | NO CONTENT |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app**
> delete_app(authorization, app_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    app_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_app(authorization, app_id)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_app: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **app_id** | **int**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | NO CONTENT |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app_parameter**
> delete_app_parameter(authorization, app_id, parameter_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    app_id = 1 # int | 
    parameter_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_app_parameter(authorization, app_id, parameter_id)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_app_parameter: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **app_id** | **int**|  |
 **parameter_id** | **int**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | NO CONTENT |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**403** | You attempted to delete a connector level parameter. |  -  |
**404** | Invalid ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_authorization_server**
> delete_authorization_server(authorization, id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_authorization_server(authorization, id)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_authorization_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **id** | **int**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | NO CONTENT |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_environment_variable**
> delete_environment_variable(authorization, envvar_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    envvar_id = "envvar_id_example" # str | Set to the id of the Hook Environment Variable that you want to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_environment_variable(authorization, envvar_id)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_environment_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **envvar_id** | **str**| Set to the id of the Hook Environment Variable that you want to fetch. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Success. The environment variable has been deleted. No content is returned. |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_factor**
> delete_factor(authorization, user_id, device_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    user_id = 1 # int | Set to the id of the user.
    device_id = 1 # int | Set to the device_id of the MFA device.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_factor(authorization, user_id, device_id)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_factor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **user_id** | **int**| Set to the id of the user. |
 **device_id** | **int**| Set to the device_id of the MFA device. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | NO CONTENT |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_hook**
> delete_hook(authorization, hook_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    hook_id = "hook_id_example" # str | Set to the id of the Hook that you want to return.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_hook(authorization, hook_id)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_hook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **hook_id** | **str**| Set to the id of the Hook that you want to return. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Success. The hook function has been queued for deletion. This typically happens within seconds of making the request. |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_mapping**
> delete_mapping(authorization, mapping_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    mapping_id = 1 # int | The id of the user mapping to locate.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_mapping(authorization, mapping_id)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_mapping: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **mapping_id** | **int**| The id of the user mapping to locate. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | NO CONTENT |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_risk_rule**
> RiskRule delete_risk_rule(authorization, risk_rule_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.risk_rule import RiskRule
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    risk_rule_id = "risk_rule_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.delete_risk_rule(authorization, risk_rule_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_risk_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **risk_rule_id** | **str**|  |

### Return type

[**RiskRule**](RiskRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_role**
> delete_role(authorization, role_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    role_id = 1 # int | Set to the id of the role you want to return.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_role(authorization, role_id)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **role_id** | **int**| Set to the id of the role you want to return. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | NO CONTENT |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rule**
> delete_rule(authorization, app_id, rule_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    app_id = 1 # int | 
    rule_id = 1 # int | The id of the app rule to locate.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_rule(authorization, app_id, rule_id)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **app_id** | **int**|  |
 **rule_id** | **int**| The id of the app rule to locate. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | NO CONTENT |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_scope**
> delete_scope(authorization, id, scope_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    id = 1 # int | 
    scope_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_scope(authorization, id, scope_id)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_scope: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **id** | **int**|  |
 **scope_id** | **int**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | NO CONTENT |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> delete_user(authorization, user_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    user_id = 1 # int | Set to the id of the user that you want to return.

    # example passing only required values which don't have defaults set
    try:
        api_instance.delete_user(authorization, user_id)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->delete_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **user_id** | **int**| Set to the id of the user that you want to return. |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | On success, no content is returned in the response body. |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dry_run_mapping**
> [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}] dry_run_mapping(authorization, mapping_id, request_body)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.status1 import Status1
from openapi_client.model.error_status import ErrorStatus
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    mapping_id = 1 # int | The id of the user mapping to locate.
    request_body = [
        1,
    ] # [int] | Request body is a list of user IDs tested against the mapping conditions to verify that the mapping would be applied

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.dry_run_mapping(authorization, mapping_id, request_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->dry_run_mapping: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **mapping_id** | **int**| The id of the user mapping to locate. |
 **request_body** | **[int]**| Request body is a list of user IDs tested against the mapping conditions to verify that the mapping would be applied |

### Return type

**[{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**422** | UNPROCESSABLE_ENTRY |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enroll_factor**
> [Factor] enroll_factor(authorization, user_id, enroll_factor_request)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.factor import Factor
from openapi_client.model.enroll_factor_request import EnrollFactorRequest
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    user_id = 1 # int | Set to the id of the user.
    enroll_factor_request = EnrollFactorRequest(
        factor_id=1,
        display_name="display_name_example",
        expires_in="expires_in_example",
        verified=True,
        redirect_to="redirect_to_example",
        custom_message="custom_message_example",
    ) # EnrollFactorRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.enroll_factor(authorization, user_id, enroll_factor_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->enroll_factor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **user_id** | **int**| Set to the id of the user. |
 **enroll_factor_request** | [**EnrollFactorRequest**](EnrollFactorRequest.md)|  |

### Return type

[**[Factor]**](Factor.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**201** | CREATED |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_mfa_token**
> GenerateMfaToken200Response generate_mfa_token(authorization, generate_mfa_token_request)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.generate_mfa_token200_response import GenerateMfaToken200Response
from openapi_client.model.generate_mfa_token_request import GenerateMfaTokenRequest
from openapi_client.model.status1 import Status1
from openapi_client.model.generate_mfa_token422_response import GenerateMfaToken422Response
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    generate_mfa_token_request = GenerateMfaTokenRequest(
        expires_in="expires_in_example",
        reusable=True,
    ) # GenerateMfaTokenRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_mfa_token(authorization, generate_mfa_token_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->generate_mfa_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **generate_mfa_token_request** | [**GenerateMfaTokenRequest**](GenerateMfaTokenRequest.md)|  |

### Return type

[**GenerateMfaToken200Response**](GenerateMfaToken200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**422** | The structure of the request payload is correct but it contains an invalid value. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_saml_assertion**
> generate_saml_assertion(authorization, generate_saml_assertion_request)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.generate_saml_assertion_request import GenerateSamlAssertionRequest
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    generate_saml_assertion_request = GenerateSamlAssertionRequest(
        username_or_email="username_or_email_example",
        password="password_example",
        app_id="app_id_example",
        subdomain="subdomain_example",
        ip_address="ip_address_example",
    ) # GenerateSamlAssertionRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.generate_saml_assertion(authorization, generate_saml_assertion_request)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->generate_saml_assertion: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **generate_saml_assertion_request** | [**GenerateSamlAssertionRequest**](GenerateSamlAssertionRequest.md)|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_token**
> GenerateToken200Response generate_token(authorization, generate_token_request)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.generate_token400_response import GenerateToken400Response
from openapi_client.model.generate_token200_response import GenerateToken200Response
from openapi_client.model.generate_token_request import GenerateTokenRequest
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    generate_token_request = GenerateTokenRequest(
        grant_type="client_credentials",
    ) # GenerateTokenRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.generate_token(authorization, generate_token_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->generate_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **generate_token_request** | [**GenerateTokenRequest**](GenerateTokenRequest.md)|  |

### Return type

[**GenerateToken200Response**](GenerateToken200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Typically, either grant_type value is incorrect or Authorization header is incorrectly formatted. |  -  |
**401** | Typically, this error means that your client_id and/or client_secret values are invalid. |  -  |
**404** | Typically, this error means that you are using the incorrect method. Ensure that you are making a POST. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app**
> Schema get_app(authorization, app_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.schema import Schema
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    app_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_app(authorization, app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_app: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **app_id** | **int**|  |

### Return type

[**Schema**](Schema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_authorization_server**
> GetAuthorizationServer200Response get_authorization_server(authorization, id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.get_authorization_server200_response import GetAuthorizationServer200Response
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_authorization_server(authorization, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_authorization_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **id** | **int**|  |

### Return type

[**GetAuthorizationServer200Response**](GetAuthorizationServer200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | NOT FOUND |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_available_factors**
> [GetAvailableFactors200ResponseInner] get_available_factors(authorization, user_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.get_available_factors200_response_inner import GetAvailableFactors200ResponseInner
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    user_id = 1 # int | Set to the id of the user.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_available_factors(authorization, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_available_factors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **user_id** | **int**| Set to the id of the user. |

### Return type

[**[GetAvailableFactors200ResponseInner]**](GetAvailableFactors200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_apps**
> [GetClientApps200ResponseInner] get_client_apps(authorization, id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.get_client_apps200_response_inner import GetClientApps200ResponseInner
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_client_apps(authorization, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_client_apps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **id** | **int**|  |

### Return type

[**[GetClientApps200ResponseInner]**](GetClientApps200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enrolled_factors**
> [Device] get_enrolled_factors(authorization, user_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.status1 import Status1
from openapi_client.model.device import Device
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    user_id = 1 # int | Set to the id of the user.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_enrolled_factors(authorization, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_enrolled_factors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **user_id** | **int**| Set to the id of the user. |

### Return type

[**[Device]**](Device.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_environment_variable**
> Envvar get_environment_variable(authorization, envvar_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.envvar import Envvar
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    envvar_id = "envvar_id_example" # str | Set to the id of the Hook Environment Variable that you want to fetch.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_environment_variable(authorization, envvar_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_environment_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **envvar_id** | **str**| Set to the id of the Hook Environment Variable that you want to fetch. |

### Return type

[**Envvar**](Envvar.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hook**
> Hook get_hook(authorization, hook_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.hook import Hook
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    hook_id = "hook_id_example" # str | Set to the id of the Hook that you want to return.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_hook(authorization, hook_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_hook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **hook_id** | **str**| Set to the id of the Hook that you want to return. |

### Return type

[**Hook**](Hook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_logs**
> [Log] get_logs(authorization, hook_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.log import Log
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    hook_id = "hook_id_example" # str | Set to the id of the Hook that you want to return.
    limit = 1 # int | The total number of items returned per page. The maximum limit varies between endpoints, see the relevant endpoint documentation for the specific limit. (optional)
    page = 1 # int | The page number of results to return. (optional)
    cursor = "cursor_example" # str | Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. (optional)
    request_id = "request_id_example" # str | Returns logs that contain this request_id. (optional)
    correlation_id = "correlation_id_example" # str | Returns logs that contain this correlation_id. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_logs(authorization, hook_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_logs: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_logs(authorization, hook_id, limit=limit, page=page, cursor=cursor, request_id=request_id, correlation_id=correlation_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_logs: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **hook_id** | **str**| Set to the id of the Hook that you want to return. |
 **limit** | **int**| The total number of items returned per page. The maximum limit varies between endpoints, see the relevant endpoint documentation for the specific limit. | [optional]
 **page** | **int**| The page number of results to return. | [optional]
 **cursor** | **str**| Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. | [optional]
 **request_id** | **str**| Returns logs that contain this request_id. | [optional]
 **correlation_id** | **str**| Returns logs that contain this correlation_id. | [optional]

### Return type

[**[Log]**](Log.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Current-Page -  <br>  * Page-Items -  <br>  * Total-Count -  <br>  * Total-Pages -  <br>  * Link -  <br>  * Before-Cursor -  <br>  * After-Cursor -  <br>  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_mapping**
> Mapping get_mapping(authorization, mapping_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.status1 import Status1
from openapi_client.model.mapping import Mapping
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    mapping_id = 1 # int | The id of the user mapping to locate.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_mapping(authorization, mapping_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_mapping: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **mapping_id** | **int**| The id of the user mapping to locate. |

### Return type

[**Mapping**](Mapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rate_limit**
> GetRateLimit200Response get_rate_limit(authorization)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.get_rate_limit200_response import GetRateLimit200Response
from openapi_client.model.generate_token400_response import GenerateToken400Response
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_rate_limit(authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_rate_limit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |

### Return type

[**GetRateLimit200Response**](GetRateLimit200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_risk_rule**
> get_risk_rule(authorization, risk_rule_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    risk_rule_id = "risk_rule_id_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.get_risk_rule(authorization, risk_rule_id)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_risk_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **risk_rule_id** | **str**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_risk_score**
> GetRiskScore200Response get_risk_score(authorization, get_risk_score_request)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.get_risk_score200_response import GetRiskScore200Response
from openapi_client.model.get_risk_score_request import GetRiskScoreRequest
from openapi_client.model.get_risk_score400_response import GetRiskScore400Response
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    get_risk_score_request = GetRiskScoreRequest(
        ip="ip_example",
        user_agent="user_agent_example",
        user=RiskUser(
            id="id_example",
            name="name_example",
            authenticated=False,
        ),
        source=Source(
            id="id_example",
            name="name_example",
        ),
        session=Session(
            id="id_example",
        ),
        device=RiskDevice(
            id="id_example",
        ),
        fp="fp_example",
    ) # GetRiskScoreRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_risk_score(authorization, get_risk_score_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_risk_score: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **get_risk_score_request** | [**GetRiskScoreRequest**](GetRiskScoreRequest.md)|  |

### Return type

[**GetRiskScore200Response**](GetRiskScore200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | BAD REQUEST |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role**
> Role get_role(authorization, role_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.role import Role
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    role_id = 1 # int | Set to the id of the role you want to return.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_role(authorization, role_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **role_id** | **int**| Set to the id of the role you want to return. |

### Return type

[**Role**](Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_admins**
> [Schema1] get_role_admins(authorization, role_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.status1 import Status1
from openapi_client.model.schema1 import Schema1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    role_id = 1 # int | Set to the id of the role you want to return.
    limit = 1 # int | The total number of items returned per page. The maximum limit varies between endpoints, see the relevant endpoint documentation for the specific limit. (optional)
    page = 1 # int | The page number of results to return. (optional)
    cursor = "cursor_example" # str | Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. (optional)
    name = "name_example" # str | Allows you to filter on first name, last name, username, and email address. (optional)
    include_unassigned = True # bool | Optional. Defaults to false. Include users that aren’t assigned to the role. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_role_admins(authorization, role_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_role_admins: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_role_admins(authorization, role_id, limit=limit, page=page, cursor=cursor, name=name, include_unassigned=include_unassigned)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_role_admins: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **role_id** | **int**| Set to the id of the role you want to return. |
 **limit** | **int**| The total number of items returned per page. The maximum limit varies between endpoints, see the relevant endpoint documentation for the specific limit. | [optional]
 **page** | **int**| The page number of results to return. | [optional]
 **cursor** | **str**| Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. | [optional]
 **name** | **str**| Allows you to filter on first name, last name, username, and email address. | [optional]
 **include_unassigned** | **bool**| Optional. Defaults to false. Include users that aren’t assigned to the role. | [optional]

### Return type

[**[Schema1]**](Schema1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: applcation/json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Current-Page -  <br>  * Page-Items -  <br>  * Total-Count -  <br>  * Total-Pages -  <br>  * Link -  <br>  * Before-Cursor -  <br>  * After-Cursor -  <br>  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_apps**
> [Schema] get_role_apps(authorization, role_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.schema import Schema
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    role_id = 1 # int | Set to the id of the role you want to return.
    limit = 1 # int | The total number of items returned per page. The maximum limit varies between endpoints, see the relevant endpoint documentation for the specific limit. (optional)
    page = 1 # int | The page number of results to return. (optional)
    cursor = "cursor_example" # str | Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. (optional)
    assigned = True # bool | Optional. Defaults to true. Returns all apps not yet assigned to the role. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_role_apps(authorization, role_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_role_apps: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_role_apps(authorization, role_id, limit=limit, page=page, cursor=cursor, assigned=assigned)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_role_apps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **role_id** | **int**| Set to the id of the role you want to return. |
 **limit** | **int**| The total number of items returned per page. The maximum limit varies between endpoints, see the relevant endpoint documentation for the specific limit. | [optional]
 **page** | **int**| The page number of results to return. | [optional]
 **cursor** | **str**| Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. | [optional]
 **assigned** | **bool**| Optional. Defaults to true. Returns all apps not yet assigned to the role. | [optional]

### Return type

[**[Schema]**](Schema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: applcation/json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Current-Page -  <br>  * Page-Items -  <br>  * Total-Count -  <br>  * Total-Pages -  <br>  * Link -  <br>  * Before-Cursor -  <br>  * After-Cursor -  <br>  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_role_users**
> [Schema1] get_role_users(authorization, role_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.status1 import Status1
from openapi_client.model.schema1 import Schema1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    role_id = 1 # int | Set to the id of the role you want to return.
    limit = 1 # int | The total number of items returned per page. The maximum limit varies between endpoints, see the relevant endpoint documentation for the specific limit. (optional)
    page = 1 # int | The page number of results to return. (optional)
    cursor = "cursor_example" # str | Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. (optional)
    name = "name_example" # str | Allows you to filter on first name, last name, username, and email address. (optional)
    include_unassigned = True # bool | Optional. Defaults to false. Include users that aren’t assigned to the role. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_role_users(authorization, role_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_role_users: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_role_users(authorization, role_id, limit=limit, page=page, cursor=cursor, name=name, include_unassigned=include_unassigned)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_role_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **role_id** | **int**| Set to the id of the role you want to return. |
 **limit** | **int**| The total number of items returned per page. The maximum limit varies between endpoints, see the relevant endpoint documentation for the specific limit. | [optional]
 **page** | **int**| The page number of results to return. | [optional]
 **cursor** | **str**| Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. | [optional]
 **name** | **str**| Allows you to filter on first name, last name, username, and email address. | [optional]
 **include_unassigned** | **bool**| Optional. Defaults to false. Include users that aren’t assigned to the role. | [optional]

### Return type

[**[Schema1]**](Schema1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: applcation/json, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Current-Page -  <br>  * Page-Items -  <br>  * Total-Count -  <br>  * Total-Pages -  <br>  * Link -  <br>  * Before-Cursor -  <br>  * After-Cursor -  <br>  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rule**
> Rule get_rule(authorization, app_id, rule_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.rule import Rule
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    app_id = 1 # int | 
    rule_id = 1 # int | The id of the app rule to locate.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_rule(authorization, app_id, rule_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **app_id** | **int**|  |
 **rule_id** | **int**| The id of the app rule to locate. |

### Return type

[**Rule**](Rule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_score_insights**
> GetScoreInsights200Response get_score_insights(authorization)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.get_score_insights200_response import GetScoreInsights200Response
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    before = "before_example" # str | Optional ISO8601 formatted date string. Defaults to current date. Maximum date is 90 days ago. (optional)
    after = "after_example" # str | Optional ISO8601 formatted date string. Defaults to 30 days ago. Maximum date is 90 days ago. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_score_insights(authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_score_insights: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_score_insights(authorization, before=before, after=after)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_score_insights: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **before** | **str**| Optional ISO8601 formatted date string. Defaults to current date. Maximum date is 90 days ago. | [optional]
 **after** | **str**| Optional ISO8601 formatted date string. Defaults to 30 days ago. Maximum date is 90 days ago. | [optional]

### Return type

[**GetScoreInsights200Response**](GetScoreInsights200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Invalid Access Token |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> User get_user(authorization, user_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.user import User
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    user_id = 1 # int | Set to the id of the user that you want to return.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_user(authorization, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **user_id** | **int**| Set to the id of the user that you want to return. |

### Return type

[**User**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_apps**
> [GetUserApps200ResponseInner] get_user_apps(authorization, user_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.get_user_apps200_response_inner import GetUserApps200ResponseInner
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    user_id = 1 # int | Set to the id of the user that you want to return.
    ignore_visibility = True # bool | Defaults to `false`. When `true` will show all apps that are assigned to a user regardless of their portal visibility setting. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_user_apps(authorization, user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_user_apps: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_user_apps(authorization, user_id, ignore_visibility=ignore_visibility)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_user_apps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **user_id** | **int**| Set to the id of the user that you want to return. |
 **ignore_visibility** | **bool**| Defaults to &#x60;false&#x60;. When &#x60;true&#x60; will show all apps that are assigned to a user regardless of their portal visibility setting. | [optional]

### Return type

[**[GetUserApps200ResponseInner]**](GetUserApps200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_access_token_claims**
> [ListAccessTokenClaims200ResponseInner] list_access_token_claims(authorization, id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.list_access_token_claims200_response_inner import ListAccessTokenClaims200ResponseInner
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_access_token_claims(authorization, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_access_token_claims: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **id** | **int**|  |

### Return type

[**[ListAccessTokenClaims200ResponseInner]**](ListAccessTokenClaims200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_action_values**
> [ListConditionValues200ResponseInner] list_action_values(authorization, app_id, action_value)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.list_condition_values200_response_inner import ListConditionValues200ResponseInner
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    app_id = 1 # int | 
    action_value = "action_value_example" # str | The value for the selected action.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_action_values(authorization, app_id, action_value)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_action_values: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **app_id** | **int**|  |
 **action_value** | **str**| The value for the selected action. |

### Return type

[**[ListConditionValues200ResponseInner]**](ListConditionValues200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_actions**
> [ListActions200ResponseInner] list_actions(authorization, app_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.status1 import Status1
from openapi_client.model.list_actions200_response_inner import ListActions200ResponseInner
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    app_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_actions(authorization, app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_actions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **app_id** | **int**|  |

### Return type

[**[ListActions200ResponseInner]**](ListActions200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_app_users**
> [ListAppUsers200ResponseInner] list_app_users(authorization, app_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.status1 import Status1
from openapi_client.model.list_app_users200_response_inner import ListAppUsers200ResponseInner
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    app_id = 1 # int | 
    limit = 1 # int | The total number of items returned per page. The maximum limit varies between endpoints, see the relevant endpoint documentation for the specific limit. (optional)
    page = 1 # int | The page number of results to return. (optional)
    cursor = "cursor_example" # str | Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_app_users(authorization, app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_app_users: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_app_users(authorization, app_id, limit=limit, page=page, cursor=cursor)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_app_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **app_id** | **int**|  |
 **limit** | **int**| The total number of items returned per page. The maximum limit varies between endpoints, see the relevant endpoint documentation for the specific limit. | [optional]
 **page** | **int**| The page number of results to return. | [optional]
 **cursor** | **str**| Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. | [optional]

### Return type

[**[ListAppUsers200ResponseInner]**](ListAppUsers200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Current-Page -  <br>  * Page-Items -  <br>  * Total-Count -  <br>  * Total-Pages -  <br>  * Link -  <br>  * Before-Cursor -  <br>  * After-Cursor -  <br>  |
**401** | Typically, this error means that your access token value is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_apps**
> [Schema] list_apps(authorization)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.schema import Schema
from openapi_client.model.auth_method import AuthMethod
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    limit = 1 # int | The total number of items returned per page. The maximum limit varies between endpoints, see the relevant endpoint documentation for the specific limit. (optional)
    page = 1 # int | The page number of results to return. (optional)
    cursor = "cursor_example" # str | Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. (optional)
    name = "name_example" # str | The name or partial name of the app to search for. When using a partial name you must append a wildcard `*` (optional)
    connector_id = 1 # int | Returns all apps based off a specific connector. See List Connectors for a complete list of Connector IDs. (optional)
    auth_method = AuthMethod(0) # AuthMethod | Returns all apps based of a given type. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_apps(authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_apps: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_apps(authorization, limit=limit, page=page, cursor=cursor, name=name, connector_id=connector_id, auth_method=auth_method)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_apps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **limit** | **int**| The total number of items returned per page. The maximum limit varies between endpoints, see the relevant endpoint documentation for the specific limit. | [optional]
 **page** | **int**| The page number of results to return. | [optional]
 **cursor** | **str**| Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. | [optional]
 **name** | **str**| The name or partial name of the app to search for. When using a partial name you must append a wildcard &#x60;*&#x60; | [optional]
 **connector_id** | **int**| Returns all apps based off a specific connector. See List Connectors for a complete list of Connector IDs. | [optional]
 **auth_method** | **AuthMethod**| Returns all apps based of a given type. | [optional]

### Return type

[**[Schema]**](Schema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Current-Page -  <br>  * Page-Items -  <br>  * Total-Count -  <br>  * Total-Pages -  <br>  * Link -  <br>  * Before-Cursor -  <br>  * After-Cursor -  <br>  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**422** | Indicates that the syntax of the request is good but a value supplied is not valid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_authorization_servers**
> [ListAuthorizationServers200ResponseInner] list_authorization_servers(authorization)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.list_authorization_servers200_response_inner import ListAuthorizationServers200ResponseInner
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_authorization_servers(authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_authorization_servers: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |

### Return type

[**[ListAuthorizationServers200ResponseInner]**](ListAuthorizationServers200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_condition_operators**
> [ListConditionOperators200ResponseInner] list_condition_operators(authorization, app_id, condition_value)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.status1 import Status1
from openapi_client.model.list_condition_operators200_response_inner import ListConditionOperators200ResponseInner
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    app_id = 1 # int | 
    condition_value = "condition_value_example" # str | The value for the selected condition.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_condition_operators(authorization, app_id, condition_value)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_condition_operators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **app_id** | **int**|  |
 **condition_value** | **str**| The value for the selected condition. |

### Return type

[**[ListConditionOperators200ResponseInner]**](ListConditionOperators200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_condition_values**
> [ListConditionValues200ResponseInner] list_condition_values(authorization, app_id, condition_value)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.list_condition_values200_response_inner import ListConditionValues200ResponseInner
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    app_id = 1 # int | 
    condition_value = "condition_value_example" # str | The value for the selected condition.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_condition_values(authorization, app_id, condition_value)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_condition_values: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **app_id** | **int**|  |
 **condition_value** | **str**| The value for the selected condition. |

### Return type

[**[ListConditionValues200ResponseInner]**](ListConditionValues200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_conditions**
> [ListConditions200ResponseInner] list_conditions(authorization, app_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.list_conditions200_response_inner import ListConditions200ResponseInner
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    app_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_conditions(authorization, app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_conditions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **app_id** | **int**|  |

### Return type

[**[ListConditions200ResponseInner]**](ListConditions200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_connectors**
> [Connector] list_connectors(authorization)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.auth_method import AuthMethod
from openapi_client.model.status1 import Status1
from openapi_client.model.connector import Connector
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    limit = 1 # int | The total number of items returned per page. The maximum limit varies between endpoints, see the relevant endpoint documentation for the specific limit. (optional)
    page = 1 # int | The page number of results to return. (optional)
    cursor = "cursor_example" # str | Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. (optional)
    name = "name_example" # str | The name or partial name of the connector to search for. When using a partial name you must append a wildcard `*` (optional)
    auth_method = AuthMethod(0) # AuthMethod | Returns all connectors of a given type. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_connectors(authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_connectors: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_connectors(authorization, limit=limit, page=page, cursor=cursor, name=name, auth_method=auth_method)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_connectors: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **limit** | **int**| The total number of items returned per page. The maximum limit varies between endpoints, see the relevant endpoint documentation for the specific limit. | [optional]
 **page** | **int**| The page number of results to return. | [optional]
 **cursor** | **str**| Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. | [optional]
 **name** | **str**| The name or partial name of the connector to search for. When using a partial name you must append a wildcard &#x60;*&#x60; | [optional]
 **auth_method** | **AuthMethod**| Returns all connectors of a given type. | [optional]

### Return type

[**[Connector]**](Connector.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Current-Page -  <br>  * Page-Items -  <br>  * Total-Count -  <br>  * Total-Pages -  <br>  * Link -  <br>  * Before-Cursor -  <br>  * After-Cursor -  <br>  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**422** | Indicates that the syntax of the request is good but a value supplied is not valid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_environment_variables**
> [Envvar] list_environment_variables(authorization)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.envvar import Envvar
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    limit = 1 # int | The total number of items returned per page. The maximum limit varies between endpoints, see the relevant endpoint documentation for the specific limit. (optional)
    page = 1 # int | The page number of results to return. (optional)
    cursor = "cursor_example" # str | Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_environment_variables(authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_environment_variables: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_environment_variables(authorization, limit=limit, page=page, cursor=cursor)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_environment_variables: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **limit** | **int**| The total number of items returned per page. The maximum limit varies between endpoints, see the relevant endpoint documentation for the specific limit. | [optional]
 **page** | **int**| The page number of results to return. | [optional]
 **cursor** | **str**| Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. | [optional]

### Return type

[**[Envvar]**](Envvar.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Current-Page -  <br>  * Page-Items -  <br>  * Total-Count -  <br>  * Total-Pages -  <br>  * Link -  <br>  * Before-Cursor -  <br>  * After-Cursor -  <br>  |
**401** | Typically, this error means that your access token value is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_hooks**
> [Hook] list_hooks(authorization)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.hook import Hook
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    limit = 1 # int | The total number of items returned per page. The maximum limit varies between endpoints, see the relevant endpoint documentation for the specific limit. (optional)
    page = 1 # int | The page number of results to return. (optional)
    cursor = "cursor_example" # str | Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_hooks(authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_hooks: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_hooks(authorization, limit=limit, page=page, cursor=cursor)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_hooks: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **limit** | **int**| The total number of items returned per page. The maximum limit varies between endpoints, see the relevant endpoint documentation for the specific limit. | [optional]
 **page** | **int**| The page number of results to return. | [optional]
 **cursor** | **str**| Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. | [optional]

### Return type

[**[Hook]**](Hook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Current-Page -  <br>  * Page-Items -  <br>  * Total-Count -  <br>  * Total-Pages -  <br>  * Link -  <br>  * Before-Cursor -  <br>  * After-Cursor -  <br>  |
**401** | Typically, this error means that your access token value is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mapping_action_values**
> [ListConditionValues200ResponseInner] list_mapping_action_values(authorization, action_value)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.list_condition_values200_response_inner import ListConditionValues200ResponseInner
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    action_value = "action_value_example" # str | The value for the selected action.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_mapping_action_values(authorization, action_value)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_mapping_action_values: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **action_value** | **str**| The value for the selected action. |

### Return type

[**[ListConditionValues200ResponseInner]**](ListConditionValues200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mapping_actions**
> [ListActions200ResponseInner] list_mapping_actions(authorization)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.status1 import Status1
from openapi_client.model.list_actions200_response_inner import ListActions200ResponseInner
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_mapping_actions(authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_mapping_actions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |

### Return type

[**[ListActions200ResponseInner]**](ListActions200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mapping_condition_operators**
> [ListMappingConditionOperators200ResponseInner] list_mapping_condition_operators(authorization, condition_value)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.list_mapping_condition_operators200_response_inner import ListMappingConditionOperators200ResponseInner
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    condition_value = "condition_value_example" # str | The value for the selected condition.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_mapping_condition_operators(authorization, condition_value)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_mapping_condition_operators: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **condition_value** | **str**| The value for the selected condition. |

### Return type

[**[ListMappingConditionOperators200ResponseInner]**](ListMappingConditionOperators200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mapping_condition_values**
> [ListConditionValues200ResponseInner] list_mapping_condition_values(authorization, condition_value)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.list_condition_values200_response_inner import ListConditionValues200ResponseInner
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    condition_value = "condition_value_example" # str | The value for the selected condition.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_mapping_condition_values(authorization, condition_value)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_mapping_condition_values: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **condition_value** | **str**| The value for the selected condition. |

### Return type

[**[ListConditionValues200ResponseInner]**](ListConditionValues200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mapping_conditions**
> [ListMappingConditions200ResponseInner] list_mapping_conditions(authorization)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.status1 import Status1
from openapi_client.model.list_mapping_conditions200_response_inner import ListMappingConditions200ResponseInner
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_mapping_conditions(authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_mapping_conditions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |

### Return type

[**[ListMappingConditions200ResponseInner]**](ListMappingConditions200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_mappings**
> [Mapping] list_mappings(authorization)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.status1 import Status1
from openapi_client.model.mapping import Mapping
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    enabled = True # bool | Defaults to true. When set to `false` will return all disabled mappings. (optional) if omitted the server will use the default value of True
    has_condition = "has_condition=has_role:123456,status:1" # str | Filters Mappings based on their Conditions. (optional)
    has_condition_type = "builtin" # str | Filters Mappings based on their condition types. (optional)
    has_action = "has_action=set_groups:123456,set_usertype:*" # str | Filters Mappings based on their Actions. (optional)
    has_action_type = "builtin" # str | Filters Mappings based on their action types. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_mappings(authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_mappings: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_mappings(authorization, enabled=enabled, has_condition=has_condition, has_condition_type=has_condition_type, has_action=has_action, has_action_type=has_action_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_mappings: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **enabled** | **bool**| Defaults to true. When set to &#x60;false&#x60; will return all disabled mappings. | [optional] if omitted the server will use the default value of True
 **has_condition** | **str**| Filters Mappings based on their Conditions. | [optional]
 **has_condition_type** | **str**| Filters Mappings based on their condition types. | [optional]
 **has_action** | **str**| Filters Mappings based on their Actions. | [optional]
 **has_action_type** | **str**| Filters Mappings based on their action types. | [optional]

### Return type

[**[Mapping]**](Mapping.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_risk_rules**
> list_risk_rules(authorization)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.list_risk_rules(authorization)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_risk_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_roles**
> [Role] list_roles(authorization)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.role import Role
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    limit = 1 # int | The total number of items returned per page. The maximum limit varies between endpoints, see the relevant endpoint documentation for the specific limit. (optional)
    page = 1 # int | The page number of results to return. (optional)
    cursor = "cursor_example" # str | Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. (optional)
    name = "name_example" # str | Optional. Filters by role name. (optional)
    app_id = "app_id_example" # str | Optional. Returns roles that contain this app name. (optional)
    fields = "apps" # str | Optional. Comma delimited list of fields to return. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_roles(authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_roles: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_roles(authorization, limit=limit, page=page, cursor=cursor, name=name, app_id=app_id, fields=fields)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_roles: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **limit** | **int**| The total number of items returned per page. The maximum limit varies between endpoints, see the relevant endpoint documentation for the specific limit. | [optional]
 **page** | **int**| The page number of results to return. | [optional]
 **cursor** | **str**| Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. | [optional]
 **name** | **str**| Optional. Filters by role name. | [optional]
 **app_id** | **str**| Optional. Returns roles that contain this app name. | [optional]
 **fields** | **str**| Optional. Comma delimited list of fields to return. | [optional]

### Return type

[**[Role]**](Role.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Current-Page -  <br>  * Page-Items -  <br>  * Total-Count -  <br>  * Total-Pages -  <br>  * Link -  <br>  * Before-Cursor -  <br>  * After-Cursor -  <br>  |
**401** | Typically, this error means that your access token value is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_rules**
> [Rule] list_rules(authorization, app_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.rule import Rule
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    app_id = 1 # int | 
    enabled = True # bool | Defaults to true. When set to `false` will return all disabled rules. (optional)
    has_condition = "has_condition_example" # str | Filters Rules based on their Conditions. (optional)
    has_condition_type = "has_condition_type_example" # str | Filters Rules based on their condition types. (optional)
    has_action = "has_action_example" # str | Filters Rules based on their Actions. (optional)
    has_action_type = "has_action_type_example" # str | Filters Rules based on their action types. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_rules(authorization, app_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_rules: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_rules(authorization, app_id, enabled=enabled, has_condition=has_condition, has_condition_type=has_condition_type, has_action=has_action, has_action_type=has_action_type)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_rules: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **app_id** | **int**|  |
 **enabled** | **bool**| Defaults to true. When set to &#x60;false&#x60; will return all disabled rules. | [optional]
 **has_condition** | **str**| Filters Rules based on their Conditions. | [optional]
 **has_condition_type** | **str**| Filters Rules based on their condition types. | [optional]
 **has_action** | **str**| Filters Rules based on their Actions. | [optional]
 **has_action_type** | **str**| Filters Rules based on their action types. | [optional]

### Return type

[**[Rule]**](Rule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_scopes**
> [ListScopes200ResponseInner] list_scopes(authorization, id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.status1 import Status1
from openapi_client.model.list_scopes200_response_inner import ListScopes200ResponseInner
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_scopes(authorization, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_scopes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **id** | **int**|  |

### Return type

[**[ListScopes200ResponseInner]**](ListScopes200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users**
> [User] list_users(authorization)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.user import User
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    limit = 1 # int | The total number of items returned per page. The maximum limit varies between endpoints, see the relevant endpoint documentation for the specific limit. (optional)
    page = 1 # int | The page number of results to return. (optional)
    cursor = "cursor_example" # str | Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. (optional)
    created_since = "created_since_example" # str | An ISO8601 timestamp value that returns all users created after a given date & time. (optional)
    created_until = "created_until_example" # str | An ISO8601 timestamp value that returns all users created before a given date & time. (optional)
    updated_since = "updated_since_example" # str | An ISO8601 timestamp value that returns all users updated after a given date & time. (optional)
    updated_until = "updated_until_example" # str | An ISO8601 timestamp value that returns all users updated before a given date & time. (optional)
    last_login_since = "last_login_since_example" # str | An ISO8601 timestamp value that returns all users that logged in after a given date & time. (optional)
    last_login_until = "last_login_until_example" # str |  (optional)
    firstname = "firstname_example" # str | The first name of the user (optional)
    lastname = "lastname_example" # str | The last name of the user (optional)
    email = "email_example" # str | The email address of the user (optional)
    username = "username_example" # str | The username for the user (optional)
    samaccountname = "samaccountname_example" # str | The AD login name for the user (optional)
    directory_id = "directory_id_example" # str | The ID in OneLogin of the Directory that the user belongs to (optional)
    external_id = "external_id_example" # str | An external identifier that has been set on the user (optional)
    app_id = "app_id_example" # str | The ID of a OneLogin Application (optional)
    user_ids = "user_ids_example" # str | A comma separated list of OneLogin User IDs (optional)
    custom_attributes_attribute_name = "custom_attributes.{attribute_name}_example" # str | The short name of a custom attribute. Note that the attribute name is prefixed with custom_attributes. (optional)
    fields = "fields_example" # str | A comma separated list user attributes to return. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.list_users(authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_users: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.list_users(authorization, limit=limit, page=page, cursor=cursor, created_since=created_since, created_until=created_until, updated_since=updated_since, updated_until=updated_until, last_login_since=last_login_since, last_login_until=last_login_until, firstname=firstname, lastname=lastname, email=email, username=username, samaccountname=samaccountname, directory_id=directory_id, external_id=external_id, app_id=app_id, user_ids=user_ids, custom_attributes_attribute_name=custom_attributes_attribute_name, fields=fields)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->list_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **limit** | **int**| The total number of items returned per page. The maximum limit varies between endpoints, see the relevant endpoint documentation for the specific limit. | [optional]
 **page** | **int**| The page number of results to return. | [optional]
 **cursor** | **str**| Set to the value extracted from Before-Cursor or After-Cursor headers to return the previous or next page. | [optional]
 **created_since** | **str**| An ISO8601 timestamp value that returns all users created after a given date &amp; time. | [optional]
 **created_until** | **str**| An ISO8601 timestamp value that returns all users created before a given date &amp; time. | [optional]
 **updated_since** | **str**| An ISO8601 timestamp value that returns all users updated after a given date &amp; time. | [optional]
 **updated_until** | **str**| An ISO8601 timestamp value that returns all users updated before a given date &amp; time. | [optional]
 **last_login_since** | **str**| An ISO8601 timestamp value that returns all users that logged in after a given date &amp; time. | [optional]
 **last_login_until** | **str**|  | [optional]
 **firstname** | **str**| The first name of the user | [optional]
 **lastname** | **str**| The last name of the user | [optional]
 **email** | **str**| The email address of the user | [optional]
 **username** | **str**| The username for the user | [optional]
 **samaccountname** | **str**| The AD login name for the user | [optional]
 **directory_id** | **str**| The ID in OneLogin of the Directory that the user belongs to | [optional]
 **external_id** | **str**| An external identifier that has been set on the user | [optional]
 **app_id** | **str**| The ID of a OneLogin Application | [optional]
 **user_ids** | **str**| A comma separated list of OneLogin User IDs | [optional]
 **custom_attributes_attribute_name** | **str**| The short name of a custom attribute. Note that the attribute name is prefixed with custom_attributes. | [optional]
 **fields** | **str**| A comma separated list user attributes to return. | [optional]

### Return type

[**[User]**](User.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Current-Page -  <br>  * Page-Items -  <br>  * Total-Count -  <br>  * Total-Pages -  <br>  * Link -  <br>  * Before-Cursor -  <br>  * After-Cursor -  <br>  |
**400** | An invalid search parameter was used. |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**422** | You cant sort on this field. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_client_app**
> remove_client_app(authorization, id, client_app_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    id = 1 # int | 
    client_app_id = 1 # int | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.remove_client_app(authorization, id, client_app_id)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->remove_client_app: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **id** | **int**|  |
 **client_app_id** | **int**|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | NO CONTENT |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**422** | Indicates that the syntax of the request is good but a value supplied is not valid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_role_admins**
> remove_role_admins(authorization, role_id, remove_role_users_request)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.status1 import Status1
from openapi_client.model.remove_role_users_request import RemoveRoleUsersRequest
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    role_id = 1 # int | Set to the id of the role you want to return.
    remove_role_users_request = RemoveRoleUsersRequest(
        user_id=[
            1,
        ],
    ) # RemoveRoleUsersRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.remove_role_admins(authorization, role_id, remove_role_users_request)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->remove_role_admins: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **role_id** | **int**| Set to the id of the role you want to return. |
 **remove_role_users_request** | [**RemoveRoleUsersRequest**](RemoveRoleUsersRequest.md)|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | NO CONTENT |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_role_users**
> remove_role_users(authorization, role_id, remove_role_users_request)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.status1 import Status1
from openapi_client.model.remove_role_users_request import RemoveRoleUsersRequest
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    role_id = 1 # int | Set to the id of the role you want to return.
    remove_role_users_request = RemoveRoleUsersRequest(
        user_id=[
            1,
        ],
    ) # RemoveRoleUsersRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.remove_role_users(authorization, role_id, remove_role_users_request)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->remove_role_users: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **role_id** | **int**| Set to the id of the role you want to return. |
 **remove_role_users_request** | [**RemoveRoleUsersRequest**](RemoveRoleUsersRequest.md)|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | NO CONTENT |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_token**
> GenerateToken400Response revoke_token(authorization)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.generate_token400_response import GenerateToken400Response
from openapi_client.model.revoke_token_request import RevokeTokenRequest
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    revoke_token_request = RevokeTokenRequest(
        access_token="access_token_example",
    ) # RevokeTokenRequest |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.revoke_token(authorization)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->revoke_token: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.revoke_token(authorization, revoke_token_request=revoke_token_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->revoke_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **revoke_token_request** | [**RevokeTokenRequest**](RevokeTokenRequest.md)|  | [optional]

### Return type

[**GenerateToken400Response**](GenerateToken400Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Possibly, the Authorization header is incorrectly formatted. |  -  |
**401** | Typically, this error means that your client_id and/or client_secret values are invalid. |  -  |
**404** | Typically, this error means that you are using the incorrect method. Ensure that you are making a POST. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_role_apps**
> [SetRoleApps200ResponseInner] set_role_apps(authorization, role_id, request_body)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.set_role_apps200_response_inner import SetRoleApps200ResponseInner
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    role_id = 1 # int | Set to the id of the role you want to return.
    request_body = [
        1,
    ] # [int] | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.set_role_apps(authorization, role_id, request_body)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->set_role_apps: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **role_id** | **int**| Set to the id of the role you want to return. |
 **request_body** | **[int]**|  |

### Return type

[**[SetRoleApps200ResponseInner]**](SetRoleApps200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The response returns an array of app IDs sent in the request. |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **track_event**
> track_event(authorization, track_event_request)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.track_event_request import TrackEventRequest
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    track_event_request = TrackEventRequest(
        verb="verb_example",
        ip="ip_example",
        user_agent="user_agent_example",
        user=RiskUser(
            id="id_example",
            name="name_example",
            authenticated=False,
        ),
        source=Source(
            id="id_example",
            name="name_example",
        ),
        session=Session(
            id="id_example",
        ),
        device=RiskDevice(
            id="id_example",
        ),
        fp="fp_example",
        published="published_example",
    ) # TrackEventRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_instance.track_event(authorization, track_event_request)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->track_event: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **track_event_request** | [**TrackEventRequest**](TrackEventRequest.md)|  |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | No content is returned. This API is fire and forget. |  -  |
**400** | BAD REQUEST |  -  |
**401** | Invalid API Key |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_access_token_claim**
> Id update_access_token_claim(authorization, id, claim_id, add_access_token_claim_request)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.add_access_token_claim_request import AddAccessTokenClaimRequest
from openapi_client.model.status1 import Status1
from openapi_client.model.id import Id
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    id = 1 # int | 
    claim_id = 1 # int | 
    add_access_token_claim_request = AddAccessTokenClaimRequest(
        name="name_example",
        user_attribute_mappings="user_attribute_mappings_example",
        user_attribute_macros="user_attribute_macros_example",
    ) # AddAccessTokenClaimRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_access_token_claim(authorization, id, claim_id, add_access_token_claim_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_access_token_claim: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **id** | **int**|  |
 **claim_id** | **int**|  |
 **add_access_token_claim_request** | [**AddAccessTokenClaimRequest**](AddAccessTokenClaimRequest.md)|  |

### Return type

[**Id**](Id.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |
**422** | This name already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app**
> Schema update_app(authorization, app_id, schema)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.schema import Schema
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    app_id = 1 # int | 
    schema = Schema(
        id=1,
        connector_id=1,
        name="name_example",
        description="description_example",
        notes="notes_example",
        policy_id=1,
        brand_id=1,
        icon_url="icon_url_example",
        visible=True,
        auth_method=0,
        tab_id=1,
        created_at="created_at_example",
        updated_at="updated_at_example",
        role_ids=[
            1,
        ],
        allow_assumed_signin=True,
        provisioning=SchemaProvisioning(
            enabled=True,
        ),
        sso={},
        configuration={},
        parameters={},
        enforcement_point={},
    ) # Schema | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_app(authorization, app_id, schema)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_app: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **app_id** | **int**|  |
 **schema** | [**Schema**](Schema.md)|  |

### Return type

[**Schema**](Schema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**422** | Indicates that the syntax of the request is good but a value supplied is not valid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_authorization_server**
> Id update_authorization_server(authorization, id, create_authorization_server_request)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.create_authorization_server_request import CreateAuthorizationServerRequest
from openapi_client.model.status1 import Status1
from openapi_client.model.update_authorization_server400_response import UpdateAuthorizationServer400Response
from openapi_client.model.id import Id
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    id = 1 # int | 
    create_authorization_server_request = CreateAuthorizationServerRequest(
        name="name_example",
        description="description_example",
        configuration=AuthServerConfiguration(
            audiences=[
                "audiences_example",
            ],
            refresh_token_expiration_minutes=1,
            resource_identifier="resource_identifier_example",
            access_token_expiration_minutes=1,
        ),
    ) # CreateAuthorizationServerRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_authorization_server(authorization, id, create_authorization_server_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_authorization_server: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **id** | **int**|  |
 **create_authorization_server_request** | [**CreateAuthorizationServerRequest**](CreateAuthorizationServerRequest.md)|  |

### Return type

[**Id**](Id.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | You need to submit all of the attributes |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**422** | Indicates that the syntax of the request is good but a value supplied is not valid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_app**
> ClientApp update_client_app(authorization, id, client_app_id, update_client_app_request)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.update_client_app_request import UpdateClientAppRequest
from openapi_client.model.client_app import ClientApp
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    id = 1 # int | 
    client_app_id = 1 # int | 
    update_client_app_request = UpdateClientAppRequest(
        scopes=[
            1,
        ],
    ) # UpdateClientAppRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_client_app(authorization, id, client_app_id, update_client_app_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_client_app: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **id** | **int**|  |
 **client_app_id** | **int**|  |
 **update_client_app_request** | [**UpdateClientAppRequest**](UpdateClientAppRequest.md)|  |

### Return type

[**ClientApp**](ClientApp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |
**422** | An invalid scope id has been provided |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_environment_variable**
> Envvar update_environment_variable(authorization, envvar_id, update_environment_variable_request)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.update_environment_variable_request import UpdateEnvironmentVariableRequest
from openapi_client.model.hook_status import HookStatus
from openapi_client.model.envvar import Envvar
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    envvar_id = "envvar_id_example" # str | Set to the id of the Hook Environment Variable that you want to fetch.
    update_environment_variable_request = UpdateEnvironmentVariableRequest(
        value="value_example",
    ) # UpdateEnvironmentVariableRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_environment_variable(authorization, envvar_id, update_environment_variable_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_environment_variable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **envvar_id** | **str**| Set to the id of the Hook Environment Variable that you want to fetch. |
 **update_environment_variable_request** | [**UpdateEnvironmentVariableRequest**](UpdateEnvironmentVariableRequest.md)|  |

### Return type

[**Envvar**](Envvar.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | BAD REQUEST |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**422** | The name of a var can not be changed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_hook**
> Hook update_hook(authorization, hook_id, hook)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.hook_status import HookStatus
from openapi_client.model.hook import Hook
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    hook_id = "hook_id_example" # str | Set to the id of the Hook that you want to return.
    hook = Hook(
        id="id_example",
        type="type_example",
        disabled=True,
        timeout=1,
        env_vars=[
            "env_vars_example",
        ],
        runtime="runtime_example",
        retries=0,
        packages={},
        function="function_example",
        context_version="context_version_example",
        status="ready",
        options=HookOptions(
            risk_enabled=True,
            location_enabled=True,
            mfa_device_info_enabled=True,
        ),
        conditions=[
            HookConditionsInner(
                source="source_example",
                operator="operator_example",
                value="value_example",
            ),
        ],
        created_at="created_at_example",
        updated_at="updated_at_example",
    ) # Hook | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_hook(authorization, hook_id, hook)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_hook: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **hook_id** | **str**| Set to the id of the Hook that you want to return. |
 **hook** | [**Hook**](Hook.md)|  |

### Return type

[**Hook**](Hook.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**422** | You function is not base64 encoded. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_mapping**
> int update_mapping(authorization, mapping_id, mapping)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.status1 import Status1
from openapi_client.model.error_status import ErrorStatus
from openapi_client.model.mapping import Mapping
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    mapping_id = 1 # int | The id of the user mapping to locate.
    mapping = Mapping(
        id=1,
        name="name_example",
        enabled=True,
        match="all",
        position=1,
        conditions=[
            Condition(
                source="source_example",
                operator="operator_example",
                value="value_example",
            ),
        ],
        actions=[
            Action(
                action="action_example",
                value=[
                    "value_example",
                ],
                expression="expression_example",
                scriplet="scriplet_example",
                macro="macro_example",
            ),
        ],
    ) # Mapping | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_mapping(authorization, mapping_id, mapping)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_mapping: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **mapping_id** | **int**| The id of the user mapping to locate. |
 **mapping** | [**Mapping**](Mapping.md)|  |

### Return type

**int**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**422** | UNPROCESSABLE_ENTRY |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_risk_rule**
> RiskRule update_risk_rule(authorization, risk_rule_id, risk_rule)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.risk_rule import RiskRule
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    risk_rule_id = "risk_rule_id_example" # str | 
    risk_rule = RiskRule(
        id="id_example",
        name="name_example",
        description="description_example",
        type="blacklist",
        target="location.ip",
        filters=[
            "filters_example",
        ],
        source=Source(
            id="id_example",
            name="name_example",
        ),
    ) # RiskRule | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_risk_rule(authorization, risk_rule_id, risk_rule)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_risk_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **risk_rule_id** | **str**|  |
 **risk_rule** | [**RiskRule**](RiskRule.md)|  |

### Return type

[**RiskRule**](RiskRule.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | BAD REQUEST |  -  |
**401** | UNAUTHORIZED |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_role**
> UpdateRole200Response update_role(authorization, role_id, role)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.role import Role
from openapi_client.model.update_role200_response import UpdateRole200Response
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    role_id = 1 # int | Set to the id of the role you want to return.
    role = Role(
        id=1,
        name="name_example",
        apps=[
            1,
        ],
        users=[
            1,
        ],
        admins=[
            1,
        ],
    ) # Role | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_role(authorization, role_id, role)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_role: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **role_id** | **int**| Set to the id of the role you want to return. |
 **role** | [**Role**](Role.md)|  |

### Return type

[**UpdateRole200Response**](UpdateRole200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**422** | Indicates that the syntax of the request is good but a value supplied is not valid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rule**
> RuleId update_rule(authorization, app_id, rule_id, rule)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.rule_id import RuleId
from openapi_client.model.rule import Rule
from openapi_client.model.status1 import Status1
from openapi_client.model.error_status import ErrorStatus
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    app_id = 1 # int | 
    rule_id = 1 # int | The id of the app rule to locate.
    rule = Rule(
        id=1,
        name="name_example",
        match="all",
        enabled=True,
        position=1,
        conditions=[
            Condition(
                source="source_example",
                operator="operator_example",
                value="value_example",
            ),
        ],
        actions=[
            Action(
                action="action_example",
                value=[
                    "value_example",
                ],
                expression="expression_example",
                scriplet="scriplet_example",
                macro="macro_example",
            ),
        ],
    ) # Rule | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_rule(authorization, app_id, rule_id, rule)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_rule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **app_id** | **int**|  |
 **rule_id** | **int**| The id of the app rule to locate. |
 **rule** | [**Rule**](Rule.md)|  |

### Return type

[**RuleId**](RuleId.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**422** | ID should not be included in the payload body. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_scope**
> Id update_scope(authorization, id, scope_id, add_scope_request)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.add_scope_request import AddScopeRequest
from openapi_client.model.status1 import Status1
from openapi_client.model.id import Id
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    id = 1 # int | 
    scope_id = 1 # int | 
    add_scope_request = AddScopeRequest(
        value="value_example",
        description="description_example",
    ) # AddScopeRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_scope(authorization, id, scope_id, add_scope_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_scope: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **id** | **int**|  |
 **scope_id** | **int**|  |
 **add_scope_request** | [**AddScopeRequest**](AddScopeRequest.md)|  |

### Return type

[**Id**](Id.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |
**422** | This name already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> User update_user(authorization, user_id, user)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.user import User
from openapi_client.model.status1 import Status1
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    user_id = 1 # int | Set to the id of the user that you want to return.
    user = User(
        id=1,
        username="username_example",
        email="email_example",
        firstname="firstname_example",
        lastname="lastname_example",
        title="title_example",
        department="department_example",
        company="company_example",
        comment="comment_example",
        group_id=1,
        role_ids=[
            1,
        ],
        phone="phone_example",
        state=0,
        status=0,
        directory_id=1,
        trusted_idp_id=1,
        manager_ad_id="manager_ad_id_example",
        manager_user_id="manager_user_id_example",
        samaccount_name="samaccount_name_example",
        member_of="member_of_example",
        userprincipalname="userprincipalname_example",
        distinguished_name="distinguished_name_example",
        external_id="external_id_example",
        activated_at="activated_at_example",
        last_login="last_login_example",
        invitation_sent_at="invitation_sent_at_example",
        updated_at="updated_at_example",
        preferred_locale_code="preferred_locale_code_example",
        created_at="created_at_example",
        custom_attributes={},
        invalid_login_attempts=1,
        locked_until="locked_until_example",
        password_changed_at="password_changed_at_example",
        password="password_example",
        password_confirmation="password_confirmation_example",
        password_algorithm="password_algorithm_example",
        salt="salt_example",
    ) # User | 
    mappings = "async" # str | Controls how mappings will be applied to the user on creation. Defaults to async. (optional)
    validate_policy = True # bool | Will passwords validate against the User Policy? Defaults to true. (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.update_user(authorization, user_id, user)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_user: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.update_user(authorization, user_id, user, mappings=mappings, validate_policy=validate_policy)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->update_user: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **user_id** | **int**| Set to the id of the user that you want to return. |
 **user** | [**User**](User.md)|  |
 **mappings** | **str**| Controls how mappings will be applied to the user on creation. Defaults to async. | [optional]
 **validate_policy** | **bool**| Will passwords validate against the User Policy? Defaults to true. | [optional]

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
**400** | BAD REQUEST |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**404** | Invalid ID |  -  |
**422** | Indicates that the syntax of the request is good but a value supplied is not valid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_enrollment**
> [Registration] verify_enrollment(authorization, user_id, registration_id, verify_enrollment_request)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.verify_enrollment_request import VerifyEnrollmentRequest
from openapi_client.model.status1 import Status1
from openapi_client.model.registration import Registration
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    user_id = 1 # int | Set to the id of the user.
    registration_id = 1 # int | Set to the uuid of the registration. This was included in the response as part of the initial request in Enroll Factor.
    verify_enrollment_request = VerifyEnrollmentRequest(
        otp=1,
    ) # VerifyEnrollmentRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.verify_enrollment(authorization, user_id, registration_id, verify_enrollment_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->verify_enrollment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **user_id** | **int**| Set to the id of the user. |
 **registration_id** | **int**| Set to the uuid of the registration. This was included in the response as part of the initial request in Enroll Factor. |
 **verify_enrollment_request** | [**VerifyEnrollmentRequest**](VerifyEnrollmentRequest.md)|  |

### Return type

[**[Registration]**](Registration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_enrollment_voice_protect**
> [Registration] verify_enrollment_voice_protect(authorization, user_id, registration_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.status1 import Status1
from openapi_client.model.registration import Registration
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    user_id = 1 # int | Set to the id of the user.
    registration_id = 1 # int | Set to the uuid of the registration. This was included in the response as part of the initial request in Enroll Factor.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.verify_enrollment_voice_protect(authorization, user_id, registration_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->verify_enrollment_voice_protect: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **user_id** | **int**| Set to the id of the user. |
 **registration_id** | **int**| Set to the uuid of the registration. This was included in the response as part of the initial request in Enroll Factor. |

### Return type

[**[Registration]**](Registration.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_factor**
> Status2 verify_factor(authorization, user_id, verification_id, verify_factor_request)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.verify_factor_request import VerifyFactorRequest
from openapi_client.model.status1 import Status1
from openapi_client.model.status2 import Status2
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    user_id = 1 # int | Set to the id of the user.
    verification_id = 1 # int | The verification_id is returned on activation of the factor or you can get the device_id using the Activate Factor API call.
    verify_factor_request = VerifyFactorRequest(
        otp="otp_example",
        device_id=1,
    ) # VerifyFactorRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.verify_factor(authorization, user_id, verification_id, verify_factor_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->verify_factor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **user_id** | **int**| Set to the id of the user. |
 **verification_id** | **int**| The verification_id is returned on activation of the factor or you can get the device_id using the Activate Factor API call. |
 **verify_factor_request** | [**VerifyFactorRequest**](VerifyFactorRequest.md)|  |

### Return type

[**Status2**](Status2.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Typically, this error means that your access token value is invalid. |  -  |
**403** | FORBIDDEN |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_factor_saml**
> VerifyFactorSaml200Response verify_factor_saml(authorization, verify_factor_saml_request)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.verify_factor_saml200_response import VerifyFactorSaml200Response
from openapi_client.model.status1 import Status1
from openapi_client.model.verify_factor_saml_request import VerifyFactorSamlRequest
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    verify_factor_saml_request = VerifyFactorSamlRequest(
        app_id="app_id_example",
        device_id="device_id_example",
        state_token="state_token_example",
        otp_token="otp_token_example",
        do_not_notify=True,
    ) # VerifyFactorSamlRequest | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.verify_factor_saml(authorization, verify_factor_saml_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->verify_factor_saml: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **verify_factor_saml_request** | [**VerifyFactorSamlRequest**](VerifyFactorSamlRequest.md)|  |

### Return type

[**VerifyFactorSaml200Response**](VerifyFactorSaml200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | BAD REQUEST |  -  |
**401** | UNAUTHORIZED |  -  |
**404** | Invalid ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_factor_voice**
> [VerifyFactorVoice200ResponseInner] verify_factor_voice(authorization, user_id, verification_id)



### Example


```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.verify_factor_voice200_response_inner import VerifyFactorVoice200ResponseInner
from openapi_client.model.status1 import Status1
from openapi_client.model.status2 import Status2
from pprint import pprint
# Defining the host is optional and defaults to https://onelogininc.onelogin.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://onelogininc.onelogin.com"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    authorization = "Authorization_example" # str | 
    user_id = 1 # int | Set to the id of the user.
    verification_id = 1 # int | The verification_id is returned on activation of the factor or you can get the device_id using the Activate Factor API call.

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.verify_factor_voice(authorization, user_id, verification_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->verify_factor_voice: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  |
 **user_id** | **int**| Set to the id of the user. |
 **verification_id** | **int**| The verification_id is returned on activation of the factor or you can get the device_id using the Activate Factor API call. |

### Return type

[**[VerifyFactorVoice200ResponseInner]**](VerifyFactorVoice200ResponseInner.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | NOT FOUND |  -  |
**404** | Invalid ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

