# RuleCondition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the operator | [optional] 
**value** | **str** | The condition operator value to use when creating or updating rules. | [optional] 

## Example

```python
from onelogin.models.rule_condition import RuleCondition

# TODO update the JSON string below
json = "{}"
# create an instance of RuleCondition from a JSON string
rule_condition_instance = RuleCondition.from_json(json)
# print the JSON string representation of the object
print RuleCondition.to_json()

# convert the object into a dict
rule_condition_dict = rule_condition_instance.to_dict()
# create an instance of RuleCondition from a dict
rule_condition_form_dict = rule_condition.from_dict(rule_condition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


