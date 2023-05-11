# SetUserStateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state** | **int** | Set to the state value. Valid values include:   - 0 : Unapproved   - 1 : Approved   - 2 : Rejected   - 3 : Unlicensed | 

## Example

```python
from onelogin.models.set_user_state_request import SetUserStateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetUserStateRequest from a JSON string
set_user_state_request_instance = SetUserStateRequest.from_json(json)
# print the JSON string representation of the object
print SetUserStateRequest.to_json()

# convert the object into a dict
set_user_state_request_dict = set_user_state_request_instance.to_dict()
# create an instance of SetUserStateRequest from a dict
set_user_state_request_form_dict = set_user_state_request.from_dict(set_user_state_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


