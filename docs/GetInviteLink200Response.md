# GetInviteLink200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**GenerateToken400Response**](GenerateToken400Response.md) |  | [optional] 
**data** | **List[str]** | Provides reset password link | [optional] 

## Example

```python
from openapi_client.models.get_invite_link200_response import GetInviteLink200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetInviteLink200Response from a JSON string
get_invite_link200_response_instance = GetInviteLink200Response.from_json(json)
# print the JSON string representation of the object
print GetInviteLink200Response.to_json()

# convert the object into a dict
get_invite_link200_response_dict = get_invite_link200_response_instance.to_dict()
# create an instance of GetInviteLink200Response from a dict
get_invite_link200_response_form_dict = get_invite_link200_response.from_dict(get_invite_link200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


