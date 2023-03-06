# ConfigurationOidcAllOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_url** | **str** | The OpenId Connect Client Id. Note that client_secret is only returned after Creating an App. | 
**redirect_uri** | **str** | Comma or newline separated list of valid redirect uris for the OpenId Connect Authorization Code flow. | 
**access_token_expiration_minutes** | **int** | Number of minutes the refresh token will be valid for. | 
**refresh_token_expiration_minutes** | **int** | Number of minutes the refresh token will be valid for. | 
**token_endpoint_auth_method** | **int** | Endpoint Auth Methods:   - 0: Basic   - 1: POST   - 2: None / PKCE | 
**oidc_application_type** | **int** | Application Types:   - 0: Web   - 1: Native / Mobile | 

## Example

```python
from onelogin.models.configuration_oidc_all_of import ConfigurationOidcAllOf

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationOidcAllOf from a JSON string
configuration_oidc_all_of_instance = ConfigurationOidcAllOf.from_json(json)
# print the JSON string representation of the object
print ConfigurationOidcAllOf.to_json()

# convert the object into a dict
configuration_oidc_all_of_dict = configuration_oidc_all_of_instance.to_dict()
# create an instance of ConfigurationOidcAllOf from a dict
configuration_oidc_all_of_form_dict = configuration_oidc_all_of.from_dict(configuration_oidc_all_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


