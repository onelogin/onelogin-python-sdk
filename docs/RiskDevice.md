# RiskDevice

Information about the device being used.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | This device&#39;s unique identifier | [optional] 

## Example

```python
from onelogin.models.risk_device import RiskDevice

# TODO update the JSON string below
json = "{}"
# create an instance of RiskDevice from a JSON string
risk_device_instance = RiskDevice.from_json(json)
# print the JSON string representation of the object
print RiskDevice.to_json()

# convert the object into a dict
risk_device_dict = risk_device_instance.to_dict()
# create an instance of RiskDevice from a dict
risk_device_form_dict = risk_device.from_dict(risk_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


