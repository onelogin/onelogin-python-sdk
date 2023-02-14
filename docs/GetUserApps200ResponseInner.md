# GetUserApps200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The App ID | [optional] 
**icon_url** | **str** | A url for the icon that represents the app in the OneLogin portal | [optional] 
**extension** | **bool** | Boolean that indicates if the OneLogin browser extension is required to launch this app. | [optional] 
**login_id** | **int** | Unqiue identifier for this user and app combination. | [optional] 
**name** | **str** | The name of the app. | [optional] 
**provisioning_status** | **str** |  | [optional] 
**provisioning_state** | **str** | If provisioning is enabled this indicates the state of provisioning for the given user. | [optional] 
**provisioning_enabled** | **bool** | Indicates if provisioning is enabled for this app. | [optional] 

## Example

```python
from openapi_client.models.get_user_apps200_response_inner import GetUserApps200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserApps200ResponseInner from a JSON string
get_user_apps200_response_inner_instance = GetUserApps200ResponseInner.from_json(json)
# print the JSON string representation of the object
print GetUserApps200ResponseInner.to_json()

# convert the object into a dict
get_user_apps200_response_inner_dict = get_user_apps200_response_inner_instance.to_dict()
# create an instance of GetUserApps200ResponseInner from a dict
get_user_apps200_response_inner_form_dict = get_user_apps200_response_inner.from_dict(get_user_apps200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


