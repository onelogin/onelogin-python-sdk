# SsoSamlCertificate

The Certificate used for signing

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | SAML Certificate ID | [optional] 
**name** | **str** | SAML Certificate Name | [optional] 
**value** | **str** | SAML Certificate Value | [optional] 

## Example

```python
from onelogin.models.sso_saml_certificate import SsoSamlCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of SsoSamlCertificate from a JSON string
sso_saml_certificate_instance = SsoSamlCertificate.from_json(json)
# print the JSON string representation of the object
print SsoSamlCertificate.to_json()

# convert the object into a dict
sso_saml_certificate_dict = sso_saml_certificate_instance.to_dict()
# create an instance of SsoSamlCertificate from a dict
sso_saml_certificate_form_dict = sso_saml_certificate.from_dict(sso_saml_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


