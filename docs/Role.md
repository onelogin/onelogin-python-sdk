# Role


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Role ID | [optional] 
**name** | **str** | Role Name | 
**apps** | **List[int]** | array of app IDs | [optional] 
**users** | **List[int]** | array of user IDs | [optional] 
**admins** | **List[int]** |  | [optional] 

## Example

```python
from onelogin.models.role import Role

# TODO update the JSON string below
json = "{}"
# create an instance of Role from a JSON string
role_instance = Role.from_json(json)
# print the JSON string representation of the object
print Role.to_json()

# convert the object into a dict
role_dict = role_instance.to_dict()
# create an instance of Role from a dict
role_form_dict = role.from_dict(role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


