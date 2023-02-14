# AddRolesToUserRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id_array** | **List[int]** | Set to an array of one or more role IDs. The IDs must be positive integers. | 

## Example

```python
from openapi_client.models.add_roles_to_user_request import AddRolesToUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddRolesToUserRequest from a JSON string
add_roles_to_user_request_instance = AddRolesToUserRequest.from_json(json)
# print the JSON string representation of the object
print AddRolesToUserRequest.to_json()

# convert the object into a dict
add_roles_to_user_request_dict = add_roles_to_user_request_instance.to_dict()
# create an instance of AddRolesToUserRequest from a dict
add_roles_to_user_request_form_dict = add_roles_to_user_request.from_dict(add_roles_to_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


