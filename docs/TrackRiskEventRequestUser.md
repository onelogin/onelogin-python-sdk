# TrackRiskEventRequestUser

An Object containing User details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for the user. | 
**name** | **str** | A name for the user. | [optional] 
**authenticated** | **bool** | Indicates if the metadata supplied in this event should be considered as trusted for the user. | [optional] [default to False]

## Example

```python
from openapi_client.models.track_risk_event_request_user import TrackRiskEventRequestUser

# TODO update the JSON string below
json = "{}"
# create an instance of TrackRiskEventRequestUser from a JSON string
track_risk_event_request_user_instance = TrackRiskEventRequestUser.from_json(json)
# print the JSON string representation of the object
print TrackRiskEventRequestUser.to_json()

# convert the object into a dict
track_risk_event_request_user_dict = track_risk_event_request_user_instance.to_dict()
# create an instance of TrackRiskEventRequestUser from a dict
track_risk_event_request_user_form_dict = track_risk_event_request_user.from_dict(track_risk_event_request_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


