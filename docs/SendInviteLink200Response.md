# SendInviteLink200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Error**](Error.md) |  | [optional] 

## Example

```python
from onelogin.models.send_invite_link200_response import SendInviteLink200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SendInviteLink200Response from a JSON string
send_invite_link200_response_instance = SendInviteLink200Response.from_json(json)
# print the JSON string representation of the object
print SendInviteLink200Response.to_json()

# convert the object into a dict
send_invite_link200_response_dict = send_invite_link200_response_instance.to_dict()
# create an instance of SendInviteLink200Response from a dict
send_invite_link200_response_form_dict = send_invite_link200_response.from_dict(send_invite_link200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


