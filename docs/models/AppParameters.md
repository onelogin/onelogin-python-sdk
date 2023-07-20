# onelogin.model.app_parameters.AppParameters

The parameters section contains parameterized attributes that have defined at the connector level as well as custom attributes that have been defined specifically for this app. Regardless of how they are defined, all parameters have the following attributes. Each parameter is an object with the key for the object being set as the parameters short name.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The parameters section contains parameterized attributes that have defined at the connector level as well as custom attributes that have been defined specifically for this app. Regardless of how they are defined, all parameters have the following attributes. Each parameter is an object with the key for the object being set as the parameters short name. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**user_attribute_mappings** | str,  | str,  | A user attribute to map values from For custom attributes prefix the name of the attribute with &#x60;custom_attribute_&#x60;. e.g. To get the value for custom attribute &#x60;employee_id&#x60; use &#x60;custom_attribute_employee_id&#x60;. | [optional] 
**user_attribute_macros** | str,  | str,  | When &#x60;user_attribute_mappings&#x60; is set to &#x60;_macro_&#x60; this macro will be used to assign the parameter value. | [optional] 
**label** | str,  | str,  | The can only be set when creating a new parameter. It can not be updated. | [optional] 
**include_in_saml_assertion** | bool,  | BoolClass,  | When true, this parameter will be included in a SAML assertion payload. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

