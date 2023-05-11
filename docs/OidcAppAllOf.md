# OidcAppAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**configuration** | [**ConfigurationOidc**](ConfigurationOidc.md) |  | 
**sso** | [**SsoOidc**](SsoOidc.md) |  | [optional] 

## Example

```python
from onelogin.models.oidc_app_all_of import OidcAppAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of OidcAppAllOf from a JSON string
oidc_app_all_of_instance = OidcAppAllOf.from_json(json)
# print the JSON string representation of the object
print OidcAppAllOf.to_json()

# convert the object into a dict
oidc_app_all_of_dict = oidc_app_all_of_instance.to_dict()
# create an instance of OidcAppAllOf from a dict
oidc_app_all_of_form_dict = oidc_app_all_of.from_dict(oidc_app_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


