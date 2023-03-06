# AuthFactor


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**factor_id** | **int** | The identifier of the factor to enroll the user with. | [optional] [readonly] 
**display_name** | **str** | Authentication factor display name as it appears to users, as defined in the admininstrative interface at Settings &gt; Authentication Factors. | [optional] 
**number** | **str** | The phone number of the user in E.164 format. | [optional] 
**verified** | **bool** | Defaults to false. Some factors like SMS or Voice require that a user recieve a token and then that token is supplied to the Verify endpoint before the device is considered active. You can set verfied to &#x60;true&#x60; which indicates the the users phone number is pre verified and the device can be immediately activated.         | [optional] 
**type_display_name** | **str** | Authentication factor display name as it appears to users upon initial registration, as defined by admins at Settings &gt; Authentication Factors. | [optional] 
**active** | **bool** | &#x60;true&#x60; &#x3D; enabled (used successfully for authentication at least once). &#x60;false&#x60; &#x3D; pending (registered but never used). | [optional] 
**user_display_name** | **str** | Authentication factor display name assigned by users when they register the device. | [optional] 
**default** | **bool** | &#x60;true&#x60; &#x3D; is user’s default MFA device for OneLogin. | [optional] 
**phone_number** | **str** | For OTP codes sent via SMS, the phone number receiving the SMS message. | [optional] [readonly] 
**auth_factor_name** | **str** | \&quot;Official\&quot; authentication factor name, as it appears to administrators in OneLogin. | [optional] [readonly] 
**id** | **int** | MFA device identifier. | [optional] [readonly] 
**needs_trigger** | **bool** | &#x60;true&#x60;: You MUST Activate this Factor to trigger an SMS or Push notification before Verifying the OTP code. &#x60;false&#x60;: No Activation required. You can Verify the OTP immediately. MFA factors that provide both push notifications (user accepts notification) and pull code submission (user initiates code submission from device or enters it manually) should appear twice; once with &#x60;needs_trigger: true&#x60; and once with &#x60;needs_trigger: false&#x60;. | [optional] 

## Example

```python
from onelogin.models.auth_factor import AuthFactor

# TODO update the JSON string below
json = "{}"
# create an instance of AuthFactor from a JSON string
auth_factor_instance = AuthFactor.from_json(json)
# print the JSON string representation of the object
print AuthFactor.to_json()

# convert the object into a dict
auth_factor_dict = auth_factor_instance.to_dict()
# create an instance of AuthFactor from a dict
auth_factor_form_dict = auth_factor.from_dict(auth_factor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


