# V1VerifyFactor200ResponseDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expires_at** | **str** | Date and time at which the session token will expire. Tokens expire two minutes after creation. | [optional] 
**return_to_url** | **str** | Returns the return_to_url value sent in the request, if applicable. | [optional] 
**session_token** | **str** | Provides the session token that can be used to log the user in. | [optional] 
**status** | **str** | Authenticated: Indicates that the username_or_email and password values sent in the request are valid. | [optional] 
**user** | [**V1User**](V1User.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


