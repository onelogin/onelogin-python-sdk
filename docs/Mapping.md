# Mapping


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the mapping. | 
**enabled** | **bool** | Indicates if the mapping is enabled or not. | 
**match** | **str** | Indicates how conditions should be matched. | 
**position** | **int** | Indicates the order of the mapping. When &#x60;null&#x60; this will default to last position. | 
**actions** | [**[Action]**](Action.md) | An array of actions that will be applied to the users that are matched by the conditions. | 
**id** | **int** |  | [optional] 
**conditions** | [**[Condition]**](Condition.md) | An array of conditions that the user must meet in order for the mapping to be applied. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


