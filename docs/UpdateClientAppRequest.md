# UpdateClientAppRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scopes** | **List[int]** | An array of Scope IDs the scopes the app can request | [optional] 

## Example

```python
from openapi_client.models.update_client_app_request import UpdateClientAppRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateClientAppRequest from a JSON string
update_client_app_request_instance = UpdateClientAppRequest.from_json(json)
# print the JSON string representation of the object
print UpdateClientAppRequest.to_json()

# convert the object into a dict
update_client_app_request_dict = update_client_app_request_instance.to_dict()
# create an instance of UpdateClientAppRequest from a dict
update_client_app_request_form_dict = update_client_app_request.from_dict(update_client_app_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


