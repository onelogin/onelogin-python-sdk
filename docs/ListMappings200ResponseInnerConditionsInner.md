# ListMappings200ResponseInnerConditionsInner

Conditions in which mappings are applied

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | source field to check. | [optional] 
**operator** | **str** | A valid operator for the selected condition source | [optional] 
**value** | **str** | A plain text string or valid value for the selected  condition source | [optional] 

## Example

```python
from openapi_client.models.list_mappings200_response_inner_conditions_inner import ListMappings200ResponseInnerConditionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListMappings200ResponseInnerConditionsInner from a JSON string
list_mappings200_response_inner_conditions_inner_instance = ListMappings200ResponseInnerConditionsInner.from_json(json)
# print the JSON string representation of the object
print ListMappings200ResponseInnerConditionsInner.to_json()

# convert the object into a dict
list_mappings200_response_inner_conditions_inner_dict = list_mappings200_response_inner_conditions_inner_instance.to_dict()
# create an instance of ListMappings200ResponseInnerConditionsInner from a dict
list_mappings200_response_inner_conditions_inner_form_dict = list_mappings200_response_inner_conditions_inner.from_dict(list_mappings200_response_inner_conditions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


