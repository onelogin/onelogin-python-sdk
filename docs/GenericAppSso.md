# GenericAppSso


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | OIDC: The OpenId Connect Client Id.  Note that client_secret is only returned after Creating an App | [optional] 
**metadata_url** | **str** |  | [optional] 
**acs_url** | **str** |  | [optional] 
**sls_url** | **str** |  | [optional] 
**issuer** | **str** |  | [optional] 
**certificate** | [**SsoSamlAllOfCertificate**](SsoSamlAllOfCertificate.md) |  | [optional] 

## Example

```python
from onelogin.models.generic_app_sso import GenericAppSso

# TODO update the JSON string below
json = "{}"
# create an instance of GenericAppSso from a JSON string
generic_app_sso_instance = GenericAppSso.from_json(json)
# print the JSON string representation of the object
print GenericAppSso.to_json()

# convert the object into a dict
generic_app_sso_dict = generic_app_sso_instance.to_dict()
# create an instance of GenericAppSso from a dict
generic_app_sso_form_dict = generic_app_sso.from_dict(generic_app_sso_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


