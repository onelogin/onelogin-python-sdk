# EnrollFactorRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**factor_id** | **int** | The identifier of the factor to enroll the user with. | 
**display_name** | **str** | A name for the users device. | 
**expires_in** | **str** | Defaults to 120. Valid values are: 120-900 seconds. | [optional] 
**verified** | **bool** | Defaults to false. | [optional] 
**redirect_to** | **str** | Redirects MagicLink success page to specified URL after 2 seconds. | [optional] 
**custom_message** | **str** | A message template that will be sent via SMS. Max length of the message after template items are inserted is 160 characters including the OTP code. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


