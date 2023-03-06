# Privilege


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**privilege** | [**PrivilegePrivilege**](PrivilegePrivilege.md) |  | 

## Example

```python
from onelogin.models.privilege import Privilege

# TODO update the JSON string below
json = "{}"
# create an instance of Privilege from a JSON string
privilege_instance = Privilege.from_json(json)
# print the JSON string representation of the object
print Privilege.to_json()

# convert the object into a dict
privilege_dict = privilege_instance.to_dict()
# create an instance of Privilege from a dict
privilege_form_dict = privilege.from_dict(privilege_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


