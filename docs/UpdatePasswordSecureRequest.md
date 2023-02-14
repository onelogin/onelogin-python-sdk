# UpdatePasswordSecureRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Set to the password value using a SHA-256-encoded value. If you are including your own password_salt value in your request, prepend the salt value to the cleartext password value before SHA-256-encoding it. For example, if your salt value is hello and your cleartext password value is password, the value you need to SHA-256-encode is hellopassword. The resulting encoded value would be b1c788abac15390de987ad17b65ac73c9b475d428a51f245c645a442fddd078b. Note that the alpha characters in this has must all be lower case. | 
**password_confirmation** | **str** | This value must match the password value. | 
**password_algorithm** | **str** | Set to salt+sha256. | 
**password_salt** | **str** | Optional. If your password hash has been salted then you can provide the salt used in this param. This assumes that the salt was prepended to the password before doing the SHA256 hash. The API supports a salt value that is up to 40 characters long. | [optional] 

## Example

```python
from openapi_client.models.update_password_secure_request import UpdatePasswordSecureRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePasswordSecureRequest from a JSON string
update_password_secure_request_instance = UpdatePasswordSecureRequest.from_json(json)
# print the JSON string representation of the object
print UpdatePasswordSecureRequest.to_json()

# convert the object into a dict
update_password_secure_request_dict = update_password_secure_request_instance.to_dict()
# create an instance of UpdatePasswordSecureRequest from a dict
update_password_secure_request_form_dict = update_password_secure_request.from_dict(update_password_secure_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


