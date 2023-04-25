# Hook


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Hook unique ID in OneLogin. | [optional] 
**type** | **str** | A string describing the type of hook. e.g. &#x60;pre-authentication&#x60; | 
**disabled** | **bool** | Boolean to enable or disable the hook. Disabled hooks will not run. | [default to True]
**timeout** | **int** | The number of seconds to allow the hook function to run before before timing out. Maximum timeout varies based on the type of hook. | [default to 1]
**env_vars** | **List[str]** | Environment Variable objects that will be available via process.env.ENV_VAR_NAME in the hook code. | 
**runtime** | **str** | The Smart Hooks supported Node.js version to execute this hook with. | 
**retries** | **int** | Number of retries if execution fails. | [default to 0]
**packages** | **Dict[str, str]** | An object containing NPM packages that are bundled with the hook function. | 
**function** | **str** | A base64 encoded string containing the javascript function code. | 
**context_version** | **str** | The semantic version of the content that will be injected into this hook. | [optional] 
**status** | **str** | String describing the state of the hook function. When a hook is ready and disabled is false it will be executed. | [optional] 
**options** | [**HookOptions**](HookOptions.md) |  | [optional] 
**conditions** | [**List[Condition]**](Condition.md) | An array of objects that let you limit the execution of a hook to users in specific roles. | [optional] 
**created_at** | **str** | ISO8601 format date that they hook function was created. | [optional] 
**updated_at** | **str** | ISO8601 format date that they hook function was last updated. | [optional] 

## Example

```python
from onelogin.models.hook import Hook

# TODO update the JSON string below
json = "{}"
# create an instance of Hook from a JSON string
hook_instance = Hook.from_json(json)
# print the JSON string representation of the object
print Hook.to_json()

# convert the object into a dict
hook_dict = hook_instance.to_dict()
# create an instance of Hook from a dict
hook_form_dict = hook.from_dict(hook_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


