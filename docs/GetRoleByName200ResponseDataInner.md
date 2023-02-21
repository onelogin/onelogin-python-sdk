# GetRoleByName200ResponseDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Role ID | [optional] 
**name** | **str** | Role Name | [optional] 

## Example

```python
from onelogin.models.get_role_by_name200_response_data_inner import GetRoleByName200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoleByName200ResponseDataInner from a JSON string
get_role_by_name200_response_data_inner_instance = GetRoleByName200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print GetRoleByName200ResponseDataInner.to_json()

# convert the object into a dict
get_role_by_name200_response_data_inner_dict = get_role_by_name200_response_data_inner_instance.to_dict()
# create an instance of GetRoleByName200ResponseDataInner from a dict
get_role_by_name200_response_data_inner_form_dict = get_role_by_name200_response_data_inner.from_dict(get_role_by_name200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


