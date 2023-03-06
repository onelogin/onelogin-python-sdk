# ClientAppFull


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scopes** | [**List[Scope]**](Scope.md) | List of All Scopes assigned to a client app | [optional] 
**app_id** | **int** | Unique Client App ID | [optional] 
**name** | **str** | Name of client app | [optional] 
**api_auth_id** | **int** |  | [optional] 

## Example

```python
from onelogin.models.client_app_full import ClientAppFull

# TODO update the JSON string below
json = "{}"
# create an instance of ClientAppFull from a JSON string
client_app_full_instance = ClientAppFull.from_json(json)
# print the JSON string representation of the object
print ClientAppFull.to_json()

# convert the object into a dict
client_app_full_dict = client_app_full_instance.to_dict()
# create an instance of ClientAppFull from a dict
client_app_full_form_dict = client_app_full.from_dict(client_app_full_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


