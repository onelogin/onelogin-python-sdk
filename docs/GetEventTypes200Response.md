# GetEventTypes200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**GenerateToken400Response**](GenerateToken400Response.md) |  | [optional] 
**data** | [**List[GetEventTypes200ResponseDataInner]**](GetEventTypes200ResponseDataInner.md) |  | [optional] 

## Example

```python
from onelogin.models.get_event_types200_response import GetEventTypes200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEventTypes200Response from a JSON string
get_event_types200_response_instance = GetEventTypes200Response.from_json(json)
# print the JSON string representation of the object
print GetEventTypes200Response.to_json()

# convert the object into a dict
get_event_types200_response_dict = get_event_types200_response_instance.to_dict()
# create an instance of GetEventTypes200Response from a dict
get_event_types200_response_form_dict = get_event_types200_response.from_dict(get_event_types200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


