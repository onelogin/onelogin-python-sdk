# RiskRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** | The name of this rule | [optional] 
**description** | **str** |  | [optional] 
**type** | **str** | The type parameter specifies the type of rule that will be created. | [optional] 
**target** | **str** | The target parameter that will be used when evaluating the rule against an incoming event. | [optional] 
**filters** | **[str]** | A list of IP addresses or country codes or names to evaluate against each event. | [optional] 
**source** | [**Source**](Source.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


