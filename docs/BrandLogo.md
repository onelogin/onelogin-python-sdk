# BrandLogo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**urls** | [**BrandLogoUrls**](BrandLogoUrls.md) |  | 
**file_size** | **int** |  | 
**updated_at** | **str** |  | 
**content_type** | **str** |  | 

## Example

```python
from onelogin.models.brand_logo import BrandLogo

# TODO update the JSON string below
json = "{}"
# create an instance of BrandLogo from a JSON string
brand_logo_instance = BrandLogo.from_json(json)
# print the JSON string representation of the object
print BrandLogo.to_json()

# convert the object into a dict
brand_logo_dict = brand_logo_instance.to_dict()
# create an instance of BrandLogo from a dict
brand_logo_form_dict = brand_logo.from_dict(brand_logo_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


