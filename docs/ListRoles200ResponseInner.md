# ListRoles200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | 
**apps** | **List[int]** |  | [optional] 
**users** | **List[int]** |  | [optional] 
**admins** | **List[int]** |  | [optional] 

## Example

```python
from openapi_client.models.list_roles200_response_inner import ListRoles200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListRoles200ResponseInner from a JSON string
list_roles200_response_inner_instance = ListRoles200ResponseInner.from_json(json)
# print the JSON string representation of the object
print ListRoles200ResponseInner.to_json()

# convert the object into a dict
list_roles200_response_inner_dict = list_roles200_response_inner_instance.to_dict()
# create an instance of ListRoles200ResponseInner from a dict
list_roles200_response_inner_form_dict = list_roles200_response_inner.from_dict(list_roles200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


