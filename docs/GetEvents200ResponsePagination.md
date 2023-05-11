# GetEvents200ResponsePagination


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**before_cursor** | **str** |  | [optional] 
**after_cursor** | **str** |  | [optional] 
**previous_link** | **str** |  | [optional] 
**next_link** | **str** |  | [optional] 

## Example

```python
from onelogin.models.get_events200_response_pagination import GetEvents200ResponsePagination

# TODO update the JSON string below
json = "{}"
# create an instance of GetEvents200ResponsePagination from a JSON string
get_events200_response_pagination_instance = GetEvents200ResponsePagination.from_json(json)
# print the JSON string representation of the object
print GetEvents200ResponsePagination.to_json()

# convert the object into a dict
get_events200_response_pagination_dict = get_events200_response_pagination_instance.to_dict()
# create an instance of GetEvents200ResponsePagination from a dict
get_events200_response_pagination_form_dict = get_events200_response_pagination.from_dict(get_events200_response_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


