# onelogin.model.hook_envvar.HookEnvvar

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The name of the environment variable. | 
**value** | str,  | str,  | The secret value that will be encrypted at rest and injected in applicable hook functions at run time. | 
**id** | str,  | str,  | A unique identifier for the Hook Environment Variable | [optional] 
**created_at** | str,  | str,  | The ISO8601 formatted date that the environment variable was created. | [optional] 
**updated_at** | str,  | str,  | The ISO8601 formatted date that the environment variable was last updated. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

