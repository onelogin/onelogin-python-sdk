# TrackRiskEventRequestDevice

Information about the device being used.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | This device&#39;s unique identifier | [optional] 

## Example

```python
from onelogin.models.track_risk_event_request_device import TrackRiskEventRequestDevice

# TODO update the JSON string below
json = "{}"
# create an instance of TrackRiskEventRequestDevice from a JSON string
track_risk_event_request_device_instance = TrackRiskEventRequestDevice.from_json(json)
# print the JSON string representation of the object
print TrackRiskEventRequestDevice.to_json()

# convert the object into a dict
track_risk_event_request_device_dict = track_risk_event_request_device_instance.to_dict()
# create an instance of TrackRiskEventRequestDevice from a dict
track_risk_event_request_device_form_dict = track_risk_event_request_device.from_dict(track_risk_event_request_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


