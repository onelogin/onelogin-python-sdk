# GenericAppConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_url** | **str** | The OpenId Connect Client Id. Note that client_secret is only returned after Creating an App. | 
**redirect_uri** | **str** | Comma or newline separated list of valid redirect uris for the OpenId Connect Authorization Code flow. | 
**access_token_expiration_minutes** | **int** | Number of minutes the refresh token will be valid for. | 
**refresh_token_expiration_minutes** | **int** | Number of minutes the refresh token will be valid for. | 
**token_endpoint_auth_method** | **int** | Endpoint Auth Methods:   - 0: Basic   - 1: POST   - 2: None / PKCE | 
**oidc_application_type** | **int** | Application Types:   - 0: Web   - 1: Native / Mobile | 
**signature_algorithm** | **str** | One of the following:   - SHA-1   - SHA-256   - SHA-348   - SHA-512 | 
**certificate_id** | **int** | When creating apps the default certificate will be used unless the &#x60;certificate_id&#x60; attribute is applied in the &#x60;configuration&#x60; object. | [optional] 

## Example

```python
from onelogin.models.generic_app_configuration import GenericAppConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of GenericAppConfiguration from a JSON string
generic_app_configuration_instance = GenericAppConfiguration.from_json(json)
# print the JSON string representation of the object
print GenericAppConfiguration.to_json()

# convert the object into a dict
generic_app_configuration_dict = generic_app_configuration_instance.to_dict()
# create an instance of GenericAppConfiguration from a dict
generic_app_configuration_form_dict = generic_app_configuration.from_dict(generic_app_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


