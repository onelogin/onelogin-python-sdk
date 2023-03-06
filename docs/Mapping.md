# Mapping


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** | The name of the mapping. | 
**enabled** | **bool** | Indicates if the mapping is enabled or not. | 
**match** | **str** | Indicates how conditions should be matched. | 
**position** | **int** | Indicates the order of the mapping. When &#x60;null&#x60; this will default to last position. | 
**conditions** | [**List[Condition]**](Condition.md) | An array of conditions that the user must meet in order for the mapping to be applied. | 
**actions** | [**List[ActionObj]**](ActionObj.md) | An array of actions that will be applied to the users that are matched by the conditions. | 

## Example

```python
from onelogin.models.mapping import Mapping

# TODO update the JSON string below
json = "{}"
# create an instance of Mapping from a JSON string
mapping_instance = Mapping.from_json(json)
# print the JSON string representation of the object
print Mapping.to_json()

# convert the object into a dict
mapping_dict = mapping_instance.to_dict()
# create an instance of Mapping from a dict
mapping_form_dict = mapping.from_dict(mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


