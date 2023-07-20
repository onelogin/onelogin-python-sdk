# onelogin.model.auth_server_configuration.AuthServerConfiguration

Authorization server configuration

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Authorization server configuration | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**resource_identifier** | str,  | str,  | Unique identifier for the API that the Authorization Server will issue Access Tokens for. | 
**[audiences](#audiences)** | list, tuple,  | tuple,  | List of API endpoints that will be returned in Access Tokens. | 
**refresh_token_expiration_minutes** | decimal.Decimal, int,  | decimal.Decimal,  | The number of minutes until refresh token expires. There is no maximum expiry limit. | [optional] 
**access_token_expiration_minutes** | decimal.Decimal, int,  | decimal.Decimal,  | The number of minutes until access token expires. There is no maximum expiry limit. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# audiences

List of API endpoints that will be returned in Access Tokens.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of API endpoints that will be returned in Access Tokens. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

