# BrandLogoUrls


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original** | **str** |  | 
**login** | **str** |  | 
**navigation** | **str** |  | 

## Example

```python
from onelogin.models.brand_logo_urls import BrandLogoUrls

# TODO update the JSON string below
json = "{}"
# create an instance of BrandLogoUrls from a JSON string
brand_logo_urls_instance = BrandLogoUrls.from_json(json)
# print the JSON string representation of the object
print BrandLogoUrls.to_json()

# convert the object into a dict
brand_logo_urls_dict = brand_logo_urls_instance.to_dict()
# create an instance of BrandLogoUrls from a dict
brand_logo_urls_form_dict = brand_logo_urls.from_dict(brand_logo_urls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


