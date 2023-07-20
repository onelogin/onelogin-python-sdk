# onelogin.model.hook.Hook

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**retries** | decimal.Decimal, int,  | decimal.Decimal,  | Number of retries if execution fails. | if omitted the server will use the default value of 0
**function** | str,  | str,  | A base64 encoded string containing the javascript function code. | 
**runtime** | str,  | str,  | The Smart Hooks supported Node.js version to execute this hook with. | 
**disabled** | bool,  | BoolClass,  | Boolean to enable or disable the hook. Disabled hooks will not run. | if omitted the server will use the default value of True
**[packages](#packages)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | An object containing NPM packages that are bundled with the hook function. | 
**type** | str,  | str,  | A string describing the type of hook. e.g. &#x60;pre-authentication&#x60; | 
**timeout** | decimal.Decimal, int,  | decimal.Decimal,  | The number of seconds to allow the hook function to run before before timing out. Maximum timeout varies based on the type of hook. | if omitted the server will use the default value of 1
**[env_vars](#env_vars)** | list, tuple,  | tuple,  | Environment Variable objects that will be available via process.env.ENV_VAR_NAME in the hook code. | 
**id** | str,  | str,  | The Hook unique ID in OneLogin. | [optional] 
**context_version** | str,  | str,  | The semantic version of the content that will be injected into this hook. | [optional] 
**status** | str,  | str,  | String describing the state of the hook function. When a hook is ready and disabled is false it will be executed. | [optional] must be one of ["ready", "create-queued", "create-running", "create-failed", "update-queued", "update-running", "update-failed", ] 
**[options](#options)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | A set of attributes allow control over the information that is included in the hook context. | [optional] 
**[conditions](#conditions)** | list, tuple,  | tuple,  | An array of objects that let you limit the execution of a hook to users in specific roles. | [optional] 
**created_at** | str,  | str,  | ISO8601 format date that they hook function was created. | [optional] 
**updated_at** | str,  | str,  | ISO8601 format date that they hook function was last updated. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# env_vars

Environment Variable objects that will be available via process.env.ENV_VAR_NAME in the hook code.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Environment Variable objects that will be available via process.env.ENV_VAR_NAME in the hook code. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# packages

An object containing NPM packages that are bundled with the hook function.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | An object containing NPM packages that are bundled with the hook function. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**any_string_name** | str,  | str,  | any string name can be used but the value must be the correct type | [optional] 

# options

A set of attributes allow control over the information that is included in the hook context.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A set of attributes allow control over the information that is included in the hook context. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**risk_enabled** | bool,  | BoolClass,  |  | [optional] 
**location_enabled** | bool,  | BoolClass,  |  | [optional] 
**mfa_device_info_enabled** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# conditions

An array of objects that let you limit the execution of a hook to users in specific roles.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | An array of objects that let you limit the execution of a hook to users in specific roles. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Condition**](Condition.md) | [**Condition**](Condition.md) | [**Condition**](Condition.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

