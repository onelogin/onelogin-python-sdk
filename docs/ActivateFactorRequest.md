# ActivateFactorRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** | Required. Specifies the factor to be verified. | [optional] 
**expires_in** | **int** | Optional. Sets the window of time in seconds that the factor must be verified within.  | [optional] 
**redirect_to** | **str** | Optional. Only applies to Email MagicLink factor. | [optional] 
**custom_message** | **str** | Optional. Only applies to SMS factor. A message template that will be sent via SMS. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


