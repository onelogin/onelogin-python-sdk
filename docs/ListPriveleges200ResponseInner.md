# ListPriveleges200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**privilege** | [**ListPriveleges200ResponseInnerPrivilege**](ListPriveleges200ResponseInnerPrivilege.md) |  | 

## Example

```python
from openapi_client.models.list_priveleges200_response_inner import ListPriveleges200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListPriveleges200ResponseInner from a JSON string
list_priveleges200_response_inner_instance = ListPriveleges200ResponseInner.from_json(json)
# print the JSON string representation of the object
print ListPriveleges200ResponseInner.to_json()

# convert the object into a dict
list_priveleges200_response_inner_dict = list_priveleges200_response_inner_instance.to_dict()
# create an instance of ListPriveleges200ResponseInner from a dict
list_priveleges200_response_inner_form_dict = list_priveleges200_response_inner.from_dict(list_priveleges200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


