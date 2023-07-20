# onelogin.model.request_brand.RequestBrand

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Brand’s name for humans. This isn’t related to subdomains. | 
**enabled** | bool,  | BoolClass,  | Indicates if the brand is enabled or not | [optional] if omitted the server will use the default value of False
**custom_support_enabled** | bool,  | BoolClass,  | Indicates if the custom support is enabled. If enabled, the login page includes the ability to submit a support request. | [optional] 
**custom_color** | str,  | str,  | Primary brand color | [optional] 
**custom_accent_color** | str,  | str,  | Secondary brand color | [optional] 
**custom_masking_color** | str,  | str,  | Color for the masking layer above the background image of the branded login screen. | [optional] 
**custom_masking_opacity** | decimal.Decimal, int,  | decimal.Decimal,  | Opacity for the custom_masking_color. | [optional] 
**enable_custom_label_for_login_screen** | bool,  | BoolClass,  | Indicates if the custom Username/Email field label is enabled or not | [optional] 
**custom_label_text_for_login_screen** | str,  | str,  | Custom label for the Username/Email field on the login screen. See example here. | [optional] 
**login_instruction_title** | str,  | str,  | Link text to show login instruction screen. | [optional] 
**login_instruction** | str,  | str,  | Text for the login instruction screen, styled in Markdown. | [optional] 
**hide_onelogin_footer** | bool,  | BoolClass,  | Indicates if the OneLogin footer will appear at the bottom of the login page. | [optional] 
**mfa_enrollment_message** | str,  | str,  | Text that replaces the default text displayed on the initial screen of the MFA Registration. | [optional] 
**background** | str,  | str,  | Base64 encoded image data (JPG/PNG, &lt;5MB) | [optional] 
**logo** | str,  | str,  | Base64 encoded image data (PNG, &lt;1MB) | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

