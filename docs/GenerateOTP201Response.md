# GenerateOTP201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mfa_token** | **str** | Token can function as a temporary MFA token. It can be used to authenticate for any app when valid. | [optional] 
**reusable** | **bool** | true indcates the token can be used multiple times, until it expires. false indicates the token is invalid after a single use or once it expires. Defaults to false. | [optional] [default to False]
**expires_at** | **str** | Defines the expiration time and date for the token. Format is UTC time. | [optional] 
**device_id** | **str** | A unique identifier for the temp otp device that has been created for this token. | [optional] 

## Example

```python
from onelogin.models.generate_otp201_response import GenerateOTP201Response

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateOTP201Response from a JSON string
generate_otp201_response_instance = GenerateOTP201Response.from_json(json)
# print the JSON string representation of the object
print GenerateOTP201Response.to_json()

# convert the object into a dict
generate_otp201_response_dict = generate_otp201_response_instance.to_dict()
# create an instance of GenerateOTP201Response from a dict
generate_otp201_response_form_dict = generate_otp201_response.from_dict(generate_otp201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


