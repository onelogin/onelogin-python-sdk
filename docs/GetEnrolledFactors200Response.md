# GetEnrolledFactors200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**GenerateToken400Response**](GenerateToken400Response.md) |  | [optional] 
**data** | [**GetEnrolledFactors200ResponseData**](GetEnrolledFactors200ResponseData.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_enrolled_factors200_response import GetEnrolledFactors200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEnrolledFactors200Response from a JSON string
get_enrolled_factors200_response_instance = GetEnrolledFactors200Response.from_json(json)
# print the JSON string representation of the object
print GetEnrolledFactors200Response.to_json()

# convert the object into a dict
get_enrolled_factors200_response_dict = get_enrolled_factors200_response_instance.to_dict()
# create an instance of GetEnrolledFactors200Response from a dict
get_enrolled_factors200_response_form_dict = get_enrolled_factors200_response.from_dict(get_enrolled_factors200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


