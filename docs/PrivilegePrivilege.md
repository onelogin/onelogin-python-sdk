# PrivilegePrivilege


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 
**statement** | [**List[PrivilegePrivilegeStatementInner]**](PrivilegePrivilegeStatementInner.md) |  | [optional] 

## Example

```python
from onelogin.models.privilege_privilege import PrivilegePrivilege

# TODO update the JSON string below
json = "{}"
# create an instance of PrivilegePrivilege from a JSON string
privilege_privilege_instance = PrivilegePrivilege.from_json(json)
# print the JSON string representation of the object
print PrivilegePrivilege.to_json()

# convert the object into a dict
privilege_privilege_dict = privilege_privilege_instance.to_dict()
# create an instance of PrivilegePrivilege from a dict
privilege_privilege_form_dict = privilege_privilege.from_dict(privilege_privilege_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


