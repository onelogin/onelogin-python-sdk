# GetRiskScore200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**score** | **float** | A risk score 0 is low risk and 100 is the highest risk level possible. | [optional] 
**triggers** | **List[str]** | Triggers are indicators of some of the key items that influenced the risk score. | [optional] 

## Example

```python
from onelogin.models.get_risk_score200_response import GetRiskScore200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetRiskScore200Response from a JSON string
get_risk_score200_response_instance = GetRiskScore200Response.from_json(json)
# print the JSON string representation of the object
print GetRiskScore200Response.to_json()

# convert the object into a dict
get_risk_score200_response_dict = get_risk_score200_response_instance.to_dict()
# create an instance of GetRiskScore200Response from a dict
get_risk_score200_response_form_dict = get_risk_score200_response.from_dict(get_risk_score200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


