# GetScopes200ResponseInner

base resource for configuring api authorization in OneLogin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Auth server unique ID in Onelogin | [optional] 
**name** | **str** | Name of the API. | 
**description** | **str** | Description of what the API does. | 
**configuration** | [**GetScopes200ResponseInnerConfiguration**](GetScopes200ResponseInnerConfiguration.md) |  | 

## Example

```python
from openapi_client.models.get_scopes200_response_inner import GetScopes200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetScopes200ResponseInner from a JSON string
get_scopes200_response_inner_instance = GetScopes200ResponseInner.from_json(json)
# print the JSON string representation of the object
print GetScopes200ResponseInner.to_json()

# convert the object into a dict
get_scopes200_response_inner_dict = get_scopes200_response_inner_instance.to_dict()
# create an instance of GetScopes200ResponseInner from a dict
get_scopes200_response_inner_form_dict = get_scopes200_response_inner.from_dict(get_scopes200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


