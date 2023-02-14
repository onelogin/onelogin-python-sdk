# GetEventById200ResponseStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **bool** |  | [optional] 
**code** | **int** |  | 
**type** | **str** |  | [optional] 
**message** | **str** |  | 

## Example

```python
from openapi_client.models.get_event_by_id200_response_status import GetEventById200ResponseStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GetEventById200ResponseStatus from a JSON string
get_event_by_id200_response_status_instance = GetEventById200ResponseStatus.from_json(json)
# print the JSON string representation of the object
print GetEventById200ResponseStatus.to_json()

# convert the object into a dict
get_event_by_id200_response_status_dict = get_event_by_id200_response_status_instance.to_dict()
# create an instance of GetEventById200ResponseStatus from a dict
get_event_by_id200_response_status_form_dict = get_event_by_id200_response_status.from_dict(get_event_by_id200_response_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


