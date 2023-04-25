# AppParameters

The parameters section contains parameterized attributes that have defined at the connector level as well as custom attributes that have been defined specifically for this app. Regardless of how they are defined, all parameters have the following attributes. Each parameter is an object with the key for the object being set as the parameters short name.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_attribute_mappings** | **str** | A user attribute to map values from For custom attributes prefix the name of the attribute with &#x60;custom_attribute_&#x60;. e.g. To get the value for custom attribute &#x60;employee_id&#x60; use &#x60;custom_attribute_employee_id&#x60;. | [optional] 
**user_attribute_macros** | **str** | When &#x60;user_attribute_mappings&#x60; is set to &#x60;_macro_&#x60; this macro will be used to assign the parameter value. | [optional] 
**label** | **str** | The can only be set when creating a new parameter. It can not be updated. | [optional] 
**include_in_saml_assertion** | **bool** | When true, this parameter will be included in a SAML assertion payload. | [optional] 

## Example

```python
from onelogin.models.app_parameters import AppParameters

# TODO update the JSON string below
json = "{}"
# create an instance of AppParameters from a JSON string
app_parameters_instance = AppParameters.from_json(json)
# print the JSON string representation of the object
print AppParameters.to_json()

# convert the object into a dict
app_parameters_dict = app_parameters_instance.to_dict()
# create an instance of AppParameters from a dict
app_parameters_form_dict = app_parameters.from_dict(app_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


