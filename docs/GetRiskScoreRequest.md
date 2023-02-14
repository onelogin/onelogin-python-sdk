# GetRiskScoreRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | The IP address of the User&#39;s request. | 
**user_agent** | **str** | The user agent of the User&#39;s request. | 
**user** | [**TrackRiskEventRequestUser**](TrackRiskEventRequestUser.md) |  | 
**source** | [**ListRiskRules200ResponseInnerSource**](ListRiskRules200ResponseInnerSource.md) |  | [optional] 
**session** | [**TrackRiskEventRequestSession**](TrackRiskEventRequestSession.md) |  | [optional] 
**device** | [**TrackRiskEventRequestDevice**](TrackRiskEventRequestDevice.md) |  | [optional] 
**fp** | **str** | Set to the value of the __tdli_fp cookie. | [optional] 

## Example

```python
from openapi_client.models.get_risk_score_request import GetRiskScoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetRiskScoreRequest from a JSON string
get_risk_score_request_instance = GetRiskScoreRequest.from_json(json)
# print the JSON string representation of the object
print GetRiskScoreRequest.to_json()

# convert the object into a dict
get_risk_score_request_dict = get_risk_score_request_instance.to_dict()
# create an instance of GetRiskScoreRequest from a dict
get_risk_score_request_form_dict = get_risk_score_request.from_dict(get_risk_score_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


