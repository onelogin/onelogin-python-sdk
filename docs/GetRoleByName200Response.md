# GetRoleByName200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**GenerateToken400Response**](GenerateToken400Response.md) |  | [optional] 
**pagination** | [**GetRoleByName200ResponsePagination**](GetRoleByName200ResponsePagination.md) |  | [optional] 
**data** | [**List[GetRoleByName200ResponseDataInner]**](GetRoleByName200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_role_by_name200_response import GetRoleByName200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoleByName200Response from a JSON string
get_role_by_name200_response_instance = GetRoleByName200Response.from_json(json)
# print the JSON string representation of the object
print GetRoleByName200Response.to_json()

# convert the object into a dict
get_role_by_name200_response_dict = get_role_by_name200_response_instance.to_dict()
# create an instance of GetRoleByName200Response from a dict
get_role_by_name200_response_form_dict = get_role_by_name200_response.from_dict(get_role_by_name200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


