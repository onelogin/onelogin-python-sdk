# BrandBackground


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**urls** | [**BrandBackgroundUrls**](BrandBackgroundUrls.md) |  | 
**file_size** | **int** |  | 
**updated_at** | **str** |  | 
**content_type** | **str** |  | 

## Example

```python
from onelogin.models.brand_background import BrandBackground

# TODO update the JSON string below
json = "{}"
# create an instance of BrandBackground from a JSON string
brand_background_instance = BrandBackground.from_json(json)
# print the JSON string representation of the object
print BrandBackground.to_json()

# convert the object into a dict
brand_background_dict = brand_background_instance.to_dict()
# create an instance of BrandBackground from a dict
brand_background_form_dict = brand_background.from_dict(brand_background_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


