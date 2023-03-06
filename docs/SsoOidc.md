# SsoOidc


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** | OIDC: The OpenId Connect Client Id.  Note that client_secret is only returned after Creating an App | [optional] 

## Example

```python
from onelogin.models.sso_oidc import SsoOidc

# TODO update the JSON string below
json = "{}"
# create an instance of SsoOidc from a JSON string
sso_oidc_instance = SsoOidc.from_json(json)
# print the JSON string representation of the object
print SsoOidc.to_json()

# convert the object into a dict
sso_oidc_dict = sso_oidc_instance.to_dict()
# create an instance of SsoOidc from a dict
sso_oidc_form_dict = sso_oidc.from_dict(sso_oidc_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


