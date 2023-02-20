# GetAuthenticationDevices200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** | MFA device identifier. | [optional] 
**user_display_name** | **str** | Authentication factor display name assigned by users when they register the device. | [optional] 
**type_display_name** | **str** | Authentication factor display name as it appears to users upon initial registration, as defined by admins at Settings &gt; Authentication Factors. | [optional] 
**auth_factor_name** | **str** | Authentication factor name, as it appears to administrators in OneLogin. | [optional] 
**default** | **bool** | true &#x3D; is user’s default MFA device for OneLogin. | [optional] [default to False]

## Example

```python
from openapi_client.models.get_authentication_devices200_response_inner import GetAuthenticationDevices200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAuthenticationDevices200ResponseInner from a JSON string
get_authentication_devices200_response_inner_instance = GetAuthenticationDevices200ResponseInner.from_json(json)
# print the JSON string representation of the object
print GetAuthenticationDevices200ResponseInner.to_json()

# convert the object into a dict
get_authentication_devices200_response_inner_dict = get_authentication_devices200_response_inner_instance.to_dict()
# create an instance of GetAuthenticationDevices200ResponseInner from a dict
get_authentication_devices200_response_inner_form_dict = get_authentication_devices200_response_inner.from_dict(get_authentication_devices200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


