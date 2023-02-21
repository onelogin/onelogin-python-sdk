# GetScopes200ResponseInnerConfiguration

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
from onelogin.models.get_scopes200_response_inner_configuration import GetScopes200ResponseInnerConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of GetScopes200ResponseInnerConfiguration from a JSON string
get_scopes200_response_inner_configuration_instance = GetScopes200ResponseInnerConfiguration.from_json(json)
# print the JSON string representation of the object
print GetScopes200ResponseInnerConfiguration.to_json()

# convert the object into a dict
get_scopes200_response_inner_configuration_dict = get_scopes200_response_inner_configuration_instance.to_dict()
# create an instance of GetScopes200ResponseInnerConfiguration from a dict
get_scopes200_response_inner_configuration_form_dict = get_scopes200_response_inner_configuration.from_dict(get_scopes200_response_inner_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


