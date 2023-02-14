# CreateMessageTemplateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Template type that describes the source (sms, voice, email) and purpose (registration, invite, etc) | 
**locale** | **str** | The 2 character language locale for the template. e.g. en &#x3D; English, es &#x3D; Spanish | 
**template** | [**CreateMessageTemplateRequestTemplate**](CreateMessageTemplateRequestTemplate.md) |  | 
**updated_at** | **str** | Last time template was updated | [optional] 
**brand_id** | **int** | brand id number | [optional] 

## Example

```python
from openapi_client.models.create_message_template_request import CreateMessageTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateMessageTemplateRequest from a JSON string
create_message_template_request_instance = CreateMessageTemplateRequest.from_json(json)
# print the JSON string representation of the object
print CreateMessageTemplateRequest.to_json()

# convert the object into a dict
create_message_template_request_dict = create_message_template_request_instance.to_dict()
# create an instance of CreateMessageTemplateRequest from a dict
create_message_template_request_form_dict = create_message_template_request.from_dict(create_message_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


