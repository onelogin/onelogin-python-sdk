# VerFactorSaml200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | Provides the SAML assertion. | [optional] 
**message** | **str** | Plain text description describing the outcome of the response. | [optional] 

## Example

```python
from onelogin.models.ver_factor_saml200_response import VerFactorSaml200Response

# TODO update the JSON string below
json = "{}"
# create an instance of VerFactorSaml200Response from a JSON string
ver_factor_saml200_response_instance = VerFactorSaml200Response.from_json(json)
# print the JSON string representation of the object
print VerFactorSaml200Response.to_json()

# convert the object into a dict
ver_factor_saml200_response_dict = ver_factor_saml200_response_instance.to_dict()
# create an instance of VerFactorSaml200Response from a dict
ver_factor_saml200_response_form_dict = ver_factor_saml200_response.from_dict(ver_factor_saml200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


