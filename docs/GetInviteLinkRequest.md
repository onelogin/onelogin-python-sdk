# GetInviteLinkRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Set to the user email address to generate an invite link. The value is case sensitive. | [optional] 

## Example

```python
from openapi_client.models.get_invite_link_request import GetInviteLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetInviteLinkRequest from a JSON string
get_invite_link_request_instance = GetInviteLinkRequest.from_json(json)
# print the JSON string representation of the object
print GetInviteLinkRequest.to_json()

# convert the object into a dict
get_invite_link_request_dict = get_invite_link_request_instance.to_dict()
# create an instance of GetInviteLinkRequest from a dict
get_invite_link_request_form_dict = get_invite_link_request.from_dict(get_invite_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


