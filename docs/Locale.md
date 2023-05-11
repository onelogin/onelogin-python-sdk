# Locale


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**language** | **str** | locale string | [optional] 
**is_default** | **bool** | indicator if language is default | [optional] 

## Example

```python
from onelogin.models.locale import Locale

# TODO update the JSON string below
json = "{}"
# create an instance of Locale from a JSON string
locale_instance = Locale.from_json(json)
# print the JSON string representation of the object
print Locale.to_json()

# convert the object into a dict
locale_dict = locale_instance.to_dict()
# create an instance of Locale from a dict
locale_form_dict = locale.from_dict(locale_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


