# ConfigurationOidc


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
from onelogin.models.configuration_oidc import ConfigurationOidc

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationOidc from a JSON string
configuration_oidc_instance = ConfigurationOidc.from_json(json)
# print the JSON string representation of the object
print ConfigurationOidc.to_json()

# convert the object into a dict
configuration_oidc_dict = configuration_oidc_instance.to_dict()
# create an instance of ConfigurationOidc from a dict
configuration_oidc_form_dict = configuration_oidc.from_dict(configuration_oidc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


