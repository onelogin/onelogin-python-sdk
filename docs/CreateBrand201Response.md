# CreateBrand201Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**enabled** | **bool** | Indicates if the brand is enabled or not | [default to False]
**custom_support_enabled** | **bool** | Indicates if the custom support is enabled. If enabled, the login page includes the ability to submit a support request. | 
**custom_color** | **str** | Primary brand color | 
**custom_accent_color** | **str** | Secondary brand color | 
**custom_masking_color** | **str** | Color for the masking layer above the background image of the branded login screen. | 
**custom_masking_opacity** | **int** | Opacity for the custom_masking_color. | 
**mfa_enrollment_message** | **str** | Text that replaces the default text displayed on the initial screen of the MFA Registration. | 
**enable_custom_label_for_login_screen** | **bool** | Indicates if the custom Username/Email field label is enabled or not | 
**custom_label_text_for_login_screen** | **str** | Custom label for the Username/Email field on the login screen. See example here. | 
**login_instruction** | **str** | Text for the login instruction screen, styled in Markdown. | 
**login_instruction_title** | **str** | Link text to show login instruction screen. | 
**hide_onelogin_footer** | **bool** | Indicates if the OneLogin footer will appear at the bottom of the login page. | 
**background** | [**CreateBrand201ResponseBackground**](CreateBrand201ResponseBackground.md) |  | 
**logo** | [**CreateBrand201ResponseLogo**](CreateBrand201ResponseLogo.md) |  | 

## Example

```python
from openapi_client.models.create_brand201_response import CreateBrand201Response

# TODO update the JSON string below
json = "{}"
# create an instance of CreateBrand201Response from a JSON string
create_brand201_response_instance = CreateBrand201Response.from_json(json)
# print the JSON string representation of the object
print CreateBrand201Response.to_json()

# convert the object into a dict
create_brand201_response_dict = create_brand201_response_instance.to_dict()
# create an instance of CreateBrand201Response from a dict
create_brand201_response_form_dict = create_brand201_response.from_dict(create_brand201_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


