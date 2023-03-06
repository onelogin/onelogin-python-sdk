# AppParametersValue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_attribute_mappings** | **str** | A user attribute to map values from For custom attributes prefix the name of the attribute with &#x60;custom_attribute_&#x60;. e.g. To get the value for custom attribute &#x60;employee_id&#x60; use &#x60;custom_attribute_employee_id&#x60;. | [optional] 
**user_attribute_macros** | **str** | When &#x60;user_attribute_mappings&#x60; is set to &#x60;_macro_&#x60; this macro will be used to assign the parameter value. | [optional] 
**label** | **str** | The can only be set when creating a new parameter. It can not be updated. | [optional] 
**include_in_saml_assertion** | **bool** | When true, this parameter will be included in a SAML assertion payload. | [optional] 

## Example

```python
from onelogin.models.app_parameters_value import AppParametersValue

# TODO update the JSON string below
json = "{}"
# create an instance of AppParametersValue from a JSON string
app_parameters_value_instance = AppParametersValue.from_json(json)
# print the JSON string representation of the object
print AppParametersValue.to_json()

# convert the object into a dict
app_parameters_value_dict = app_parameters_value_instance.to_dict()
# create an instance of AppParametersValue from a dict
app_parameters_value_form_dict = app_parameters_value.from_dict(app_parameters_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


