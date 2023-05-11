# Session

A dictionary of extra information that provides useful context about the session, for example the session ID, or some cookie information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | If you use a database to track sessions, you can send us the session ID. | [optional] 

## Example

```python
from onelogin.models.session import Session

# TODO update the JSON string below
json = "{}"
# create an instance of Session from a JSON string
session_instance = Session.from_json(json)
# print the JSON string representation of the object
print Session.to_json()

# convert the object into a dict
session_dict = session_instance.to_dict()
# create an instance of Session from a dict
session_form_dict = session.from_dict(session_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


