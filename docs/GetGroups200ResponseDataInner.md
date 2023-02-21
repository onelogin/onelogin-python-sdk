# GetGroups200ResponseDataInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Group&#39;s unique Onelogin ID | [optional] 
**name** | **str** | Group name | [optional] 
**reference** | **str** | Deprecated. Will always show the attribute nil&#x3D;\&quot;true\&quot;. | [optional] 

## Example

```python
from onelogin.models.get_groups200_response_data_inner import GetGroups200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetGroups200ResponseDataInner from a JSON string
get_groups200_response_data_inner_instance = GetGroups200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print GetGroups200ResponseDataInner.to_json()

# convert the object into a dict
get_groups200_response_data_inner_dict = get_groups200_response_data_inner_instance.to_dict()
# create an instance of GetGroups200ResponseDataInner from a dict
get_groups200_response_data_inner_form_dict = get_groups200_response_data_inner.from_dict(get_groups200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


