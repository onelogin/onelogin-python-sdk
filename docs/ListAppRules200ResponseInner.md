# ListAppRules200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | App Rule ID | [optional] 
**name** | **str** | Rule Name | [optional] 
**match** | **str** | Indicates how conditions should be matched. | [optional] 
**enabled** | **bool** | Indicates if the rule is enabled or not. | [optional] 
**position** | **int** | Indicates the order of the rule. When &#x60;null&#x60; this will default to last position. | [optional] 
**conditions** | [**List[ListMappings200ResponseInnerConditionsInner]**](ListMappings200ResponseInnerConditionsInner.md) | An array of conditions that the user must meet in order for the rule to be applied. | [optional] 
**actions** | [**List[ListMappings200ResponseInnerActionsInner]**](ListMappings200ResponseInnerActionsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_app_rules200_response_inner import ListAppRules200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListAppRules200ResponseInner from a JSON string
list_app_rules200_response_inner_instance = ListAppRules200ResponseInner.from_json(json)
# print the JSON string representation of the object
print ListAppRules200ResponseInner.to_json()

# convert the object into a dict
list_app_rules200_response_inner_dict = list_app_rules200_response_inner_instance.to_dict()
# create an instance of ListAppRules200ResponseInner from a dict
list_app_rules200_response_inner_form_dict = list_app_rules200_response_inner.from_dict(list_app_rules200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


