# onelogin.model.oauth_token.OauthToken

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**access_token** | str,  | str,  | Provides the requested access token. You can use this token to call our resource APIs. | [optional] 
**created_at** | str,  | str,  | Time at which the access token was generated. | [optional] 
**expires_in** | decimal.Decimal, int,  | decimal.Decimal,  | Indicates that the generated access token expires in 36,000 seconds, 600 minutes, or 10 hours. An expired access token cannot be used to make resource API calls, but it can still be used along with its associated refresh token to call the Refresh Tokens v2 API. | [optional] 
**refresh_token** | str,  | str,  | deprecated No longer in use | [optional] 
**token_type** | str,  | str,  | Indicates that the generated access token is a bearer token. | [optional] 
**account_id** | decimal.Decimal, int,  | decimal.Decimal,  | Account ID associated with the API credentials used to generate the token. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

