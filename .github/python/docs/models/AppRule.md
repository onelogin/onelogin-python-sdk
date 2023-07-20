# onelogin.model.app_rule.AppRule

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  | App Rule ID | [optional] 
**name** | str,  | str,  | Rule Name | [optional] 
**match** | str,  | str,  | Indicates how conditions should be matched. | [optional] must be one of ["all", "any", ] 
**enabled** | bool,  | BoolClass,  | Indicates if the rule is enabled or not. | [optional] 
**position** | decimal.Decimal, int,  | decimal.Decimal,  | Indicates the order of the rule. When &#x60;null&#x60; this will default to last position. | [optional] 
**[conditions](#conditions)** | list, tuple,  | tuple,  | An array of conditions that the user must meet in order for the rule to be applied. | [optional] 
**[actions](#actions)** | list, tuple,  | tuple,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# conditions

An array of conditions that the user must meet in order for the rule to be applied.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of conditions that the user must meet in order for the rule to be applied. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Condition**](Condition.md) | [**Condition**](Condition.md) | [**Condition**](Condition.md) |  | 

# actions

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ActionObj**](ActionObj.md) | [**ActionObj**](ActionObj.md) | [**ActionObj**](ActionObj.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

