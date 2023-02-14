# GenerateToken400Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **bool** |  | [optional] 
**code** | **int** |  | 
**type** | **str** |  | [optional] 
**message** | **str** |  | 

## Example

```python
from openapi_client.models.generate_token400_response import GenerateToken400Response

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateToken400Response from a JSON string
generate_token400_response_instance = GenerateToken400Response.from_json(json)
# print the JSON string representation of the object
print GenerateToken400Response.to_json()

# convert the object into a dict
generate_token400_response_dict = generate_token400_response_instance.to_dict()
# create an instance of GenerateToken400Response from a dict
generate_token400_response_form_dict = generate_token400_response.from_dict(generate_token400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


