# ListBrands200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Brand’s unique ID in OneLogin. | [optional] 
**enabled** | **bool** | Indicates if the brand is enabled or not. | [optional] 
**name** | **str** | Brand name for humans. This isn’t related to subdomains. | [optional] 

## Example

```python
from openapi_client.models.list_brands200_response_inner import ListBrands200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListBrands200ResponseInner from a JSON string
list_brands200_response_inner_instance = ListBrands200ResponseInner.from_json(json)
# print the JSON string representation of the object
print ListBrands200ResponseInner.to_json()

# convert the object into a dict
list_brands200_response_inner_dict = list_brands200_response_inner_instance.to_dict()
# create an instance of ListBrands200ResponseInner from a dict
list_brands200_response_inner_form_dict = list_brands200_response_inner.from_dict(list_brands200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


