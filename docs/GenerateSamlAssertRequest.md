# GenerateSamlAssertRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username_or_email** | **str** | Set this to the username or email of the OneLogin user accessing the app for which you want to generate a SAML token. | 
**password** | **str** | Password of the OneLogin user accessing the app for which you want to generate a SAML token. | 
**app_id** | **str** | App ID of the app for which you want to generate a SAML token. This is the app ID in OneLogin. | 
**subdomain** | **str** | Set to the subdomain of the OneLogin user accessing the app for which you want to generate a SAML token. | 
**ip_address** | **str** | If you are using this API in a scenario in which MFA is required and you’ll need to be able to honor IP address whitelisting defined in MFA policies, provide this parameter and set its value to the whitelisted IP address that needs to be bypassed. | [optional] 

## Example

```python
from onelogin.models.generate_saml_assert_request import GenerateSamlAssertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateSamlAssertRequest from a JSON string
generate_saml_assert_request_instance = GenerateSamlAssertRequest.from_json(json)
# print the JSON string representation of the object
print GenerateSamlAssertRequest.to_json()

# convert the object into a dict
generate_saml_assert_request_dict = generate_saml_assert_request_instance.to_dict()
# create an instance of GenerateSamlAssertRequest from a dict
generate_saml_assert_request_form_dict = generate_saml_assert_request.from_dict(generate_saml_assert_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


