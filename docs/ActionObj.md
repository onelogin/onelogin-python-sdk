# ActionObj


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action to apply | [optional] 
**value** | **List[str]** | Only applicable to provisioned and set_* actions. Items in the array will be a plain text string or valid value for the selected action. | [optional] 

## Example

```python
from onelogin.models.action_obj import ActionObj

# TODO update the JSON string below
json = "{}"
# create an instance of ActionObj from a JSON string
action_obj_instance = ActionObj.from_json(json)
# print the JSON string representation of the object
print ActionObj.to_json()

# convert the object into a dict
action_obj_dict = action_obj_instance.to_dict()
# create an instance of ActionObj from a dict
action_obj_form_dict = action_obj.from_dict(action_obj_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


