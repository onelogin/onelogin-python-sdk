# Condition

Conditions in which mappings are applied

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**source** | **str** | source field to check. | [optional] 
**operator** | **str** | A valid operator for the selected condition source | [optional] 
**value** | **str** | A plain text string or valid value for the selected  condition source | [optional] 

## Example

```python
from onelogin.models.condition import Condition

# TODO update the JSON string below
json = "{}"
# create an instance of Condition from a JSON string
condition_instance = Condition.from_json(json)
# print the JSON string representation of the object
print Condition.to_json()

# convert the object into a dict
condition_dict = condition_instance.to_dict()
# create an instance of Condition from a dict
condition_form_dict = condition.from_dict(condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


