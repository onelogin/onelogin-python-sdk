# AuthId


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for the Scope | [optional] 

## Example

```python
from onelogin.models.auth_id import AuthId

# TODO update the JSON string below
json = "{}"
# create an instance of AuthId from a JSON string
auth_id_instance = AuthId.from_json(json)
# print the JSON string representation of the object
print AuthId.to_json()

# convert the object into a dict
auth_id_dict = auth_id_instance.to_dict()
# create an instance of AuthId from a dict
auth_id_form_dict = auth_id.from_dict(auth_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


