# GetRiskScores200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scores** | [**GetRiskScores200ResponseScores**](GetRiskScores200ResponseScores.md) |  | [optional] 
**total** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.get_risk_scores200_response import GetRiskScores200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetRiskScores200Response from a JSON string
get_risk_scores200_response_instance = GetRiskScores200Response.from_json(json)
# print the JSON string representation of the object
print GetRiskScores200Response.to_json()

# convert the object into a dict
get_risk_scores200_response_dict = get_risk_scores200_response_instance.to_dict()
# create an instance of GetRiskScores200Response from a dict
get_risk_scores200_response_form_dict = get_risk_scores200_response.from_dict(get_risk_scores200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


