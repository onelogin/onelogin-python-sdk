# onelogin.model.token_claim.TokenClaim

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  | The unique ID of the claim. | [optional] 
**label** | str,  | str,  | The UI label for the claims. | [optional] 
**user_attribute_mappings** | str,  | str,  | A user attribute to map values from. | [optional] 
**user_attribute_macros** | str,  | str,  | When &#x60;user_attribute_mappings&#x60; is set to &#x60;_macro_&#x60; this macro will be used to assign the claims value. | [optional] 
**attribute_transformations** | str,  | str,  | The type of transformation to perform on multi valued attributes. | [optional] 
**skip_if_blank** | bool,  | BoolClass,  | not used | [optional] 
**[values](#values)** | list, tuple,  | tuple,  | Relates to Rules/Entitlements. Not supported yet. | [optional] 
**default_values** | str,  | str,  | Relates to Rules/Entitlements. Not supported yet. | [optional] 
**provisioned_entitlements** | bool,  | BoolClass,  | Relates to Rules/Entitlements. Not supported yet. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# values

Relates to Rules/Entitlements. Not supported yet.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Relates to Rules/Entitlements. Not supported yet. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

