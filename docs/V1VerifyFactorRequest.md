# V1VerifyFactorRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** | Provide the MFA device_id you are submitting for verification. The device_id is supplied by the Create Session Login Token API | 
**state_token** | **str** | Token of MFA device_id you are submitting for verification. The state_token is supplied by the Create Session Login Token API. | 
**otp_token** | **str** | Provide the OTP value for the MFA factor you are submitting for verification. | [optional] 
**do_not_notify** | **bool** | When verifying MFA via Protect Push, true stops additional push notifications being sent to the OneLogin Protect device. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


