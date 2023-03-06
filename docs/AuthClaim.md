# AuthClaim


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The attribute name for the claim when its returned in an Access Token | 
**user_attribute_mappings** | **str** | A user attribute to map values from For custom attributes prefix the name of the attribute with &#x60;custom_attribute_&#x60;. e.g. To get the value for custom attribute &#x60;employee_id&#x60; use &#x60;custom_attribute_employee_id&#x60;. | [optional] 
**user_attribute_macros** | **str** | When &#x60;user_attribute_mappings&#x60; is set to &#x60;_macro_&#x60; this macro will be used to assign the parameter value. | [optional] 

## Example

```python
from onelogin.models.auth_claim import AuthClaim

# TODO update the JSON string below
json = "{}"
# create an instance of AuthClaim from a JSON string
auth_claim_instance = AuthClaim.from_json(json)
# print the JSON string representation of the object
print AuthClaim.to_json()

# convert the object into a dict
auth_claim_dict = auth_claim_instance.to_dict()
# create an instance of AuthClaim from a dict
auth_claim_form_dict = auth_claim.from_dict(auth_claim_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


