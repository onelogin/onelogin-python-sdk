# onelogin.model.user.User

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**username** | str,  | str,  | A username for the user. | [optional] 
**email** | str,  | str,  | A valid email for the user. | [optional] 
**firstname** | str,  | str,  | The user&#x27;s first name. | [optional] 
**lastname** | str,  | str,  | The user&#x27;s last name. | [optional] 
**title** | str,  | str,  | The user&#x27;s job title. | [optional] 
**department** | str,  | str,  | The user&#x27;s department. | [optional] 
**company** | str,  | str,  | The user&#x27;s company. | [optional] 
**comment** | str,  | str,  | Free text related to the user. | [optional] 
**group_id** | decimal.Decimal, int,  | decimal.Decimal,  | The ID of the Group in OneLogin that the user is assigned to. | [optional] 
**[role_ids](#role_ids)** | list, tuple,  | tuple,  | A list of OneLogin Role IDs of the user | [optional] 
**phone** | str,  | str,  | The E.164 format phone number for a user. | [optional] 
**state** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [0, 1, 2, 3, ] 
**status** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] must be one of [0, 1, 2, 3, 4, 5, 7, 8, ] 
**directory_id** | decimal.Decimal, int,  | decimal.Decimal,  | The ID of the OneLogin Directory of the user. | [optional] 
**trusted_idp_id** | decimal.Decimal, int,  | decimal.Decimal,  | The ID of the OneLogin Trusted IDP of the user. | [optional] 
**manager_ad_id** | str,  | str,  | The ID of the user&#x27;s manager in Active Directory. | [optional] 
**manager_user_id** | str,  | str,  | The OneLogin User ID for the user&#x27;s manager. | [optional] 
**samaccountname** | str,  | str,  | The user&#x27;s Active Directory username. | [optional] 
**member_of** | str,  | str,  | The user&#x27;s directory membership. | [optional] 
**userprincipalname** | str,  | str,  | The principle name of the user. | [optional] 
**distinguished_name** | str,  | str,  | The distinguished name of the user. | [optional] 
**external_id** | str,  | str,  | The ID of the user in an external directory. | [optional] 
**activated_at** | str,  | str,  |  | [optional] 
**last_login** | str,  | str,  |  | [optional] 
**invitation_sent_at** | str,  | str,  |  | [optional] 
**updated_at** | str,  | str,  |  | [optional] 
**preferred_locale_code** | str,  | str,  |  | [optional] 
**created_at** | str,  | str,  |  | [optional] 
**invalid_login_attempts** | decimal.Decimal, int,  | decimal.Decimal,  |  | [optional] 
**locked_until** | str,  | str,  |  | [optional] 
**password_changed_at** | str,  | str,  |  | [optional] 
**password** | str,  | str,  | The password to set for a user. | [optional] 
**password_confirmation** | str,  | str,  | Required if the password is being set. | [optional] 
**password_algorithm** | str,  | str,  | Use this when importing a password that&#x27;s already hashed. Prepend the salt value to the cleartext password value before SHA-256-encoding it | [optional] 
**salt** | str,  | str,  | The salt value used with the password_algorithm. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# role_ids

A list of OneLogin Role IDs of the user

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | A list of OneLogin Role IDs of the user | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | decimal.Decimal, int,  | decimal.Decimal,  |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

