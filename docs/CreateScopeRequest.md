# CreateScopeRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | A value representing the api scope that with be authorized | [optional] 
**description** | **str** | A description of what access the scope enables | [optional] 

## Example

```python
from openapi_client.models.create_scope_request import CreateScopeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateScopeRequest from a JSON string
create_scope_request_instance = CreateScopeRequest.from_json(json)
# print the JSON string representation of the object
print CreateScopeRequest.to_json()

# convert the object into a dict
create_scope_request_dict = create_scope_request_instance.to_dict()
# create an instance of CreateScopeRequest from a dict
create_scope_request_form_dict = create_scope_request.from_dict(create_scope_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


