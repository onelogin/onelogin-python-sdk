# Source

Used for targeting custom rules based on a group of people, customers, accounts, or even a single user.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique id that represents the source of the event. | [optional] 
**name** | **str** | The name of the source | [optional] 

## Example

```python
from onelogin.models.source import Source

# TODO update the JSON string below
json = "{}"
# create an instance of Source from a JSON string
source_instance = Source.from_json(json)
# print the JSON string representation of the object
print Source.to_json()

# convert the object into a dict
source_dict = source_instance.to_dict()
# create an instance of Source from a dict
source_form_dict = source.from_dict(source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


