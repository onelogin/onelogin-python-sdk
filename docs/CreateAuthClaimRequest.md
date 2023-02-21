# CreateAuthClaimRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The attribute name for the claim when its returned in an Access Token | 
**user_attribute_mappings** | **str** | A user attribute to map values from For custom attributes prefix the name of the attribute with &#x60;custom_attribute_&#x60;. e.g. To get the value for custom attribute &#x60;employee_id&#x60; use &#x60;custom_attribute_employee_id&#x60;. | [optional] 
**user_attribute_macros** | **str** | When &#x60;user_attribute_mappings&#x60; is set to &#x60;_macro_&#x60; this macro will be used to assign the parameter value. | [optional] 

## Example

```python
from onelogin.models.create_auth_claim_request import CreateAuthClaimRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuthClaimRequest from a JSON string
create_auth_claim_request_instance = CreateAuthClaimRequest.from_json(json)
# print the JSON string representation of the object
print CreateAuthClaimRequest.to_json()

# convert the object into a dict
create_auth_claim_request_dict = create_auth_claim_request_instance.to_dict()
# create an instance of CreateAuthClaimRequest from a dict
create_auth_claim_request_form_dict = create_auth_claim_request.from_dict(create_auth_claim_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


