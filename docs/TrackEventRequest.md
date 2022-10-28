# TrackEventRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verb** | **str** | Verbs are used to distinguish between different types of events. | 
**ip** | **str** | The IP address of the User&#39;s request. | 
**user_agent** | **str** | The user agent of the User&#39;s request. | 
**user** | [**RiskUser**](RiskUser.md) |  | 
**source** | [**Source**](Source.md) |  | [optional] 
**session** | [**Session**](Session.md) |  | [optional] 
**device** | [**RiskDevice**](RiskDevice.md) |  | [optional] 
**fp** | **str** | Set to the value of the __tdli_fp cookie. | [optional] 
**published** | **str** | Date and time of the event in IS08601 format. Useful for preloading old events. Defaults to date time this API request is received. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


