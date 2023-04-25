# OtpDevice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**factor_id** | **int** | The identifier of the factor to enroll the user with. | [readonly] 
**display_name** | **str** | A name for the users device | 
**number** | **str** | The phone number of the user in E.164 format. | 
**verified** | **bool** | Defaults to false. Some factors like SMS or Voice require that a user recieve a token and then that token is supplied to the Verify endpoint before the device is considered active. You can set verfied to &#x60;true&#x60; which indicates the the users phone number is pre verified and the device can be immediately activated.            | [optional] 

## Example

```python
from onelogin.models.otp_device import OtpDevice

# TODO update the JSON string below
json = "{}"
# create an instance of OtpDevice from a JSON string
otp_device_instance = OtpDevice.from_json(json)
# print the JSON string representation of the object
print OtpDevice.to_json()

# convert the object into a dict
otp_device_dict = otp_device_instance.to_dict()
# create an instance of OtpDevice from a dict
otp_device_form_dict = otp_device.from_dict(otp_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


