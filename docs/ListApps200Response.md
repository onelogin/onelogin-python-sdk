# ListApps200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Apps unique ID in OneLogin. | [optional] 
**connector_id** | **int** | ID of the apps underlying connector. | [optional] 
**name** | **str** | App name. | [optional] 
**description** | **str** | Freeform description of the app. | [optional] 
**notes** | **str** | Freeform notes about the app. | [optional] 
**policy_id** | **int** | The security policy assigned to the app. | [optional] 
**brand_id** | **int** | The custom login page branding to use for this app. Applies to app initiated logins via OIDC or SAML. | [optional] 
**icon_url** | **str** | A link to the apps icon url. | [optional] 
**visible** | **bool** | Indicates if the app is visible in the OneLogin portal. | [optional] 
**auth_method** | **int** | An ID indicating the type of app. | [optional] 
**tab_id** | **int** | ID of the OneLogin portal tab that the app is assigned to. | [optional] 
**created_at** | **str** | The date the app was created. | [optional] 
**updated_at** | **str** | The date the app was last updated. | [optional] 
**role_ids** | **List[int]** | A list of OneLogin Role IDs of the user | [optional] 
**allow_assumed_signin** | **bool** | Indicates whether or not administrators can access the app as a user that they have assumed control over. | [optional] 
**provisioning** | [**ListApps200ResponseProvisioning**](ListApps200ResponseProvisioning.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_apps200_response import ListApps200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListApps200Response from a JSON string
list_apps200_response_instance = ListApps200Response.from_json(json)
# print the JSON string representation of the object
print ListApps200Response.to_json()

# convert the object into a dict
list_apps200_response_dict = list_apps200_response_instance.to_dict()
# create an instance of ListApps200Response from a dict
list_apps200_response_form_dict = list_apps200_response.from_dict(list_apps200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


