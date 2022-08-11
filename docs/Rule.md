# Rule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** | The name of the rule. | [optional] 
**match** | **str** | Indicates how conditions should be matched. | [optional] 
**enabled** | **bool** | Indicates if the rule is enabled or not. | [optional] 
**position** | **int** | Indicates the order of the rule. When &#x60;null&#x60; this will default to last position. | [optional] 
**conditions** | [**[Condition]**](Condition.md) | An array of conditions that the user must meet in order for the rule to be applied. | [optional] 
**actions** | [**[Action]**](Action.md) | An array of actions that will be applied to the users that are matched by the conditions. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


