# UpdateRiskRuleRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the Rule to Update | [optional] 

## Example

```python
from onelogin.models.update_risk_rule_request import UpdateRiskRuleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRiskRuleRequest from a JSON string
update_risk_rule_request_instance = UpdateRiskRuleRequest.from_json(json)
# print the JSON string representation of the object
print UpdateRiskRuleRequest.to_json()

# convert the object into a dict
update_risk_rule_request_dict = update_risk_rule_request_instance.to_dict()
# create an instance of UpdateRiskRuleRequest from a dict
update_risk_rule_request_form_dict = update_risk_rule_request.from_dict(update_risk_rule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


