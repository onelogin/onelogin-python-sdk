# ListRiskRules200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** | The name of this rule | [optional] 
**description** | **str** |  | [optional] 
**type** | **str** | The type parameter specifies the type of rule that will be created. | [optional] 
**target** | **str** | The target parameter that will be used when evaluating the rule against an incoming event. | [optional] 
**filters** | **List[str]** | A list of IP addresses or country codes or names to evaluate against each event. | [optional] 
**source** | [**ListRiskRules200ResponseInnerSource**](ListRiskRules200ResponseInnerSource.md) |  | [optional] 

## Example

```python
from onelogin.models.list_risk_rules200_response_inner import ListRiskRules200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListRiskRules200ResponseInner from a JSON string
list_risk_rules200_response_inner_instance = ListRiskRules200ResponseInner.from_json(json)
# print the JSON string representation of the object
print ListRiskRules200ResponseInner.to_json()

# convert the object into a dict
list_risk_rules200_response_inner_dict = list_risk_rules200_response_inner_instance.to_dict()
# create an instance of ListRiskRules200ResponseInner from a dict
list_risk_rules200_response_inner_form_dict = list_risk_rules200_response_inner.from_dict(list_risk_rules200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


