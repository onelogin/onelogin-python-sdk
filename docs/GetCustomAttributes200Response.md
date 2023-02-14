# GetCustomAttributes200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**GenerateToken400Response**](GenerateToken400Response.md) |  | [optional] 
**data** | **List[List[str]]** | Provides a list of custom attribute fields (also known as custom user fields) that are available for your account. The values returned correspond to the values you provided in the Shortname field when you defined the custom user field. For details about defining custom user fields, see Custom User Fields. | [optional] 

## Example

```python
from openapi_client.models.get_custom_attributes200_response import GetCustomAttributes200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCustomAttributes200Response from a JSON string
get_custom_attributes200_response_instance = GetCustomAttributes200Response.from_json(json)
# print the JSON string representation of the object
print GetCustomAttributes200Response.to_json()

# convert the object into a dict
get_custom_attributes200_response_dict = get_custom_attributes200_response_instance.to_dict()
# create an instance of GetCustomAttributes200Response from a dict
get_custom_attributes200_response_form_dict = get_custom_attributes200_response.from_dict(get_custom_attributes200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


