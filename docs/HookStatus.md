# HookStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | responses status nam | [optional] 
**message** | **str** | your operation was successful | [optional] 

## Example

```python
from onelogin.models.hook_status import HookStatus

# TODO update the JSON string below
json = "{}"
# create an instance of HookStatus from a JSON string
hook_status_instance = HookStatus.from_json(json)
# print the JSON string representation of the object
print HookStatus.to_json()

# convert the object into a dict
hook_status_dict = hook_status_instance.to_dict()
# create an instance of HookStatus from a dict
hook_status_form_dict = hook_status.from_dict(hook_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


