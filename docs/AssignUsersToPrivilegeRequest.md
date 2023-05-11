# AssignUsersToPrivilegeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | **List[int]** |  | [optional] 

## Example

```python
from onelogin.models.assign_users_to_privilege_request import AssignUsersToPrivilegeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AssignUsersToPrivilegeRequest from a JSON string
assign_users_to_privilege_request_instance = AssignUsersToPrivilegeRequest.from_json(json)
# print the JSON string representation of the object
print AssignUsersToPrivilegeRequest.to_json()

# convert the object into a dict
assign_users_to_privilege_request_dict = assign_users_to_privilege_request_instance.to_dict()
# create an instance of AssignUsersToPrivilegeRequest from a dict
assign_users_to_privilege_request_form_dict = assign_users_to_privilege_request.from_dict(assign_users_to_privilege_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


