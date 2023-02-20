# ActivateMfaFactorsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**state_token_expires_in** | **int** | Optional. Sets the window of time in seconds that the factor must be verified within. Defaults to 120 seconds (2 minutes). Max 900 seconds (15 minutes). | [optional] 
**numeric_sms_otp** | **bool** | Optional. Defaults to false. Only applies to SMS factor. When set to &#x60;true&#x60; a 6 digit numeric code will be sent to the user instead of the standard code which is alphanumeric. | [optional] 
**sms_message** | **str** | Optional. Only applies to SMS factor. A message template that will be sent via SMS. Max length of the message after template items are inserted is 160 characters. The following template variables can be included in the message. - {{otp_code}} - The security code. - {{expiration}} - The number of minutes until the one time code expires. | [optional] 

## Example

```python
from openapi_client.models.activate_mfa_factors_request import ActivateMfaFactorsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ActivateMfaFactorsRequest from a JSON string
activate_mfa_factors_request_instance = ActivateMfaFactorsRequest.from_json(json)
# print the JSON string representation of the object
print ActivateMfaFactorsRequest.to_json()

# convert the object into a dict
activate_mfa_factors_request_dict = activate_mfa_factors_request_instance.to_dict()
# create an instance of ActivateMfaFactorsRequest from a dict
activate_mfa_factors_request_form_dict = activate_mfa_factors_request.from_dict(activate_mfa_factors_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


