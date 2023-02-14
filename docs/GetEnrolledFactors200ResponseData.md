# GetEnrolledFactors200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**otp_devices** | [**List[GetEnrolledFactors200ResponseDataOtpDevicesInner]**](GetEnrolledFactors200ResponseDataOtpDevicesInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_enrolled_factors200_response_data import GetEnrolledFactors200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetEnrolledFactors200ResponseData from a JSON string
get_enrolled_factors200_response_data_instance = GetEnrolledFactors200ResponseData.from_json(json)
# print the JSON string representation of the object
print GetEnrolledFactors200ResponseData.to_json()

# convert the object into a dict
get_enrolled_factors200_response_data_dict = get_enrolled_factors200_response_data_instance.to_dict()
# create an instance of GetEnrolledFactors200ResponseData from a dict
get_enrolled_factors200_response_data_form_dict = get_enrolled_factors200_response_data.from_dict(get_enrolled_factors200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


