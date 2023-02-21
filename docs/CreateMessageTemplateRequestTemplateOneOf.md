# CreateMessageTemplateRequestTemplateOneOf


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | Custom Email Subject | 
**html** | **str** | The HTML body of the Custom Email | 
**plain** | **str** | The Plain text body of the email | 

## Example

```python
from onelogin.models.create_message_template_request_template_one_of import CreateMessageTemplateRequestTemplateOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMessageTemplateRequestTemplateOneOf from a JSON string
create_message_template_request_template_one_of_instance = CreateMessageTemplateRequestTemplateOneOf.from_json(json)
# print the JSON string representation of the object
print CreateMessageTemplateRequestTemplateOneOf.to_json()

# convert the object into a dict
create_message_template_request_template_one_of_dict = create_message_template_request_template_one_of_instance.to_dict()
# create an instance of CreateMessageTemplateRequestTemplateOneOf from a dict
create_message_template_request_template_one_of_form_dict = create_message_template_request_template_one_of.from_dict(create_message_template_request_template_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


