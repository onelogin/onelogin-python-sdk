# onelogin.model.mapping.Mapping

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**match** | str,  | str,  | Indicates how conditions should be matched. | must be one of ["all", "any", ] 
**name** | str,  | str,  | The name of the mapping. | 
**position** | decimal.Decimal, int,  | decimal.Decimal,  | Indicates the order of the mapping. When &#x60;null&#x60; this will default to last position. | 
**[conditions](#conditions)** | list, tuple,  | tuple,  | An array of conditions that the user must meet in order for the mapping to be applied. | 
**[actions](#actions)** | list, tuple,  | tuple,  | An array of actions that will be applied to the users that are matched by the conditions. | 
**enabled** | bool,  | BoolClass,  | Indicates if the mapping is enabled or not. | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# conditions

An array of conditions that the user must meet in order for the mapping to be applied.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of conditions that the user must meet in order for the mapping to be applied. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Condition**](Condition.md) | [**Condition**](Condition.md) | [**Condition**](Condition.md) |  | 

# actions

An array of actions that will be applied to the users that are matched by the conditions.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of actions that will be applied to the users that are matched by the conditions. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**ActionObj**](ActionObj.md) | [**ActionObj**](ActionObj.md) | [**ActionObj**](ActionObj.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

