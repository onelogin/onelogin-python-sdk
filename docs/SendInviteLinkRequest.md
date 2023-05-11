# SendInviteLinkRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Set to the user email address to generate an invite link. The value is case sensitive. | [optional] 
**personal_email** | **str** | To send an invite email to a different address than the one provided in email, provide it here. The invite link is sent to this address instead. | [optional] 

## Example

```python
from onelogin.models.send_invite_link_request import SendInviteLinkRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendInviteLinkRequest from a JSON string
send_invite_link_request_instance = SendInviteLinkRequest.from_json(json)
# print the JSON string representation of the object
print SendInviteLinkRequest.to_json()

# convert the object into a dict
send_invite_link_request_dict = send_invite_link_request_instance.to_dict()
# create an instance of SendInviteLinkRequest from a dict
send_invite_link_request_form_dict = send_invite_link_request.from_dict(send_invite_link_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


