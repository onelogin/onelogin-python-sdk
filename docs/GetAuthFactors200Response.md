# GetAuthFactors200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**factor_id** | **int** | Identifier for the factor which will be used for user enrollment | [optional] 
**name** | **str** | Authentication factor name, as it appears to administrators in OneLogin. | [optional] 
**auth_factor_name** | **str** | Internal use only | [optional] 

## Example

```python
from openapi_client.models.get_auth_factors200_response import GetAuthFactors200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAuthFactors200Response from a JSON string
get_auth_factors200_response_instance = GetAuthFactors200Response.from_json(json)
# print the JSON string representation of the object
print GetAuthFactors200Response.to_json()

# convert the object into a dict
get_auth_factors200_response_dict = get_auth_factors200_response_instance.to_dict()
# create an instance of GetAuthFactors200Response from a dict
get_auth_factors200_response_form_dict = get_auth_factors200_response.from_dict(get_auth_factors200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


