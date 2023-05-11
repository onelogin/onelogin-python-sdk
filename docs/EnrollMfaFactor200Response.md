# EnrollMfaFactor200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Error**](Error.md) |  | [optional] 
**data** | [**List[GetEnrolledFactors200ResponseDataOtpDevicesInner]**](GetEnrolledFactors200ResponseDataOtpDevicesInner.md) |  | [optional] 

## Example

```python
from onelogin.models.enroll_mfa_factor200_response import EnrollMfaFactor200Response

# TODO update the JSON string below
json = "{}"
# create an instance of EnrollMfaFactor200Response from a JSON string
enroll_mfa_factor200_response_instance = EnrollMfaFactor200Response.from_json(json)
# print the JSON string representation of the object
print EnrollMfaFactor200Response.to_json()

# convert the object into a dict
enroll_mfa_factor200_response_dict = enroll_mfa_factor200_response_instance.to_dict()
# create an instance of EnrollMfaFactor200Response from a dict
enroll_mfa_factor200_response_form_dict = enroll_mfa_factor200_response.from_dict(enroll_mfa_factor200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


