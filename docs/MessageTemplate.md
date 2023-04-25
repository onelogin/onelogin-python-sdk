# MessageTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] [readonly] 
**account_id** | **int** |  | [optional] [readonly] 
**type** | **str** | Template type that describes the source (sms, voice, email) and purpose (registration, invite, etc) | 
**locale** | **str** | The 2 character language locale for the template. e.g. en &#x3D; English, es &#x3D; Spanish | 
**template** | [**MessageTemplateTemplate**](MessageTemplateTemplate.md) |  | 
**template_class** | **str** |  | [optional] [readonly] 
**updated_at** | **str** | Last time template was updated | [optional] [readonly] 
**brand_id** | **int** | brand id number | [optional] [readonly] 

## Example

```python
from onelogin.models.message_template import MessageTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of MessageTemplate from a JSON string
message_template_instance = MessageTemplate.from_json(json)
# print the JSON string representation of the object
print MessageTemplate.to_json()

# convert the object into a dict
message_template_dict = message_template_instance.to_dict()
# create an instance of MessageTemplate from a dict
message_template_form_dict = message_template.from_dict(message_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


