# ListClientApps200ResponseScopesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique Scope ID value | [optional] 
**value** | **str** | Scope Value | [optional] 
**description** | **str** | Description of the scope | [optional] 

## Example

```python
from onelogin.models.list_client_apps200_response_scopes_inner import ListClientApps200ResponseScopesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListClientApps200ResponseScopesInner from a JSON string
list_client_apps200_response_scopes_inner_instance = ListClientApps200ResponseScopesInner.from_json(json)
# print the JSON string representation of the object
print ListClientApps200ResponseScopesInner.to_json()

# convert the object into a dict
list_client_apps200_response_scopes_inner_dict = list_client_apps200_response_scopes_inner_instance.to_dict()
# create an instance of ListClientApps200ResponseScopesInner from a dict
list_client_apps200_response_scopes_inner_form_dict = list_client_apps200_response_scopes_inner.from_dict(list_client_apps200_response_scopes_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


