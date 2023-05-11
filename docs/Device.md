# Device


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** | an ID for the device type that must be submitted with the Verify Factor API call. | [optional] 
**device_type** | **str** | Lists an available MFA device type, such as OneLogin OTP SMS or Google Authenticator. | [optional] 

## Example

```python
from onelogin.models.device import Device

# TODO update the JSON string below
json = "{}"
# create an instance of Device from a JSON string
device_instance = Device.from_json(json)
# print the JSON string representation of the object
print Device.to_json()

# convert the object into a dict
device_dict = device_instance.to_dict()
# create an instance of Device from a dict
device_form_dict = device.from_dict(device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


