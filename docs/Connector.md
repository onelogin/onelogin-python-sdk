# Connector


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Connectors unique ID in OneLogin. | [optional] 
**name** | **str** | Name of Connector | [optional] 
**icon_url** | **str** | A link to the icon&#39;s url. | [optional] 
**auth_method** | [**AuthMethod**](AuthMethod.md) |  | [optional] 
**allows_new_parameters** | **bool** | Indicates if apps created using this connector will be allowed to create custom parameters. | [optional] 

## Example

```python
from onelogin.models.connector import Connector

# TODO update the JSON string below
json = "{}"
# create an instance of Connector from a JSON string
connector_instance = Connector.from_json(json)
# print the JSON string representation of the object
print Connector.to_json()

# convert the object into a dict
connector_dict = connector_instance.to_dict()
# create an instance of Connector from a dict
connector_form_dict = connector.from_dict(connector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


