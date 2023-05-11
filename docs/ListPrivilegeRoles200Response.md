# ListPrivilegeRoles200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**roles** | **List[int]** |  | [optional] 
**before_cursor** | **int** |  | [optional] 
**previous_link** | **str** |  | [optional] 
**after_cursor** | **int** |  | [optional] 
**next_link** | **str** |  | [optional] 

## Example

```python
from onelogin.models.list_privilege_roles200_response import ListPrivilegeRoles200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListPrivilegeRoles200Response from a JSON string
list_privilege_roles200_response_instance = ListPrivilegeRoles200Response.from_json(json)
# print the JSON string representation of the object
print ListPrivilegeRoles200Response.to_json()

# convert the object into a dict
list_privilege_roles200_response_dict = list_privilege_roles200_response_instance.to_dict()
# create an instance of ListPrivilegeRoles200Response from a dict
list_privilege_roles200_response_form_dict = list_privilege_roles200_response.from_dict(list_privilege_roles200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


