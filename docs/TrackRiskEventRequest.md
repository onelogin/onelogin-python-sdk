# TrackRiskEventRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verb** | **str** | Verbs are used to distinguish between different types of events. | 
**ip** | **str** | The IP address of the User&#39;s request. | 
**user_agent** | **str** | The user agent of the User&#39;s request. | 
**user** | [**TrackRiskEventRequestUser**](TrackRiskEventRequestUser.md) |  | 
**source** | [**ListRiskRules200ResponseInnerSource**](ListRiskRules200ResponseInnerSource.md) |  | [optional] 
**session** | [**TrackRiskEventRequestSession**](TrackRiskEventRequestSession.md) |  | [optional] 
**device** | [**TrackRiskEventRequestDevice**](TrackRiskEventRequestDevice.md) |  | [optional] 
**fp** | **str** | Set to the value of the __tdli_fp cookie. | [optional] 
**published** | **str** | Date and time of the event in IS08601 format. Useful for preloading old events. Defaults to date time this API request is received. | [optional] 

## Example

```python
from onelogin.models.track_risk_event_request import TrackRiskEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrackRiskEventRequest from a JSON string
track_risk_event_request_instance = TrackRiskEventRequest.from_json(json)
# print the JSON string representation of the object
print TrackRiskEventRequest.to_json()

# convert the object into a dict
track_risk_event_request_dict = track_risk_event_request_instance.to_dict()
# create an instance of TrackRiskEventRequest from a dict
track_risk_event_request_form_dict = track_risk_event_request.from_dict(track_risk_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


