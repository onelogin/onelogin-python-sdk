# onelogin.model.saml_assert.SamlAssert

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**password** | str,  | str,  | Password of the OneLogin user accessing the app for which you want to generate a SAML token. | 
**subdomain** | str,  | str,  | Set to the subdomain of the OneLogin user accessing the app for which you want to generate a SAML token. | 
**username_or_email** | str,  | str,  | Set this to the username or email of the OneLogin user accessing the app for which you want to generate a SAML token. | 
**app_id** | str,  | str,  | App ID of the app for which you want to generate a SAML token. This is the app ID in OneLogin. | 
**ip_address** | str,  | str,  | If you are using this API in a scenario in which MFA is required and you’ll need to be able to honor IP address whitelisting defined in MFA policies, provide this parameter and set its value to the whitelisted IP address that needs to be bypassed. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

