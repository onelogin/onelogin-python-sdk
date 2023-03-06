# ConfigurationSamlAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signature_algorithm** | **str** | One of the following:   - SHA-1   - SHA-256   - SHA-348   - SHA-512 | 
**certificate_id** | **int** | When creating apps the default certificate will be used unless the &#x60;certificate_id&#x60; attribute is applied in the &#x60;configuration&#x60; object. | [optional] 

## Example

```python
from onelogin.models.configuration_saml_all_of import ConfigurationSamlAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationSamlAllOf from a JSON string
configuration_saml_all_of_instance = ConfigurationSamlAllOf.from_json(json)
# print the JSON string representation of the object
print ConfigurationSamlAllOf.to_json()

# convert the object into a dict
configuration_saml_all_of_dict = configuration_saml_all_of_instance.to_dict()
# create an instance of ConfigurationSamlAllOf from a dict
configuration_saml_all_of_form_dict = configuration_saml_all_of.from_dict(configuration_saml_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


