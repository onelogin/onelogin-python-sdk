# GetEnrolledFactors200ResponseDataOtpDevicesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** | True &#x3D; enabled (used successfully for authentication at least once). False &#x3D; pending (registered but never used). | [optional] 
**default** | **bool** | True &#x3D; is user’s default MFA device for OneLogin. | [optional] 
**state_token** | **str** | A short lived token that is required to Verify the Factor. This token expires in 120 seconds. | [optional] 
**auth_factor_name** | **str** | \&quot;Official\&quot; authentication factor name, as it appears to administrators in OneLogin. | [optional] 
**phone_number** | **str** | For OTP codes sent via SMS, the phone number receiving the SMS message. | [optional] 
**type_display_name** | **str** | Authentication factor display name as it appears to users upon initial registration, as defined by admins at Settings &gt; Authentication Factors. | [optional] 
**needs_trigger** | **bool** | true: You MUST Activate this Factor to trigger an SMS or Push notification before Verifying the OTP code. false: No Activation required. You can Verify the OTP immediately. MFA factors that provide both push notifications (user accepts notification) and pull code submission (user initiates code submission from device or enters it manually) should appear twice; once with needs_trigger: true and once with needs_trigger: false. | [optional] 
**user_display_name** | **str** | Authentication factor display name assigned by users when they enroll the device. | [optional] 
**id** | **int** | MFA device identifier. | [optional] 

## Example

```python
from openapi_client.models.get_enrolled_factors200_response_data_otp_devices_inner import GetEnrolledFactors200ResponseDataOtpDevicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetEnrolledFactors200ResponseDataOtpDevicesInner from a JSON string
get_enrolled_factors200_response_data_otp_devices_inner_instance = GetEnrolledFactors200ResponseDataOtpDevicesInner.from_json(json)
# print the JSON string representation of the object
print GetEnrolledFactors200ResponseDataOtpDevicesInner.to_json()

# convert the object into a dict
get_enrolled_factors200_response_data_otp_devices_inner_dict = get_enrolled_factors200_response_data_otp_devices_inner_instance.to_dict()
# create an instance of GetEnrolledFactors200ResponseDataOtpDevicesInner from a dict
get_enrolled_factors200_response_data_otp_devices_inner_form_dict = get_enrolled_factors200_response_data_otp_devices_inner.from_dict(get_enrolled_factors200_response_data_otp_devices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


