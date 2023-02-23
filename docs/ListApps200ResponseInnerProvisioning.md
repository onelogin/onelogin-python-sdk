# ListApps200ResponseInnerProvisioning


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Indicates if provisioning is enabled for this app. | [optional] 

## Example

```python
from onelogin.models.list_apps200_response_inner_provisioning import ListApps200ResponseInnerProvisioning

# TODO update the JSON string below
json = "{}"
# create an instance of ListApps200ResponseInnerProvisioning from a JSON string
list_apps200_response_inner_provisioning_instance = ListApps200ResponseInnerProvisioning.from_json(json)
# print the JSON string representation of the object
print ListApps200ResponseInnerProvisioning.to_json()

# convert the object into a dict
list_apps200_response_inner_provisioning_dict = list_apps200_response_inner_provisioning_instance.to_dict()
# create an instance of ListApps200ResponseInnerProvisioning from a dict
list_apps200_response_inner_provisioning_form_dict = list_apps200_response_inner_provisioning.from_dict(list_apps200_response_inner_provisioning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


