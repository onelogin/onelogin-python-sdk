# GetEmailSettings200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | [optional] 
**address** | **str** | Email Settings server address | 
**use_tls** | **bool** | Use TLS | [optional] [default to True]
**var_from** | **str** | The From email address in the message. | 
**domain** | **str** | Domain of the From address. | 
**user_name** | **str** | The user name of the account to authenticate with the Email Settings server. | [optional] 
**password** | **str** | The password of the account to authenticate with the Email Settings server. | [optional] 
**port** | **int** | Defaults to 25. | [optional] [default to 25]

## Example

```python
from onelogin.models.get_email_settings200_response import GetEmailSettings200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetEmailSettings200Response from a JSON string
get_email_settings200_response_instance = GetEmailSettings200Response.from_json(json)
# print the JSON string representation of the object
print GetEmailSettings200Response.to_json()

# convert the object into a dict
get_email_settings200_response_dict = get_email_settings200_response_instance.to_dict()
# create an instance of GetEmailSettings200Response from a dict
get_email_settings200_response_form_dict = get_email_settings200_response.from_dict(get_email_settings200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


