# GetEventById200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**GetEventById200ResponseStatus**](GetEventById200ResponseStatus.md) |  | [optional] 
**data** | [**GetEvents200ResponseDataInner**](GetEvents200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_event_by_id200_response import GetEventById200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEventById200Response from a JSON string
get_event_by_id200_response_instance = GetEventById200Response.from_json(json)
# print the JSON string representation of the object
print GetEventById200Response.to_json()

# convert the object into a dict
get_event_by_id200_response_dict = get_event_by_id200_response_instance.to_dict()
# create an instance of GetEventById200Response from a dict
get_event_by_id200_response_form_dict = get_event_by_id200_response.from_dict(get_event_by_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


