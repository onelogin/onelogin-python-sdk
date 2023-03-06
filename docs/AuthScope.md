# AuthScope


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | A value representing the api scope that with be authorized | [optional] 
**description** | **str** | A description of what access the scope enables | [optional] 

## Example

```python
from onelogin.models.auth_scope import AuthScope

# TODO update the JSON string below
json = "{}"
# create an instance of AuthScope from a JSON string
auth_scope_instance = AuthScope.from_json(json)
# print the JSON string representation of the object
print AuthScope.to_json()

# convert the object into a dict
auth_scope_dict = auth_scope_instance.to_dict()
# create an instance of AuthScope from a dict
auth_scope_form_dict = auth_scope.from_dict(auth_scope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


