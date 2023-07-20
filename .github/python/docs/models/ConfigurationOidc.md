# onelogin.model.configuration_oidc.ConfigurationOidc

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**login_url** | str,  | str,  | The OpenId Connect Client Id. Note that client_secret is only returned after Creating an App. | 
**access_token_expiration_minutes** | decimal.Decimal, int,  | decimal.Decimal,  | Number of minutes the refresh token will be valid for. | 
**refresh_token_expiration_minutes** | decimal.Decimal, int,  | decimal.Decimal,  | Number of minutes the refresh token will be valid for. | 
**redirect_uri** | str,  | str,  | Comma or newline separated list of valid redirect uris for the OpenId Connect Authorization Code flow. | 
**oidc_application_type** | decimal.Decimal, int,  | decimal.Decimal,  | - 0 : Web - 1 : Native / Mobile | must be one of [0, 1, ] 
**token_endpoint_auth_method** | decimal.Decimal, int,  | decimal.Decimal,  | - 0: Basic - 1: POST - 2: None / PKCE | must be one of [0, 1, 2, ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

