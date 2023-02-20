# CreateDeviceVerificationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** | Specifies the factor to be verified. | 
**display_name** | **str** | A name for the users device | [optional] 
**expires_in** | **str** | Defaults to 120. Valid values are: 120-900 seconds. | [optional] 
**redirect_to** | **str** | Only applies to Email MagicLink factor. Redirects MagicLink success page to specified URL after 2 seconds. Email must already be configured by the user. | [optional] 
**custom_message** | **str** | Only applies to SMS factor. A message template that will be sent via SMS. Max length of the message after template items are inserted is 160 characters including the OTP code. SMS must already be configured by the user. The following template variables can be included in the message. - {{otp_code}} - The security code. - {{otp_expiry}} - The number of minutes until the one time code expires. | [optional] 

## Example

```python
from openapi_client.models.create_device_verification_request import CreateDeviceVerificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDeviceVerificationRequest from a JSON string
create_device_verification_request_instance = CreateDeviceVerificationRequest.from_json(json)
# print the JSON string representation of the object
print CreateDeviceVerificationRequest.to_json()

# convert the object into a dict
create_device_verification_request_dict = create_device_verification_request_instance.to_dict()
# create an instance of CreateDeviceVerificationRequest from a dict
create_device_verification_request_form_dict = create_device_verification_request.from_dict(create_device_verification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


