# VerifyUserVerificationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**otp** | **str** | OTP code provided by the device or SMS message sent to user. | [optional] 
**device_id** | **int** | ID of the specified device which has been registerd for the given user. Available on Get Devices API call. | [optional] 

## Example

```python
from onelogin.models.verify_user_verification_request import VerifyUserVerificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyUserVerificationRequest from a JSON string
verify_user_verification_request_instance = VerifyUserVerificationRequest.from_json(json)
# print the JSON string representation of the object
print VerifyUserVerificationRequest.to_json()

# convert the object into a dict
verify_user_verification_request_dict = verify_user_verification_request_instance.to_dict()
# create an instance of VerifyUserVerificationRequest from a dict
verify_user_verification_request_form_dict = verify_user_verification_request.from_dict(verify_user_verification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


