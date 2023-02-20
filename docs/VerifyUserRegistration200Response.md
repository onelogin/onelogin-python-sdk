# VerifyUserRegistration200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Registration identifier. | [optional] 
**status** | **str** | pending registration has not been completed successfully. accepted registration has successfully completed. | [optional] 
**device_id** | **str** | Device id to be used with Verify the Factor. | [optional] 

## Example

```python
from openapi_client.models.verify_user_registration200_response import VerifyUserRegistration200Response

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyUserRegistration200Response from a JSON string
verify_user_registration200_response_instance = VerifyUserRegistration200Response.from_json(json)
# print the JSON string representation of the object
print VerifyUserRegistration200Response.to_json()

# convert the object into a dict
verify_user_registration200_response_dict = verify_user_registration200_response_instance.to_dict()
# create an instance of VerifyUserRegistration200Response from a dict
verify_user_registration200_response_form_dict = verify_user_registration200_response.from_dict(verify_user_registration200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


