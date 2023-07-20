# onelogin.model.saml_factor.SamlFactor

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**device_id** | str,  | str,  | Provide the MFA device_id you are submitting for verification. The device_id is supplied by the Generate SAML Assertion API. | 
**state_token** | str,  | str,  | Provide the state_token associated with the MFA device_id you are submitting for verification. The state_token is supplied by the Generate SAML Assertion API. | 
**app_id** | str,  | str,  | App ID of the app for which you want to generate a SAML token. This is the app ID in OneLogin. | 
**otp_token** | str,  | str,  | Provide the OTP value for the MFA factor you are submitting for verification. For some MFA factors; such as OneLogin OTP SMS, which requires the user to request an OTP; the otp_token value is not required, and if not included, returns a 200 OK - Pending result. You’ll make a subsequent Verify Factor API call to provide the otp_token value once it has been provided to the user. | [optional] 
**do_not_notify** | bool,  | BoolClass,  | When verifying MFA via Protect Push, set this to true to stop additional push notifications being sent to the OneLogin Protect device. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

