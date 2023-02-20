# VerifyUserRegistrationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**otp** | **int** | One-Time-Password (OTP) that was sent to the user based on the chosen factor. OneLogin SMS and OneLogin Email support this OTP code. | [optional] 

## Example

```python
from openapi_client.models.verify_user_registration_request import VerifyUserRegistrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyUserRegistrationRequest from a JSON string
verify_user_registration_request_instance = VerifyUserRegistrationRequest.from_json(json)
# print the JSON string representation of the object
print VerifyUserRegistrationRequest.to_json()

# convert the object into a dict
verify_user_registration_request_dict = verify_user_registration_request_instance.to_dict()
# create an instance of VerifyUserRegistrationRequest from a dict
verify_user_registration_request_form_dict = verify_user_registration_request.from_dict(verify_user_registration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


