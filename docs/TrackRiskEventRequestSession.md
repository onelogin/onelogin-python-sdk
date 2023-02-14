# TrackRiskEventRequestSession

A dictionary of extra information that provides useful context about the session, for example the session ID, or some cookie information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | If you use a database to track sessions, you can send us the session ID. | [optional] 

## Example

```python
from openapi_client.models.track_risk_event_request_session import TrackRiskEventRequestSession

# TODO update the JSON string below
json = "{}"
# create an instance of TrackRiskEventRequestSession from a JSON string
track_risk_event_request_session_instance = TrackRiskEventRequestSession.from_json(json)
# print the JSON string representation of the object
print TrackRiskEventRequestSession.to_json()

# convert the object into a dict
track_risk_event_request_session_dict = track_risk_event_request_session_instance.to_dict()
# create an instance of TrackRiskEventRequestSession from a dict
track_risk_event_request_session_form_dict = track_risk_event_request_session.from_dict(track_risk_event_request_session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


