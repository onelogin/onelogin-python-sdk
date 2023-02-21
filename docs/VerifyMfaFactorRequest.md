# VerifyMfaFactorRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state_token** | **str** | The state_token is returned after a successful request to Enroll a Factor or Activate a Factor. The state_token MUST be provided if the needs_trigger attribute from the proceeding calls is set to true. Note that the state_token expires 120 seconds after creation. If the token is expired you will need to Activate the Factor again. | [optional] 
**otp_token** | **str** | OTP code provided by the device or SMS message sent to user. When a device like OneLogin Protect that supports Push has been used you do not need to provide the otp_token and can keep polling this endpoint until the state_token expires. | [optional] 

## Example

```python
from onelogin.models.verify_mfa_factor_request import VerifyMfaFactorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyMfaFactorRequest from a JSON string
verify_mfa_factor_request_instance = VerifyMfaFactorRequest.from_json(json)
# print the JSON string representation of the object
print VerifyMfaFactorRequest.to_json()

# convert the object into a dict
verify_mfa_factor_request_dict = verify_mfa_factor_request_instance.to_dict()
# create an instance of VerifyMfaFactorRequest from a dict
verify_mfa_factor_request_form_dict = verify_mfa_factor_request.from_dict(verify_mfa_factor_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


