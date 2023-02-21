# ListRiskRules200ResponseInnerSource

Used for targeting custom rules based on a group of people, customers, accounts, or even a single user.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique id that represents the source of the event. | [optional] 
**name** | **str** | The name of the source | [optional] 

## Example

```python
from onelogin.models.list_risk_rules200_response_inner_source import ListRiskRules200ResponseInnerSource

# TODO update the JSON string below
json = "{}"
# create an instance of ListRiskRules200ResponseInnerSource from a JSON string
list_risk_rules200_response_inner_source_instance = ListRiskRules200ResponseInnerSource.from_json(json)
# print the JSON string representation of the object
print ListRiskRules200ResponseInnerSource.to_json()

# convert the object into a dict
list_risk_rules200_response_inner_source_dict = list_risk_rules200_response_inner_source_instance.to_dict()
# create an instance of ListRiskRules200ResponseInnerSource from a dict
list_risk_rules200_response_inner_source_form_dict = list_risk_rules200_response_inner_source.from_dict(list_risk_rules200_response_inner_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


