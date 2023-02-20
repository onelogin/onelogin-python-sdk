# ListConditionOperators200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the operator | [optional] 
**value** | **str** | The condition operator value to use when creating or updating rules. | [optional] 

## Example

```python
from openapi_client.models.list_condition_operators200_response_inner import ListConditionOperators200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListConditionOperators200ResponseInner from a JSON string
list_condition_operators200_response_inner_instance = ListConditionOperators200ResponseInner.from_json(json)
# print the JSON string representation of the object
print ListConditionOperators200ResponseInner.to_json()

# convert the object into a dict
list_condition_operators200_response_inner_dict = list_condition_operators200_response_inner_instance.to_dict()
# create an instance of ListConditionOperators200ResponseInner from a dict
list_condition_operators200_response_inner_form_dict = list_condition_operators200_response_inner.from_dict(list_condition_operators200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


