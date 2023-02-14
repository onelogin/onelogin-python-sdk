# UpdatePasswordInsecureRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Set to the password value using cleartext. Hashes are never stored as cleartext. They are stored securely using cryptographic hash. OneLogin continuously upgrades the strength of the hash. Ensure that the value meets the password strength requirements set for the account. | 
**password_confirmation** | **str** | Ensure that this value matches the password value exactly. | 
**validate_policy** | **bool** | Will passwords validate against the User Policy. Defaults to false. | [optional] [default to False]

## Example

```python
from openapi_client.models.update_password_insecure_request import UpdatePasswordInsecureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePasswordInsecureRequest from a JSON string
update_password_insecure_request_instance = UpdatePasswordInsecureRequest.from_json(json)
# print the JSON string representation of the object
print UpdatePasswordInsecureRequest.to_json()

# convert the object into a dict
update_password_insecure_request_dict = update_password_insecure_request_instance.to_dict()
# create an instance of UpdatePasswordInsecureRequest from a dict
update_password_insecure_request_form_dict = update_password_insecure_request.from_dict(update_password_insecure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


