# AddPrivilegeToRoleRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | **List[int]** |  | [optional] 

## Example

```python
from openapi_client.models.add_privilege_to_role_request import AddPrivilegeToRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddPrivilegeToRoleRequest from a JSON string
add_privilege_to_role_request_instance = AddPrivilegeToRoleRequest.from_json(json)
# print the JSON string representation of the object
print AddPrivilegeToRoleRequest.to_json()

# convert the object into a dict
add_privilege_to_role_request_dict = add_privilege_to_role_request_instance.to_dict()
# create an instance of AddPrivilegeToRoleRequest from a dict
add_privilege_to_role_request_form_dict = add_privilege_to_role_request.from_dict(add_privilege_to_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


