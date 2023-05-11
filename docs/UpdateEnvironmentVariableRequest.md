# UpdateEnvironmentVariableRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The secret value that will be encrypted at rest and injected in applicable hook functions at run time. | 

## Example

```python
from onelogin.models.update_environment_variable_request import UpdateEnvironmentVariableRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateEnvironmentVariableRequest from a JSON string
update_environment_variable_request_instance = UpdateEnvironmentVariableRequest.from_json(json)
# print the JSON string representation of the object
print UpdateEnvironmentVariableRequest.to_json()

# convert the object into a dict
update_environment_variable_request_dict = update_environment_variable_request_instance.to_dict()
# create an instance of UpdateEnvironmentVariableRequest from a dict
update_environment_variable_request_form_dict = update_environment_variable_request.from_dict(update_environment_variable_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


