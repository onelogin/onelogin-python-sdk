# GetRoleById200ResponseDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | role&#39;s unique ID in Onelogin | [optional] 
**name** | **str** | Role name | [optional] 

## Example

```python
from openapi_client.models.get_role_by_id200_response_data_inner import GetRoleById200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoleById200ResponseDataInner from a JSON string
get_role_by_id200_response_data_inner_instance = GetRoleById200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print GetRoleById200ResponseDataInner.to_json()

# convert the object into a dict
get_role_by_id200_response_data_inner_dict = get_role_by_id200_response_data_inner_instance.to_dict()
# create an instance of GetRoleById200ResponseDataInner from a dict
get_role_by_id200_response_data_inner_form_dict = get_role_by_id200_response_data_inner.from_dict(get_role_by_id200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


