# GetRateLimit200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**x_rate_limit_limit** | **int** | Rate Limit Limit | [optional] 
**x_rate_limit_remaining** | **int** | Rate Limit Remaining | [optional] 
**x_rate_limit_reset** | **int** | Rate Limit Reset | [optional] 

## Example

```python
from onelogin.models.get_rate_limit200_response_data import GetRateLimit200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetRateLimit200ResponseData from a JSON string
get_rate_limit200_response_data_instance = GetRateLimit200ResponseData.from_json(json)
# print the JSON string representation of the object
print GetRateLimit200ResponseData.to_json()

# convert the object into a dict
get_rate_limit200_response_data_dict = get_rate_limit200_response_data_instance.to_dict()
# create an instance of GetRateLimit200ResponseData from a dict
get_rate_limit200_response_data_form_dict = get_rate_limit200_response_data.from_dict(get_rate_limit200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


