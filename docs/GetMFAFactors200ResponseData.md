# GetMFAFactors200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_factors** | [**List[GetMFAFactors200ResponseDataAuthFactorsInner]**](GetMFAFactors200ResponseDataAuthFactorsInner.md) |  | [optional] 

## Example

```python
from onelogin.models.get_mfa_factors200_response_data import GetMFAFactors200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetMFAFactors200ResponseData from a JSON string
get_mfa_factors200_response_data_instance = GetMFAFactors200ResponseData.from_json(json)
# print the JSON string representation of the object
print GetMFAFactors200ResponseData.to_json()

# convert the object into a dict
get_mfa_factors200_response_data_dict = get_mfa_factors200_response_data_instance.to_dict()
# create an instance of GetMFAFactors200ResponseData from a dict
get_mfa_factors200_response_data_form_dict = get_mfa_factors200_response_data.from_dict(get_mfa_factors200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


