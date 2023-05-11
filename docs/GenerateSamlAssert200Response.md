# GenerateSamlAssert200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Error**](Error.md) |  | [optional] 
**data** | **List[object]** |  | [optional] 

## Example

```python
from onelogin.models.generate_saml_assert200_response import GenerateSamlAssert200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateSamlAssert200Response from a JSON string
generate_saml_assert200_response_instance = GenerateSamlAssert200Response.from_json(json)
# print the JSON string representation of the object
print GenerateSamlAssert200Response.to_json()

# convert the object into a dict
generate_saml_assert200_response_dict = generate_saml_assert200_response_instance.to_dict()
# create an instance of GenerateSamlAssert200Response from a dict
generate_saml_assert200_response_form_dict = generate_saml_assert200_response.from_dict(generate_saml_assert200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


