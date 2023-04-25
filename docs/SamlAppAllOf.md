# SamlAppAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**ConfigurationSaml**](ConfigurationSaml.md) |  | [optional] 
**sso** | [**SsoSaml**](SsoSaml.md) |  | [optional] 
**parameters** | [**SamlAppAllOfParameters**](SamlAppAllOfParameters.md) |  | [optional] 

## Example

```python
from onelogin.models.saml_app_all_of import SamlAppAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of SamlAppAllOf from a JSON string
saml_app_all_of_instance = SamlAppAllOf.from_json(json)
# print the JSON string representation of the object
print SamlAppAllOf.to_json()

# convert the object into a dict
saml_app_all_of_dict = saml_app_all_of_instance.to_dict()
# create an instance of SamlAppAllOf from a dict
saml_app_all_of_form_dict = saml_app_all_of.from_dict(saml_app_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


