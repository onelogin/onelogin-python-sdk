# ListMappingConditions200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of Condition | [optional] 
**value** | **str** | The unique identifier of the condition. This should be used when defining conditions for a User Mapping | [optional] 

## Example

```python
from onelogin.models.list_mapping_conditions200_response import ListMappingConditions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListMappingConditions200Response from a JSON string
list_mapping_conditions200_response_instance = ListMappingConditions200Response.from_json(json)
# print the JSON string representation of the object
print ListMappingConditions200Response.to_json()

# convert the object into a dict
list_mapping_conditions200_response_dict = list_mapping_conditions200_response_instance.to_dict()
# create an instance of ListMappingConditions200Response from a dict
list_mapping_conditions200_response_form_dict = list_mapping_conditions200_response.from_dict(list_mapping_conditions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


