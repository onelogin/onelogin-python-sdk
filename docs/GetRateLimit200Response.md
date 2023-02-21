# GetRateLimit200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**GenerateToken400Response**](GenerateToken400Response.md) |  | [optional] 
**data** | [**GetRateLimit200ResponseData**](GetRateLimit200ResponseData.md) |  | [optional] 

## Example

```python
from onelogin.models.get_rate_limit200_response import GetRateLimit200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetRateLimit200Response from a JSON string
get_rate_limit200_response_instance = GetRateLimit200Response.from_json(json)
# print the JSON string representation of the object
print GetRateLimit200Response.to_json()

# convert the object into a dict
get_rate_limit200_response_dict = get_rate_limit200_response_instance.to_dict()
# create an instance of GetRateLimit200Response from a dict
get_rate_limit200_response_form_dict = get_rate_limit200_response.from_dict(get_rate_limit200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


