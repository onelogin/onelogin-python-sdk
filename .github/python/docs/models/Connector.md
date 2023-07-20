# onelogin.model.connector.Connector

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  | Connectors unique ID in OneLogin. | [optional] 
**name** | str,  | str,  | Name of Connector | [optional] 
**icon_url** | str,  | str,  | A link to the icon&#x27;s url. | [optional] 
**auth_method** | [**AuthMethod**](AuthMethod.md) | [**AuthMethod**](AuthMethod.md) |  | [optional] 
**allows_new_parameters** | bool,  | BoolClass,  | Indicates if apps created using this connector will be allowed to create custom parameters. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

