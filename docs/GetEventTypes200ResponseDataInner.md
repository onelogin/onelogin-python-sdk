# GetEventTypes200ResponseDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from onelogin.models.get_event_types200_response_data_inner import GetEventTypes200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetEventTypes200ResponseDataInner from a JSON string
get_event_types200_response_data_inner_instance = GetEventTypes200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print GetEventTypes200ResponseDataInner.to_json()

# convert the object into a dict
get_event_types200_response_data_inner_dict = get_event_types200_response_data_inner_instance.to_dict()
# create an instance of GetEventTypes200ResponseDataInner from a dict
get_event_types200_response_data_inner_form_dict = get_event_types200_response_data_inner.from_dict(get_event_types200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


