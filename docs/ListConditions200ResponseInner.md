# ListConditions200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the rule condition | [optional] 
**value** | **str** | The unique identifier of the condition. This should be used when defining conditions for a rule. | [optional] 

## Example

```python
from onelogin.models.list_conditions200_response_inner import ListConditions200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListConditions200ResponseInner from a JSON string
list_conditions200_response_inner_instance = ListConditions200ResponseInner.from_json(json)
# print the JSON string representation of the object
print ListConditions200ResponseInner.to_json()

# convert the object into a dict
list_conditions200_response_inner_dict = list_conditions200_response_inner_instance.to_dict()
# create an instance of ListConditions200ResponseInner from a dict
list_conditions200_response_inner_form_dict = list_conditions200_response_inner.from_dict(list_conditions200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


