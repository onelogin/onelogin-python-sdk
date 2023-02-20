# GenerateMFAtoken200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mfa_token** | **str** | Token can function as a temporary MFA token. It can be used to authenticate for any app when valid. | [optional] 
**resuable** | **bool** | true indcates the token can be used multiple times, until it expires. false indicates the token is invalid after a single use or once it expires. Defaults to false. | [optional] 
**expires_at** | **str** | Defines the expiration time and date for the token. Format is UTC time. | [optional] 

## Example

```python
from openapi_client.models.generate_mf_atoken200_response import GenerateMFAtoken200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateMFAtoken200Response from a JSON string
generate_mf_atoken200_response_instance = GenerateMFAtoken200Response.from_json(json)
# print the JSON string representation of the object
print GenerateMFAtoken200Response.to_json()

# convert the object into a dict
generate_mf_atoken200_response_dict = generate_mf_atoken200_response_instance.to_dict()
# create an instance of GenerateMFAtoken200Response from a dict
generate_mf_atoken200_response_form_dict = generate_mf_atoken200_response.from_dict(generate_mf_atoken200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


