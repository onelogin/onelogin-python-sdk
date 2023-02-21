# GetRiskScores200ResponseScores


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minimal** | **int** |  | [optional] 
**low** | **int** |  | [optional] 
**medium** | **int** |  | [optional] 
**high** | **int** |  | [optional] 
**very_high** | **int** |  | [optional] 

## Example

```python
from onelogin.models.get_risk_scores200_response_scores import GetRiskScores200ResponseScores

# TODO update the JSON string below
json = "{}"
# create an instance of GetRiskScores200ResponseScores from a JSON string
get_risk_scores200_response_scores_instance = GetRiskScores200ResponseScores.from_json(json)
# print the JSON string representation of the object
print GetRiskScores200ResponseScores.to_json()

# convert the object into a dict
get_risk_scores200_response_scores_dict = get_risk_scores200_response_scores_instance.to_dict()
# create an instance of GetRiskScores200ResponseScores from a dict
get_risk_scores200_response_scores_form_dict = get_risk_scores200_response_scores.from_dict(get_risk_scores200_response_scores_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


