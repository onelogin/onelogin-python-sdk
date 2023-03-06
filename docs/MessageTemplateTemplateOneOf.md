# MessageTemplateTemplateOneOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | Custom Email Subject | 
**html** | **str** | The HTML body of the Custom Email | 
**plain** | **str** | The Plain text body of the email | 

## Example

```python
from onelogin.models.message_template_template_one_of import MessageTemplateTemplateOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of MessageTemplateTemplateOneOf from a JSON string
message_template_template_one_of_instance = MessageTemplateTemplateOneOf.from_json(json)
# print the JSON string representation of the object
print MessageTemplateTemplateOneOf.to_json()

# convert the object into a dict
message_template_template_one_of_dict = message_template_template_one_of_instance.to_dict()
# create an instance of MessageTemplateTemplateOneOf from a dict
message_template_template_one_of_form_dict = message_template_template_one_of.from_dict(message_template_template_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


