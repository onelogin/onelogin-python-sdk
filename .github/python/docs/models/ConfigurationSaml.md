# onelogin.model.configuration_saml.ConfigurationSaml

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**signature_algorithm** | str,  | str,  | One of the following:   - SHA-1   - SHA-256   - SHA-348   - SHA-512 | [optional] 
**certificate_id** | decimal.Decimal, int,  | decimal.Decimal,  | When creating apps the default certificate will be used unless the &#x60;certificate_id&#x60; attribute is applied in the &#x60;configuration&#x60; object. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

