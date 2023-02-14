# CreateFactorRegistrationRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**factor_id** | **int** | The identifier of the factor to enroll the user with. See Get Available Factors for a list of possible id values. | 
**display_name** | **str** | A name for the users device | 
**expires_in** | **str** | Defaults to 120. Valid values are: 120-900 seconds. | [optional] 
**verified** | **bool** | Defaults to false. The following factors support verified &#x3D; true as part of the initial registration request: OneLogin SMS, OneLogin Voice, OneLogin Email. When using verified &#x3D; true it is critical that the supported factors have pre-verified values, most likely imported from an existing directory or by the users themselvdes. Factors such as Authenticator and OneLogin Protect do not support verification &#x3D; true as the user interaction is required to verify the factor. | [optional] 
**redirect_to** | **str** | Only applies to Email MagicLink factor. Redirects MagicLink success page to specified URL after 2 seconds. Email must already be configured by the user. | [optional] 
**custom_message** | **str** | Only applies to SMS factor. A message template that will be sent via SMS. Max length of the message after template items are inserted is 160 characters including the OTP code. SMS must already be configured by the user. The following template variables can be included in the message. - {{otp_code}} - The security code. - {{otp_expiry}} - The number of minutes until the one time code expires. | [optional] 

## Example

```python
from openapi_client.models.create_factor_registration_request import CreateFactorRegistrationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFactorRegistrationRequest from a JSON string
create_factor_registration_request_instance = CreateFactorRegistrationRequest.from_json(json)
# print the JSON string representation of the object
print CreateFactorRegistrationRequest.to_json()

# convert the object into a dict
create_factor_registration_request_dict = create_factor_registration_request_instance.to_dict()
# create an instance of CreateFactorRegistrationRequest from a dict
create_factor_registration_request_form_dict = create_factor_registration_request.from_dict(create_factor_registration_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


