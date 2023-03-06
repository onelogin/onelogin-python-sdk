# EnforcementPointResourcesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | [optional] 
**is_path_regex** | **bool** |  | [optional] 
**require_auth** | **bool** |  | [optional] 
**permission** | **str** |  | [optional] 
**conditions** | **str** | required if permission &#x3D;&#x3D; \&quot;conditions\&quot; | [optional] 

## Example

```python
from onelogin.models.enforcement_point_resources_inner import EnforcementPointResourcesInner

# TODO update the JSON string below
json = "{}"
# create an instance of EnforcementPointResourcesInner from a JSON string
enforcement_point_resources_inner_instance = EnforcementPointResourcesInner.from_json(json)
# print the JSON string representation of the object
print EnforcementPointResourcesInner.to_json()

# convert the object into a dict
enforcement_point_resources_inner_dict = enforcement_point_resources_inner_instance.to_dict()
# create an instance of EnforcementPointResourcesInner from a dict
enforcement_point_resources_inner_form_dict = enforcement_point_resources_inner.from_dict(enforcement_point_resources_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


