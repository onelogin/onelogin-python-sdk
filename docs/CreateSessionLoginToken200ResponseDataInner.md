# CreateSessionLoginToken200ResponseDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **str** | Date and time when session token expires. Tokens expire 2 minutes after creation. Returned only when MFA is not required. | [optional] 
**return_to_url** | **str** | Returns the return_to_url value sent in the request, if applicable. Returned only when MFA is not required. | [optional] 
**session_token** | **str** | Provides the session token that can be used to log the user in. Returned only when MFA is not required. | [optional] 
**status** | **str** | username_or_email and password values sent are valid. Returned only when MFA is not required. | [optional] 
**user** | [**V1User**](V1User.md) |  | [optional] 
**state_token** | **str** | Value to submit with each Verify Factor API call until session login token is issued. Returned only when MFA required. | [optional] 
**callback_url** | **str** | Verify Factor API endpoint where device_id, state_token, and otp_token must be sent. Returned only when MFA is required. | [optional] 
**devices** | [**[CreateSessionLoginToken200ResponseDataInnerDevicesInner]**](CreateSessionLoginToken200ResponseDataInnerDevicesInner.md) | Provides device values that must be submitted with the Verify Factor API call. Returned only when MFA is required | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


