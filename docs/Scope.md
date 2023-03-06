# Scope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique Scope ID value | [optional] 
**value** | **str** | Scope Value | [optional] 
**description** | **str** | Description of the scope | [optional] 

## Example

```python
from onelogin.models.scope import Scope

# TODO update the JSON string below
json = "{}"
# create an instance of Scope from a JSON string
scope_instance = Scope.from_json(json)
# print the JSON string representation of the object
print Scope.to_json()

# convert the object into a dict
scope_dict = scope_instance.to_dict()
# create an instance of Scope from a dict
scope_form_dict = scope.from_dict(scope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


