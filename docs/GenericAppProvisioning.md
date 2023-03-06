# GenericAppProvisioning

Indicates if provisioning is enabled for this app.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 

## Example

```python
from onelogin.models.generic_app_provisioning import GenericAppProvisioning

# TODO update the JSON string below
json = "{}"
# create an instance of GenericAppProvisioning from a JSON string
generic_app_provisioning_instance = GenericAppProvisioning.from_json(json)
# print the JSON string representation of the object
print GenericAppProvisioning.to_json()

# convert the object into a dict
generic_app_provisioning_dict = generic_app_provisioning_instance.to_dict()
# create an instance of GenericAppProvisioning from a dict
generic_app_provisioning_form_dict = generic_app_provisioning.from_dict(generic_app_provisioning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


