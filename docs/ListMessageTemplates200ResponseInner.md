# ListMessageTemplates200ResponseInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | template ID | [optional] 
**enabled** | **bool** | indicator if template is enabled | [optional] 
**name** | **str** | name of message template | [optional] 

## Example

```python
from onelogin.models.list_message_templates200_response_inner import ListMessageTemplates200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListMessageTemplates200ResponseInner from a JSON string
list_message_templates200_response_inner_instance = ListMessageTemplates200ResponseInner.from_json(json)
# print the JSON string representation of the object
print ListMessageTemplates200ResponseInner.to_json()

# convert the object into a dict
list_message_templates200_response_inner_dict = list_message_templates200_response_inner_instance.to_dict()
# create an instance of ListMessageTemplates200ResponseInner from a dict
list_message_templates200_response_inner_form_dict = list_message_templates200_response_inner.from_dict(list_message_templates200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


