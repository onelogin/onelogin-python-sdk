# GetBrandApps200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**updated_at** | **str** |  | 
**name** | **str** |  | 
**connector_id** | **int** |  | 
**auth_method_description** | **str** |  | 
**description** | **str** |  | 
**auth_method** | **int** |  | 
**created_at** | **str** |  | 
**visible** | **bool** |  | 

## Example

```python
from onelogin.models.get_brand_apps200_response_inner import GetBrandApps200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetBrandApps200ResponseInner from a JSON string
get_brand_apps200_response_inner_instance = GetBrandApps200ResponseInner.from_json(json)
# print the JSON string representation of the object
print GetBrandApps200ResponseInner.to_json()

# convert the object into a dict
get_brand_apps200_response_inner_dict = get_brand_apps200_response_inner_instance.to_dict()
# create an instance of GetBrandApps200ResponseInner from a dict
get_brand_apps200_response_inner_form_dict = get_brand_apps200_response_inner.from_dict(get_brand_apps200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


