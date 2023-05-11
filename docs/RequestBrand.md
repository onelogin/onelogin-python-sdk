# RequestBrand


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Indicates if the brand is enabled or not | [optional] [default to False]
**name** | **str** | Brand’s name for humans. This isn’t related to subdomains. | 
**custom_support_enabled** | **bool** | Indicates if the custom support is enabled. If enabled, the login page includes the ability to submit a support request. | [optional] 
**custom_color** | **str** | Primary brand color | [optional] 
**custom_accent_color** | **str** | Secondary brand color | [optional] 
**custom_masking_color** | **str** | Color for the masking layer above the background image of the branded login screen. | [optional] 
**custom_masking_opacity** | **int** | Opacity for the custom_masking_color. | [optional] 
**enable_custom_label_for_login_screen** | **bool** | Indicates if the custom Username/Email field label is enabled or not | [optional] 
**custom_label_text_for_login_screen** | **str** | Custom label for the Username/Email field on the login screen. See example here. | [optional] 
**login_instruction_title** | **str** | Link text to show login instruction screen. | [optional] 
**login_instruction** | **str** | Text for the login instruction screen, styled in Markdown. | [optional] 
**hide_onelogin_footer** | **bool** | Indicates if the OneLogin footer will appear at the bottom of the login page. | [optional] 
**mfa_enrollment_message** | **str** | Text that replaces the default text displayed on the initial screen of the MFA Registration. | [optional] 
**background** | **str** | Base64 encoded image data (JPG/PNG, &lt;5MB) | [optional] 
**logo** | **str** | Base64 encoded image data (PNG, &lt;1MB) | [optional] 

## Example

```python
from onelogin.models.request_brand import RequestBrand

# TODO update the JSON string below
json = "{}"
# create an instance of RequestBrand from a JSON string
request_brand_instance = RequestBrand.from_json(json)
# print the JSON string representation of the object
print RequestBrand.to_json()

# convert the object into a dict
request_brand_dict = request_brand_instance.to_dict()
# create an instance of RequestBrand from a dict
request_brand_form_dict = request_brand.from_dict(request_brand_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


