# CreateDeviceVerification201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** | Specifies the factor to be verified. | [optional] 
**display_name** | **str** | A name for the users device | [optional] 
**expires_at** | **str** | A short lived token that is required to Verify the Factor. This token expires based on the expires_in parameter passed in. | [optional] 
**redirect_to** | **str** | Only applies to Email MagicLink factor. Redirects MagicLink success page to specified URL after 2 seconds. Email must already be configured by the user. | [optional] 
**user_display_name** | **str** | Authentication factor display name assigned by users when they register the device. | [optional] 
**id** | **str** | Registration identifier. | [optional] 
**type_display_name** | **str** | Authentication factor display name as it appears to users upon initial registration, as defined by admins at Settings &gt; Authentication Factors. | [optional] 
**auth_factor_name** | **str** | Authentication factor name, as it appears to administrators in OneLogin. | [optional] 

## Example

```python
from onelogin.models.create_device_verification201_response import CreateDeviceVerification201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDeviceVerification201Response from a JSON string
create_device_verification201_response_instance = CreateDeviceVerification201Response.from_json(json)
# print the JSON string representation of the object
print CreateDeviceVerification201Response.to_json()

# convert the object into a dict
create_device_verification201_response_dict = create_device_verification201_response_instance.to_dict()
# create an instance of CreateDeviceVerification201Response from a dict
create_device_verification201_response_form_dict = create_device_verification201_response.from_dict(create_device_verification201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


