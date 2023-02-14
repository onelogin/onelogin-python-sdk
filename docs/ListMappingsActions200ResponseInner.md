# ListMappingsActions200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the action | [optional] 
**value** | **str** | The unique identifier of the action. This should be used when defining actions for a User Mapping. | [optional] 

## Example

```python
from openapi_client.models.list_mappings_actions200_response_inner import ListMappingsActions200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListMappingsActions200ResponseInner from a JSON string
list_mappings_actions200_response_inner_instance = ListMappingsActions200ResponseInner.from_json(json)
# print the JSON string representation of the object
print ListMappingsActions200ResponseInner.to_json()

# convert the object into a dict
list_mappings_actions200_response_inner_dict = list_mappings_actions200_response_inner_instance.to_dict()
# create an instance of ListMappingsActions200ResponseInner from a dict
list_mappings_actions200_response_inner_form_dict = list_mappings_actions200_response_inner.from_dict(list_mappings_actions200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


