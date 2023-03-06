# AuthServerConfiguration

Authorization server configuration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**audiences** | **List[str]** | List of API endpoints that will be returned in Access Tokens. | 
**refresh_token_expiration_minutes** | **int** | The number of minutes until refresh token expires. There is no maximum expiry limit. | [optional] 
**resource_identifier** | **str** | Unique identifier for the API that the Authorization Server will issue Access Tokens for. | 
**access_token_expiration_minutes** | **int** | The number of minutes until access token expires. There is no maximum expiry limit. | [optional] 

## Example

```python
from onelogin.models.auth_server_configuration import AuthServerConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of AuthServerConfiguration from a JSON string
auth_server_configuration_instance = AuthServerConfiguration.from_json(json)
# print the JSON string representation of the object
print AuthServerConfiguration.to_json()

# convert the object into a dict
auth_server_configuration_dict = auth_server_configuration_instance.to_dict()
# create an instance of AuthServerConfiguration from a dict
auth_server_configuration_form_dict = auth_server_configuration.from_dict(auth_server_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


