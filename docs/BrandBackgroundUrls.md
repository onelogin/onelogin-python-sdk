# BrandBackgroundUrls


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original** | **str** |  | 
**login** | **str** |  | 
**branding** | **str** |  | 

## Example

```python
from onelogin.models.brand_background_urls import BrandBackgroundUrls

# TODO update the JSON string below
json = "{}"
# create an instance of BrandBackgroundUrls from a JSON string
brand_background_urls_instance = BrandBackgroundUrls.from_json(json)
# print the JSON string representation of the object
print BrandBackgroundUrls.to_json()

# convert the object into a dict
brand_background_urls_dict = brand_background_urls_instance.to_dict()
# create an instance of BrandBackgroundUrls from a dict
brand_background_urls_form_dict = brand_background_urls.from_dict(brand_background_urls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


