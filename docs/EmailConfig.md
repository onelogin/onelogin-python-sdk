# EmailConfig


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** | Email Settings server address | 
**use_tls** | **bool** | Use TLS | [optional] [default to True]
**var_from** | **str** | The From email address in the message. | 
**domain** | **str** | Domain of the From address. | 
**user_name** | **str** | The user name of the account to authenticate with the Email Settings server. | [optional] 
**password** | **str** | The password of the account to authenticate with the Email Settings server. | [optional] 
**port** | **int** | Defaults to 25. | [optional] [default to 25]

## Example

```python
from onelogin.models.email_config import EmailConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EmailConfig from a JSON string
email_config_instance = EmailConfig.from_json(json)
# print the JSON string representation of the object
print EmailConfig.to_json()

# convert the object into a dict
email_config_dict = email_config_instance.to_dict()
# create an instance of EmailConfig from a dict
email_config_form_dict = email_config.from_dict(email_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


