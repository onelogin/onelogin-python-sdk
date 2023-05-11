# MessageTemplateTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | Custom Email Subject | 
**html** | **str** | The HTML body of the Custom Email | 
**plain** | **str** | The Plain text body of the email | 
**message** | **str** | The body of the SMS message. Max length 160 characters. | 

## Example

```python
from onelogin.models.message_template_template import MessageTemplateTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of MessageTemplateTemplate from a JSON string
message_template_template_instance = MessageTemplateTemplate.from_json(json)
# print the JSON string representation of the object
print MessageTemplateTemplate.to_json()

# convert the object into a dict
message_template_template_dict = message_template_template_instance.to_dict()
# create an instance of MessageTemplateTemplate from a dict
message_template_template_form_dict = message_template_template.from_dict(message_template_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


