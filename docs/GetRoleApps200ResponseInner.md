# GetRoleApps200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | app id | [optional] 
**name** | **str** | app name | [optional] 
**icon_url** | **str** | url of Icon | [optional] 

## Example

```python
from openapi_client.models.get_role_apps200_response_inner import GetRoleApps200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetRoleApps200ResponseInner from a JSON string
get_role_apps200_response_inner_instance = GetRoleApps200ResponseInner.from_json(json)
# print the JSON string representation of the object
print GetRoleApps200ResponseInner.to_json()

# convert the object into a dict
get_role_apps200_response_inner_dict = get_role_apps200_response_inner_instance.to_dict()
# create an instance of GetRoleApps200ResponseInner from a dict
get_role_apps200_response_inner_form_dict = get_role_apps200_response_inner.from_dict(get_role_apps200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


