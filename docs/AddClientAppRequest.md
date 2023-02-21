# AddClientAppRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **int** | The ID of the OpenId Connect app to allow access through. | [optional] 
**scopes** | **List[int]** | An array of Scope IDs that represent scopes the app can request | [optional] 

## Example

```python
from onelogin.models.add_client_app_request import AddClientAppRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddClientAppRequest from a JSON string
add_client_app_request_instance = AddClientAppRequest.from_json(json)
# print the JSON string representation of the object
print AddClientAppRequest.to_json()

# convert the object into a dict
add_client_app_request_dict = add_client_app_request_instance.to_dict()
# create an instance of AddClientAppRequest from a dict
add_client_app_request_form_dict = add_client_app_request.from_dict(add_client_app_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


