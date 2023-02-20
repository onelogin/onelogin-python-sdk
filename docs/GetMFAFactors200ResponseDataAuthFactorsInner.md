# GetMFAFactors200ResponseDataAuthFactorsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Official authentication factor name, as it appears to administrators in OneLogin. | [optional] 
**factor_id** | **int** | Identifier for the factor which will be used for user enrollment | [optional] 

## Example

```python
from openapi_client.models.get_mfa_factors200_response_data_auth_factors_inner import GetMFAFactors200ResponseDataAuthFactorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetMFAFactors200ResponseDataAuthFactorsInner from a JSON string
get_mfa_factors200_response_data_auth_factors_inner_instance = GetMFAFactors200ResponseDataAuthFactorsInner.from_json(json)
# print the JSON string representation of the object
print GetMFAFactors200ResponseDataAuthFactorsInner.to_json()

# convert the object into a dict
get_mfa_factors200_response_data_auth_factors_inner_dict = get_mfa_factors200_response_data_auth_factors_inner_instance.to_dict()
# create an instance of GetMFAFactors200ResponseDataAuthFactorsInner from a dict
get_mfa_factors200_response_data_auth_factors_inner_form_dict = get_mfa_factors200_response_data_auth_factors_inner.from_dict(get_mfa_factors200_response_data_auth_factors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


