# SsoSaml


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata_url** | **str** |  | [optional] 
**acs_url** | **str** |  | [optional] 
**sls_url** | **str** |  | [optional] 
**issuer** | **str** |  | [optional] 
**certificate** | [**SsoSamlAllOfCertificate**](SsoSamlAllOfCertificate.md) |  | [optional] 

## Example

```python
from onelogin.models.sso_saml import SsoSaml

# TODO update the JSON string below
json = "{}"
# create an instance of SsoSaml from a JSON string
sso_saml_instance = SsoSaml.from_json(json)
# print the JSON string representation of the object
print SsoSaml.to_json()

# convert the object into a dict
sso_saml_dict = sso_saml_instance.to_dict()
# create an instance of SsoSaml from a dict
sso_saml_form_dict = sso_saml.from_dict(sso_saml_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


