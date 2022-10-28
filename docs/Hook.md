# Hook


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | A string describing the type of hook. e.g. &#x60;pre-authentication&#x60; | 
**env_vars** | **[str]** | Environment Variable objects that will be available via process.env.ENV_VAR_NAME in the hook code. | 
**runtime** | **str** | The Smart Hooks supported Node.js version to execute this hook with. | 
**packages** | **{str: (bool, date, datetime, dict, float, int, list, str, none_type)}** | An object containing NPM packages that are bundled with the hook function. | 
**function** | **str** | A base64 encoded string containing the javascript function code. | 
**disabled** | **bool** | Boolean to enable or disable the hook. Disabled hooks will not run. | defaults to True
**timeout** | **int** | The number of seconds to allow the hook function to run before before timing out. Maximum timeout varies based on the type of hook. | defaults to 1
**retries** | **int** | Number of retries if execution fails. | defaults to 0
**id** | **str** | The Hook unique ID in OneLogin. | [optional] 
**context_version** | **str** | The semantic version of the content that will be injected into this hook. | [optional] 
**status** | **str** | String describing the state of the hook function. When a hook is ready and disabled is false it will be executed. | [optional] 
**options** | [**HookOptions**](HookOptions.md) |  | [optional] 
**conditions** | [**[HookConditionsInner]**](HookConditionsInner.md) | An array of objects that let you limit the execution of a hook to users in specific roles. | [optional] 
**created_at** | **str** | ISO8601 format date that they hook function was created. | [optional] 
**updated_at** | **str** | ISO8601 format date that they hook function was last updated. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


