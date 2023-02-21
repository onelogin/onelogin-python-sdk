# RemoveRoleUsersRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **List[int]** |  | [optional] 

## Example

```python
from onelogin.models.remove_role_users_request import RemoveRoleUsersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveRoleUsersRequest from a JSON string
remove_role_users_request_instance = RemoveRoleUsersRequest.from_json(json)
# print the JSON string representation of the object
print RemoveRoleUsersRequest.to_json()

# convert the object into a dict
remove_role_users_request_dict = remove_role_users_request_instance.to_dict()
# create an instance of RemoveRoleUsersRequest from a dict
remove_role_users_request_form_dict = remove_role_users_request.from_dict(remove_role_users_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


