# onelogin.model.brand.Brand

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**custom_label_text_for_login_screen** | str,  | str,  | Custom label for the Username/Email field on the login screen. See example here. | 
**login_instruction** | str,  | str,  | Text for the login instruction screen, styled in Markdown. | 
**custom_masking_color** | str,  | str,  | Color for the masking layer above the background image of the branded login screen. | 
**custom_masking_opacity** | decimal.Decimal, int,  | decimal.Decimal,  | Opacity for the custom_masking_color. | 
**enabled** | bool,  | BoolClass,  | Indicates if the brand is enabled or not | if omitted the server will use the default value of False
**mfa_enrollment_message** | str,  | str,  | Text that replaces the default text displayed on the initial screen of the MFA Registration. | 
**custom_color** | str,  | str,  | Primary brand color | 
**[background](#background)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**custom_support_enabled** | bool,  | BoolClass,  | Indicates if the custom support is enabled. If enabled, the login page includes the ability to submit a support request. | 
**enable_custom_label_for_login_screen** | bool,  | BoolClass,  | Indicates if the custom Username/Email field label is enabled or not | 
**hide_onelogin_footer** | bool,  | BoolClass,  | Indicates if the OneLogin footer will appear at the bottom of the login page. | 
**[logo](#logo)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**custom_accent_color** | str,  | str,  | Secondary brand color | 
**id** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**login_instruction_title** | str,  | str,  | Link text to show login instruction screen. | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# background

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[urls](#urls)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**content_type** | str,  | str,  |  | 
**updated_at** | str,  | str,  |  | 
**file_size** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# urls

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**original** | str,  | str,  |  | 
**branding** | str,  | str,  |  | 
**login** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# logo

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**[urls](#urls)** | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 
**content_type** | str,  | str,  |  | 
**updated_at** | str,  | str,  |  | 
**file_size** | decimal.Decimal, int,  | decimal.Decimal,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# urls

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**navigation** | str,  | str,  |  | 
**original** | str,  | str,  |  | 
**login** | str,  | str,  |  | 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

