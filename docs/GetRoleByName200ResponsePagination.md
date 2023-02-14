# GetRoleByName200ResponsePagination


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**after_cursor** | **str** |  | [optional] 
**before_cursor** | **str** |  | [optional] 
**next_link** | **str** |  | [optional] 
**previous_link** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.get_role_by_name200_response_pagination import GetRoleByName200ResponsePagination

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoleByName200ResponsePagination from a JSON string
get_role_by_name200_response_pagination_instance = GetRoleByName200ResponsePagination.from_json(json)
# print the JSON string representation of the object
print GetRoleByName200ResponsePagination.to_json()

# convert the object into a dict
get_role_by_name200_response_pagination_dict = get_role_by_name200_response_pagination_instance.to_dict()
# create an instance of GetRoleByName200ResponsePagination from a dict
get_role_by_name200_response_pagination_form_dict = get_role_by_name200_response_pagination.from_dict(get_role_by_name200_response_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


