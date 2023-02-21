# ListMappings200ResponseInnerActionsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action to apply | [optional] 
**value** | **List[str]** | Only applicable to provisioned and set_* actions. Items in the array will be a plain text string or valid value for the selected action. | [optional] 

## Example

```python
from onelogin.models.list_mappings200_response_inner_actions_inner import ListMappings200ResponseInnerActionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListMappings200ResponseInnerActionsInner from a JSON string
list_mappings200_response_inner_actions_inner_instance = ListMappings200ResponseInnerActionsInner.from_json(json)
# print the JSON string representation of the object
print ListMappings200ResponseInnerActionsInner.to_json()

# convert the object into a dict
list_mappings200_response_inner_actions_inner_dict = list_mappings200_response_inner_actions_inner_instance.to_dict()
# create an instance of ListMappings200ResponseInnerActionsInner from a dict
list_mappings200_response_inner_actions_inner_form_dict = list_mappings200_response_inner_actions_inner.from_dict(list_mappings200_response_inner_actions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


