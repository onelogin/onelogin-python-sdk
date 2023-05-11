# CreateFactorRegistration201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **str** | MFA device identifier. | [optional] 
**user_display_name** | **str** | Authentication factor display name assigned by users when they register the device. | [optional] 
**type_display_name** | **str** | Authentication factor display name as it appears to users upon initial registration, as defined by admins at Settings &gt; Authentication Factors. | [optional] 
**auth_factor_name** | **str** | Authentication factor name, as it appears to administrators in OneLogin. | [optional] 
**id** | **str** | Verification identifier used in subsequent verification step. | [optional] 
**user_id** | **str** | User identifier | [optional] 

## Example

```python
from onelogin.models.create_factor_registration201_response import CreateFactorRegistration201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateFactorRegistration201Response from a JSON string
create_factor_registration201_response_instance = CreateFactorRegistration201Response.from_json(json)
# print the JSON string representation of the object
print CreateFactorRegistration201Response.to_json()

# convert the object into a dict
create_factor_registration201_response_dict = create_factor_registration201_response_instance.to_dict()
# create an instance of CreateFactorRegistration201Response from a dict
create_factor_registration201_response_form_dict = create_factor_registration201_response.from_dict(create_factor_registration201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


