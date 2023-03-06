# Rule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | App Rule ID | [optional] 
**name** | **str** | Rule Name | [optional] 
**match** | **str** | Indicates how conditions should be matched. | [optional] 
**enabled** | **bool** | Indicates if the rule is enabled or not. | [optional] 
**position** | **int** | Indicates the order of the rule. When &#x60;null&#x60; this will default to last position. | [optional] 
**conditions** | [**List[Condition]**](Condition.md) | An array of conditions that the user must meet in order for the rule to be applied. | [optional] 
**actions** | [**List[ActionObj]**](ActionObj.md) |  | [optional] 

## Example

```python
from onelogin.models.rule import Rule

# TODO update the JSON string below
json = "{}"
# create an instance of Rule from a JSON string
rule_instance = Rule.from_json(json)
# print the JSON string representation of the object
print Rule.to_json()

# convert the object into a dict
rule_dict = rule_instance.to_dict()
# create an instance of Rule from a dict
rule_form_dict = rule.from_dict(rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


