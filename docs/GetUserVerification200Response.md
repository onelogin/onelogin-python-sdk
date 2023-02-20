# GetUserVerification200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | registration identifier | [optional] 
**status** | **str** | pending &#x3D; has not been completed. accepted registration has successfully completed, rejected user has denied the MFA attempt or incorrectly provided the OneLogin Voice OTP code. | [optional] 
**device_id** | **str** | Device Id to be used with verify factor | [optional] 

## Example

```python
from openapi_client.models.get_user_verification200_response import GetUserVerification200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserVerification200Response from a JSON string
get_user_verification200_response_instance = GetUserVerification200Response.from_json(json)
# print the JSON string representation of the object
print GetUserVerification200Response.to_json()

# convert the object into a dict
get_user_verification200_response_dict = get_user_verification200_response_instance.to_dict()
# create an instance of GetUserVerification200Response from a dict
get_user_verification200_response_form_dict = get_user_verification200_response.from_dict(get_user_verification200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


