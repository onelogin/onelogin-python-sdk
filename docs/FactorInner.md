# FactorInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | MFA device identifier. | [optional] 
**status** | **str** | accepted : factor has been verified. pending: registered but has not been verified. | [optional] 
**default** | **bool** | True &#x3D; is user&#39;s default MFA device for OneLogin. | [optional] 
**auth_factor_name** | **str** | \&quot;Official\&quot; authentication factor name, as it appears to administrators in OneLogin. | [optional] 
**type_display_name** | **str** | Authentication factor display name as it appears to users upon initial registration, as defined by admins at Settings &gt; Authentication Factors. | [optional] 
**user_display_name** | **str** | Authentication factor display name assigned by users when they enroll the device. | [optional] 
**expires_at** | **str** | A short lived token that is required to Verify the Factor. This token expires based on the expires_in parameter passed in. | [optional] 
**factor_data** | [**FactorInnerFactorData**](FactorInnerFactorData.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


