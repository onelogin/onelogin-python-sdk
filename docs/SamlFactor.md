# SamlFactor


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | App ID of the app for which you want to generate a SAML token. This is the app ID in OneLogin. | 
**device_id** | **str** | Provide the MFA device_id you are submitting for verification. The device_id is supplied by the Generate SAML Assertion API. | 
**state_token** | **str** | Provide the state_token associated with the MFA device_id you are submitting for verification. The state_token is supplied by the Generate SAML Assertion API. | 
**otp_token** | **str** | Provide the OTP value for the MFA factor you are submitting for verification. For some MFA factors; such as OneLogin OTP SMS, which requires the user to request an OTP; the otp_token value is not required, and if not included, returns a 200 OK - Pending result. You’ll make a subsequent Verify Factor API call to provide the otp_token value once it has been provided to the user. | [optional] 
**do_not_notify** | **bool** | When verifying MFA via Protect Push, set this to true to stop additional push notifications being sent to the OneLogin Protect device. | [optional] 

## Example

```python
from onelogin.models.saml_factor import SamlFactor

# TODO update the JSON string below
json = "{}"
# create an instance of SamlFactor from a JSON string
saml_factor_instance = SamlFactor.from_json(json)
# print the JSON string representation of the object
print SamlFactor.to_json()

# convert the object into a dict
saml_factor_dict = saml_factor_instance.to_dict()
# create an instance of SamlFactor from a dict
saml_factor_form_dict = saml_factor.from_dict(saml_factor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


