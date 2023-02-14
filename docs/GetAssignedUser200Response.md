# GetAssignedUser200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | [optional] 
**users** | **List[int]** |  | [optional] 
**before_cursor** | **int** |  | [optional] 
**previous_link** | **str** |  | [optional] 
**after_cursor** | **int** |  | [optional] 
**next_link** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.get_assigned_user200_response import GetAssignedUser200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAssignedUser200Response from a JSON string
get_assigned_user200_response_instance = GetAssignedUser200Response.from_json(json)
# print the JSON string representation of the object
print GetAssignedUser200Response.to_json()

# convert the object into a dict
get_assigned_user200_response_dict = get_assigned_user200_response_instance.to_dict()
# create an instance of GetAssignedUser200Response from a dict
get_assigned_user200_response_form_dict = get_assigned_user200_response.from_dict(get_assigned_user200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


