# HookEnvvar


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique identifier for the Hook Environment Variable | [optional] [readonly] 
**name** | **str** | The name of the environment variable. | 
**created_at** | **str** | The ISO8601 formatted date that the environment variable was created. | [optional] 
**updated_at** | **str** | The ISO8601 formatted date that the environment variable was last updated. | [optional] 
**value** | **str** | The secret value that will be encrypted at rest and injected in applicable hook functions at run time. | 

## Example

```python
from onelogin.models.hook_envvar import HookEnvvar

# TODO update the JSON string below
json = "{}"
# create an instance of HookEnvvar from a JSON string
hook_envvar_instance = HookEnvvar.from_json(json)
# print the JSON string representation of the object
print HookEnvvar.to_json()

# convert the object into a dict
hook_envvar_dict = hook_envvar_instance.to_dict()
# create an instance of HookEnvvar from a dict
hook_envvar_form_dict = hook_envvar.from_dict(hook_envvar_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


