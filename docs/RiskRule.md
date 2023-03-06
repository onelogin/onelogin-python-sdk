# RiskRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** | The name of this rule | [optional] 
**description** | **str** |  | [optional] 
**type** | **str** | The type parameter specifies the type of rule that will be created. | [optional] 
**target** | **str** | The target parameter that will be used when evaluating the rule against an incoming event. | [optional] 
**filters** | **List[str]** | A list of IP addresses or country codes or names to evaluate against each event. | [optional] 
**source** | [**Source**](Source.md) |  | [optional] 

## Example

```python
from onelogin.models.risk_rule import RiskRule

# TODO update the JSON string below
json = "{}"
# create an instance of RiskRule from a JSON string
risk_rule_instance = RiskRule.from_json(json)
# print the JSON string representation of the object
print RiskRule.to_json()

# convert the object into a dict
risk_rule_dict = risk_rule_instance.to_dict()
# create an instance of RiskRule from a dict
risk_rule_form_dict = risk_rule.from_dict(risk_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


