# AuthServer

base resource for configuring api authorization in OneLogin

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Auth server unique ID in Onelogin | [optional] [readonly] 
**name** | **str** | Name of the API. | 
**description** | **str** | Description of what the API does. | 
**configuration** | [**AuthServerConfiguration**](AuthServerConfiguration.md) |  | 

## Example

```python
from onelogin.models.auth_server import AuthServer

# TODO update the JSON string below
json = "{}"
# create an instance of AuthServer from a JSON string
auth_server_instance = AuthServer.from_json(json)
# print the JSON string representation of the object
print AuthServer.to_json()

# convert the object into a dict
auth_server_dict = auth_server_instance.to_dict()
# create an instance of AuthServer from a dict
auth_server_form_dict = auth_server.from_dict(auth_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


