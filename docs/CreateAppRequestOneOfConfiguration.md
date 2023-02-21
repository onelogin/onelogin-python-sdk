# CreateAppRequestOneOfConfiguration


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_url** | **str** |  | 
**redirect_uri** | **str** |  | 
**access_token_expiration_minutes** | **int** |  | 
**refresh_token_expiration_minutes** | **int** |  | 
**token_endpoint_auth_method** | **int** |  | 
**oidc_application_type** | **int** |  | 

## Example

```python
from onelogin.models.create_app_request_one_of_configuration import CreateAppRequestOneOfConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAppRequestOneOfConfiguration from a JSON string
create_app_request_one_of_configuration_instance = CreateAppRequestOneOfConfiguration.from_json(json)
# print the JSON string representation of the object
print CreateAppRequestOneOfConfiguration.to_json()

# convert the object into a dict
create_app_request_one_of_configuration_dict = create_app_request_one_of_configuration_instance.to_dict()
# create an instance of CreateAppRequestOneOfConfiguration from a dict
create_app_request_one_of_configuration_form_dict = create_app_request_one_of_configuration.from_dict(create_app_request_one_of_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


