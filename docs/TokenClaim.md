# TokenClaim


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
from onelogin.models.token_claim import TokenClaim

# TODO update the JSON string below
json = "{}"
# create an instance of TokenClaim from a JSON string
token_claim_instance = TokenClaim.from_json(json)
# print the JSON string representation of the object
print TokenClaim.to_json()

# convert the object into a dict
token_claim_dict = token_claim_instance.to_dict()
# create an instance of TokenClaim from a dict
token_claim_form_dict = token_claim.from_dict(token_claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


