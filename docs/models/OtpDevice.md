# onelogin.model.otp_device.OtpDevice

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**number** | str,  | str,  | The phone number of the user in E.164 format. | 
**factor_id** | decimal.Decimal, int,  | decimal.Decimal,  | The identifier of the factor to enroll the user with. | 
**display_name** | str,  | str,  | A name for the users device | 
**verified** | bool,  | BoolClass,  | Defaults to false. Some factors like SMS or Voice require that a user recieve a token and then that token is supplied to the Verify endpoint before the device is considered active. You can set verfied to &#x60;true&#x60; which indicates the the users phone number is pre verified and the device can be immediately activated.            | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

