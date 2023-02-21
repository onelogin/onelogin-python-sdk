# CreateAppRequestOneOf1Parameters


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**saml_username** | [**CreateAppRequestOneOf1ParametersSamlUsername**](CreateAppRequestOneOf1ParametersSamlUsername.md) |  | 

## Example

```python
from onelogin.models.create_app_request_one_of1_parameters import CreateAppRequestOneOf1Parameters

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAppRequestOneOf1Parameters from a JSON string
create_app_request_one_of1_parameters_instance = CreateAppRequestOneOf1Parameters.from_json(json)
# print the JSON string representation of the object
print CreateAppRequestOneOf1Parameters.to_json()

# convert the object into a dict
create_app_request_one_of1_parameters_dict = create_app_request_one_of1_parameters_instance.to_dict()
# create an instance of CreateAppRequestOneOf1Parameters from a dict
create_app_request_one_of1_parameters_form_dict = create_app_request_one_of1_parameters.from_dict(create_app_request_one_of1_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


