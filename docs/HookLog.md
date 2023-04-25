# HookLog


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** |  | [optional] 
**correlation_id** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**events** | **List[str]** |  | [optional] 

## Example

```python
from onelogin.models.hook_log import HookLog

# TODO update the JSON string below
json = "{}"
# create an instance of HookLog from a JSON string
hook_log_instance = HookLog.from_json(json)
# print the JSON string representation of the object
print HookLog.to_json()

# convert the object into a dict
hook_log_dict = hook_log_instance.to_dict()
# create an instance of HookLog from a dict
hook_log_form_dict = hook_log.from_dict(hook_log_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


