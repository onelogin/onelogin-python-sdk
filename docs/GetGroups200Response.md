# GetGroups200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**GenerateToken400Response**](GenerateToken400Response.md) |  | [optional] 
**data** | [**List[GetGroups200ResponseDataInner]**](GetGroups200ResponseDataInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_groups200_response import GetGroups200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroups200Response from a JSON string
get_groups200_response_instance = GetGroups200Response.from_json(json)
# print the JSON string representation of the object
print GetGroups200Response.to_json()

# convert the object into a dict
get_groups200_response_dict = get_groups200_response_instance.to_dict()
# create an instance of GetGroups200Response from a dict
get_groups200_response_form_dict = get_groups200_response.from_dict(get_groups200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


