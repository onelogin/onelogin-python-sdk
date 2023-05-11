# CreateApp200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Apps unique ID in OneLogin. | [optional] [readonly] 
**name** | **str** | The name of the app. | 
**visible** | **bool** | Indicates if the app is visible in the OneLogin portal. | 
**description** | **str** | Freeform description of the app. | 
**notes** | **str** | Freeform notes about the app. | [optional] 
**icon_url** | **str** | A link to the apps icon url | [optional] 
**auth_method** | [**AuthMethod**](AuthMethod.md) |  | [optional] 
**policy_id** | **int** | The security policy assigned to the app. | 
**allow_assumed_signin** | **bool** | Indicates whether or not administrators can access the app as a user that they have assumed control over. | [optional] 
**tab_id** | **int** | ID of the OneLogin portal tab that the app is assigned to. | [optional] 
**connector_id** | **int** | ID of the connector to base the app from. | 
**created_at** | **str** | the date the app was created | [optional] 
**updated_at** | **str** | the date the app was last updated | [optional] 
**role_ids** | **List[int]** | List of Role IDs that are assigned to the app. On App Create or Update the entire array is replaced with the values provided. | [optional] 
**provisioning** | [**GenericAppProvisioning**](GenericAppProvisioning.md) |  | [optional] 
**parameters** | [**AppParameters**](AppParameters.md) |  | [optional] 
**enforcement_point** | [**EnforcementPoint**](EnforcementPoint.md) |  | [optional] 
**configuration** | [**ConfigurationSaml**](ConfigurationSaml.md) |  | 
**sso** | [**SsoSaml**](SsoSaml.md) |  | [optional] 

## Example

```python
from onelogin.models.create_app200_response import CreateApp200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateApp200Response from a JSON string
create_app200_response_instance = CreateApp200Response.from_json(json)
# print the JSON string representation of the object
print CreateApp200Response.to_json()

# convert the object into a dict
create_app200_response_dict = create_app200_response_instance.to_dict()
# create an instance of CreateApp200Response from a dict
create_app200_response_form_dict = create_app200_response.from_dict(create_app200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


