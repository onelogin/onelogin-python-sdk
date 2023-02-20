# ListMappingActionValues200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name or description of operator | [optional] 
**value** | **int** | The action operator value to use when creating or updating User Mappings. | [optional] 

## Example

```python
from openapi_client.models.list_mapping_action_values200_response_inner import ListMappingActionValues200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListMappingActionValues200ResponseInner from a JSON string
list_mapping_action_values200_response_inner_instance = ListMappingActionValues200ResponseInner.from_json(json)
# print the JSON string representation of the object
print ListMappingActionValues200ResponseInner.to_json()

# convert the object into a dict
list_mapping_action_values200_response_inner_dict = list_mapping_action_values200_response_inner_instance.to_dict()
# create an instance of ListMappingActionValues200ResponseInner from a dict
list_mapping_action_values200_response_inner_form_dict = list_mapping_action_values200_response_inner.from_dict(list_mapping_action_values200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


