# onelogin.model.risk_rule.RiskRule

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  |  | [optional] 
**name** | str,  | str,  | The name of this rule | [optional] 
**description** | str,  | str,  |  | [optional] 
**type** | str,  | str,  | The type parameter specifies the type of rule that will be created. | [optional] must be one of ["blacklist", "whitelist", ] 
**target** | str,  | str,  | The target parameter that will be used when evaluating the rule against an incoming event. | [optional] must be one of ["location.ip", "location.address.country_iso_code", ] 
**[filters](#filters)** | list, tuple,  | tuple,  | A list of IP addresses or country codes or names to evaluate against each event. | [optional] 
**source** | [**Source**](Source.md) | [**Source**](Source.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# filters

A list of IP addresses or country codes or names to evaluate against each event.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of IP addresses or country codes or names to evaluate against each event. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

