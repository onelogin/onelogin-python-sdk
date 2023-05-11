# onelogin.InviteLinksApi

All URIs are relative to *https://your-api-subdomain.onelogin.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_invite_link**](InviteLinksApi.md#get_invite_link) | **POST** /api/1/invites/get_invite_link | Generate Invite Link
[**send_invite_link**](InviteLinksApi.md#send_invite_link) | **POST** /api/1/invites/send_invite_link | Send  Invite Link


# **get_invite_link**
> GetInviteLink200Response get_invite_link(get_invite_link_request=get_invite_link_request)

Generate Invite Link

Generate Invite Link

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
    api_instance = onelogin.InviteLinksApi(api_client)
    get_invite_link_request = onelogin.GetInviteLinkRequest() # GetInviteLinkRequest |  (optional)

    try:
        # Generate Invite Link
        api_response = api_instance.get_invite_link(get_invite_link_request=get_invite_link_request)
        print("The response of InviteLinksApi->get_invite_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InviteLinksApi->get_invite_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_invite_link_request** | [**GetInviteLinkRequest**](GetInviteLinkRequest.md)|  | [optional] 

### Return type

[**GetInviteLink200Response**](GetInviteLink200Response.md)

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

# **send_invite_link**
> SendInviteLink200Response send_invite_link(send_invite_link_request=send_invite_link_request)

Send  Invite Link

Send Invite Link

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
    api_instance = onelogin.InviteLinksApi(api_client)
    send_invite_link_request = onelogin.SendInviteLinkRequest() # SendInviteLinkRequest |  (optional)

    try:
        # Send  Invite Link
        api_response = api_instance.send_invite_link(send_invite_link_request=send_invite_link_request)
        print("The response of InviteLinksApi->send_invite_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InviteLinksApi->send_invite_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_invite_link_request** | [**SendInviteLinkRequest**](SendInviteLinkRequest.md)|  | [optional] 

### Return type

[**SendInviteLink200Response**](SendInviteLink200Response.md)

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

