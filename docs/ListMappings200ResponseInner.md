# ListMappings200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** | The name of the mapping. | 
**enabled** | **bool** | Indicates if the mapping is enabled or not. | 
**match** | **str** | Indicates how conditions should be matched. | 
**position** | **int** | Indicates the order of the mapping. When &#x60;null&#x60; this will default to last position. | 
**conditions** | [**List[ListMappings200ResponseInnerConditionsInner]**](ListMappings200ResponseInnerConditionsInner.md) | An array of conditions that the user must meet in order for the mapping to be applied. | 
**actions** | [**List[ListMappings200ResponseInnerActionsInner]**](ListMappings200ResponseInnerActionsInner.md) | An array of actions that will be applied to the users that are matched by the conditions. | 

## Example

```python
from openapi_client.models.list_mappings200_response_inner import ListMappings200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListMappings200ResponseInner from a JSON string
list_mappings200_response_inner_instance = ListMappings200ResponseInner.from_json(json)
# print the JSON string representation of the object
print ListMappings200ResponseInner.to_json()

# convert the object into a dict
list_mappings200_response_inner_dict = list_mappings200_response_inner_instance.to_dict()
# create an instance of ListMappings200ResponseInner from a dict
list_mappings200_response_inner_form_dict = list_mappings200_response_inner.from_dict(list_mappings200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


