# GetUserRoles200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**Error**](Error.md) |  | [optional] 
**data** | **List[int]** | List of Role IDs that are assigned to the User | [optional] 

## Example

```python
from onelogin.models.get_user_roles200_response import GetUserRoles200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserRoles200Response from a JSON string
get_user_roles200_response_instance = GetUserRoles200Response.from_json(json)
# print the JSON string representation of the object
print GetUserRoles200Response.to_json()

# convert the object into a dict
get_user_roles200_response_dict = get_user_roles200_response_instance.to_dict()
# create an instance of GetUserRoles200Response from a dict
get_user_roles200_response_form_dict = get_user_roles200_response.from_dict(get_user_roles200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


