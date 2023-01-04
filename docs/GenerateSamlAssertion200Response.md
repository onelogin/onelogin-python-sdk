# GenerateSamlAssertion200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | Provides the SAML assertion. Returned only when MFA is not required. | [optional] 
**message** | **str** | Plain text description describing the outcome of the response. | [optional] 
**state_token** | **str** | State_token that must be submitted with each Verify Factor API call until the SAML assertion has been issued. Returned only if MFA is required. | [optional] 
**user** | [**GenerateSamlAssertion200ResponseUser**](GenerateSamlAssertion200ResponseUser.md) |  | [optional] 
**devices** | [**[GenerateSamlAssertion200ResponseDevicesInner]**](GenerateSamlAssertion200ResponseDevicesInner.md) | Provides device values that must be submitted with the Verify Factor API call. Returned only when MFA is required. | [optional] 
**callback_url** | **str** | Verify Factor API endpoint to which the device_id, state_token, app_id, and otp_token must be sent. Returned only when MFA is required. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


