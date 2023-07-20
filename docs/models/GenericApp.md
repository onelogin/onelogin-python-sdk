# onelogin.model.generic_app.GenericApp

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  | Apps unique ID in OneLogin. | [optional] 
**name** | str,  | str,  | The name of the app. | [optional] 
**visible** | bool,  | BoolClass,  | Indicates if the app is visible in the OneLogin portal. | [optional] 
**description** | str,  | str,  | Freeform description of the app. | [optional] 
**notes** | str,  | str,  | Freeform notes about the app. | [optional] 
**icon_url** | str,  | str,  | A link to the apps icon url | [optional] 
**auth_method** | [**AuthMethod**](AuthMethod.md) | [**AuthMethod**](AuthMethod.md) |  | [optional] 
**policy_id** | decimal.Decimal, int,  | decimal.Decimal,  | The security policy assigned to the app. | [optional] 
**allow_assumed_signin** | bool,  | BoolClass,  | Indicates whether or not administrators can access the app as a user that they have assumed control over. | [optional] 
**tab_id** | decimal.Decimal, int,  | decimal.Decimal,  | ID of the OneLogin portal tab that the app is assigned to. | [optional] 
**connector_id** | decimal.Decimal, int,  | decimal.Decimal,  | ID of the connector to base the app from. | [optional] 
**created_at** | str,  | str,  | the date the app was created | [optional] 
**updated_at** | str,  | str,  | the date the app was last updated | [optional] 
**[role_ids](#role_ids)** | list, tuple,  | tuple,  | List of Role IDs that are assigned to the app. On App Create or Update the entire array is replaced with the values provided. | [optional] 
**[provisioning](#provisioning)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | Indicates if provisioning is enabled for this app. | [optional] 
**parameters** | [**AppParameters**](AppParameters.md) | [**AppParameters**](AppParameters.md) |  | [optional] 
**enforcement_point** | [**EnforcementPoint**](EnforcementPoint.md) | [**EnforcementPoint**](EnforcementPoint.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# role_ids

List of Role IDs that are assigned to the app. On App Create or Update the entire array is replaced with the values provided.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | List of Role IDs that are assigned to the app. On App Create or Update the entire array is replaced with the values provided. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  | Role ID | 

# provisioning

Indicates if provisioning is enabled for this app.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Indicates if provisioning is enabled for this app. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**enabled** | bool,  | BoolClass,  |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

