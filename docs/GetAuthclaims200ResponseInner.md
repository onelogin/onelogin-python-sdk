# GetAuthclaims200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique ID of the claim. | [optional] 
**label** | **str** | The UI label for the claims. | [optional] 
**user_attribute_mappings** | **str** | A user attribute to map values from. | [optional] 
**user_attribute_macros** | **str** | When &#x60;user_attribute_mappings&#x60; is set to &#x60;_macro_&#x60; this macro will be used to assign the claims value. | [optional] 
**attribute_transformations** | **str** | The type of transformation to perform on multi valued attributes. | [optional] 
**skip_if_blank** | **bool** | not used | [optional] 
**values** | **List[str]** | Relates to Rules/Entitlements. Not supported yet. | [optional] 
**default_values** | **str** | Relates to Rules/Entitlements. Not supported yet. | [optional] 
**provisioned_entitlements** | **bool** | Relates to Rules/Entitlements. Not supported yet. | [optional] 

## Example

```python
from onelogin.models.get_authclaims200_response_inner import GetAuthclaims200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetAuthclaims200ResponseInner from a JSON string
get_authclaims200_response_inner_instance = GetAuthclaims200ResponseInner.from_json(json)
# print the JSON string representation of the object
print GetAuthclaims200ResponseInner.to_json()

# convert the object into a dict
get_authclaims200_response_inner_dict = get_authclaims200_response_inner_instance.to_dict()
# create an instance of GetAuthclaims200ResponseInner from a dict
get_authclaims200_response_inner_form_dict = get_authclaims200_response_inner.from_dict(get_authclaims200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


