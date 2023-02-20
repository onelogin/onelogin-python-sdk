# RemoveUserRoleRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id_array** | [**List[RemoveUserRoleRequestRoleIdArrayInner]**](RemoveUserRoleRequestRoleIdArrayInner.md) |  | 

## Example

```python
from openapi_client.models.remove_user_role_request import RemoveUserRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveUserRoleRequest from a JSON string
remove_user_role_request_instance = RemoveUserRoleRequest.from_json(json)
# print the JSON string representation of the object
print RemoveUserRoleRequest.to_json()

# convert the object into a dict
remove_user_role_request_dict = remove_user_role_request_instance.to_dict()
# create an instance of RemoveUserRoleRequest from a dict
remove_user_role_request_form_dict = remove_user_role_request.from_dict(remove_user_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


