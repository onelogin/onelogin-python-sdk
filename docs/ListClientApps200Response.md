# ListClientApps200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scopes** | [**List[ListClientApps200ResponseScopesInner]**](ListClientApps200ResponseScopesInner.md) | List of All Scopes assigned to a client app | [optional] 
**app_id** | **int** | Unique Client App ID | [optional] 
**name** | **str** | Name of client app | [optional] 
**api_auth_id** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.list_client_apps200_response import ListClientApps200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListClientApps200Response from a JSON string
list_client_apps200_response_instance = ListClientApps200Response.from_json(json)
# print the JSON string representation of the object
print ListClientApps200Response.to_json()

# convert the object into a dict
list_client_apps200_response_dict = list_client_apps200_response_instance.to_dict()
# create an instance of ListClientApps200Response from a dict
list_client_apps200_response_form_dict = list_client_apps200_response.from_dict(list_client_apps200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


