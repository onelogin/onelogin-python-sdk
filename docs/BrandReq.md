# BrandReq


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Brand’s unique ID in OneLogin. | [optional] 
**enabled** | **bool** | Indicates if the brand is enabled or not. | [optional] 
**name** | **str** | Brand name for humans. This isn’t related to subdomains. | [optional] 

## Example

```python
from onelogin.models.brand_req import BrandReq

# TODO update the JSON string below
json = "{}"
# create an instance of BrandReq from a JSON string
brand_req_instance = BrandReq.from_json(json)
# print the JSON string representation of the object
print BrandReq.to_json()

# convert the object into a dict
brand_req_dict = brand_req_instance.to_dict()
# create an instance of BrandReq from a dict
brand_req_form_dict = brand_req.from_dict(brand_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


