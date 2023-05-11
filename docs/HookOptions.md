# HookOptions

A set of attributes allow control over the information that is included in the hook context.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**risk_enabled** | **bool** |  | [optional] 
**location_enabled** | **bool** |  | [optional] 
**mfa_device_info_enabled** | **bool** |  | [optional] 

## Example

```python
from onelogin.models.hook_options import HookOptions

# TODO update the JSON string below
json = "{}"
# create an instance of HookOptions from a JSON string
hook_options_instance = HookOptions.from_json(json)
# print the JSON string representation of the object
print HookOptions.to_json()

# convert the object into a dict
hook_options_dict = hook_options_instance.to_dict()
# create an instance of HookOptions from a dict
hook_options_form_dict = hook_options.from_dict(hook_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


