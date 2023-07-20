# onelogin.model.auth_server.AuthServer

base resource for configuring api authorization in OneLogin

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | base resource for configuring api authorization in OneLogin | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**configuration** | [**AuthServerConfiguration**](AuthServerConfiguration.md) | [**AuthServerConfiguration**](AuthServerConfiguration.md) |  | 
**name** | str,  | str,  | Name of the API. | 
**description** | str,  | str,  | Description of what the API does. | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  | Auth server unique ID in Onelogin | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

