# SamlAppAllOfParameters


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**saml_username** | [**SamlAppAllOfParametersSamlUsername**](SamlAppAllOfParametersSamlUsername.md) |  | 

## Example

```python
from onelogin.models.saml_app_all_of_parameters import SamlAppAllOfParameters

# TODO update the JSON string below
json = "{}"
# create an instance of SamlAppAllOfParameters from a JSON string
saml_app_all_of_parameters_instance = SamlAppAllOfParameters.from_json(json)
# print the JSON string representation of the object
print SamlAppAllOfParameters.to_json()

# convert the object into a dict
saml_app_all_of_parameters_dict = saml_app_all_of_parameters_instance.to_dict()
# create an instance of SamlAppAllOfParameters from a dict
saml_app_all_of_parameters_form_dict = saml_app_all_of_parameters.from_dict(saml_app_all_of_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


