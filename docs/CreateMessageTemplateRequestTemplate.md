# CreateMessageTemplateRequestTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subject** | **str** | Custom Email Subject | 
**html** | **str** | The HTML body of the Custom Email | 
**plain** | **str** | The Plain text body of the email | 
**message** | **str** | The body of the SMS message. Max length 160 characters. | 

## Example

```python
from openapi_client.models.create_message_template_request_template import CreateMessageTemplateRequestTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMessageTemplateRequestTemplate from a JSON string
create_message_template_request_template_instance = CreateMessageTemplateRequestTemplate.from_json(json)
# print the JSON string representation of the object
print CreateMessageTemplateRequestTemplate.to_json()

# convert the object into a dict
create_message_template_request_template_dict = create_message_template_request_template_instance.to_dict()
# create an instance of CreateMessageTemplateRequestTemplate from a dict
create_message_template_request_template_form_dict = create_message_template_request_template.from_dict(create_message_template_request_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


