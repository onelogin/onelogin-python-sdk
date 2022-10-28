# GenerateSamlAssertionRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username_or_email** | **str** | Set this to the username or email of the OneLogin user accessing the app for which you want to generate a SAML token. | 
**password** | **str** | Password of the OneLogin user accessing the app for which you want to generate a SAML token. | 
**app_id** | **str** | App ID of the app for which you want to generate a SAML token. This is the app ID in OneLogin. | 
**subdomain** | **str** | Set to the subdomain of the OneLogin user accessing the app for which you want to generate a SAML token. | 
**ip_address** | **str** | Whitelisted IP address, if MFA is required and you need to honor IP address whitelisting defined in MFA policies. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


