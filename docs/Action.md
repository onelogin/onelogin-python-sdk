# Action


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action to apply | [optional] 
**value** | **[str]** | Only applicable to provisioned and set_* actions. Items in the array will be a plain text string or valid value for the selected action. | [optional] 
**expression** | **str** | A regular expression to extract a value. Applies to provisionable, multi-selects, and string actions. | [optional] 
**scriplet** | **str** | A hash containing scriptlet code that returns a value. | [optional] 
**macro** | **str** | A template to construct a value. Applies to default, string, and list actions. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


