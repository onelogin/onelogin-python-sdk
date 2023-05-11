# BrandApp


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
from onelogin.models.brand_app import BrandApp

# TODO update the JSON string below
json = "{}"
# create an instance of BrandApp from a JSON string
brand_app_instance = BrandApp.from_json(json)
# print the JSON string representation of the object
print BrandApp.to_json()

# convert the object into a dict
brand_app_dict = brand_app_instance.to_dict()
# create an instance of BrandApp from a dict
brand_app_form_dict = brand_app.from_dict(brand_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


