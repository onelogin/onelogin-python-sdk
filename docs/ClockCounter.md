# ClockCounter

unit: - 0 = Seconds - 1 = Minutes - 2 = Hours value: - When Unit = 0 or 1 value must be 0-60 - When Unit = 2 value must be 0-24

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** |  | [optional] 
**unit** | **int** |  | [optional] 

## Example

```python
from onelogin.models.clock_counter import ClockCounter

# TODO update the JSON string below
json = "{}"
# create an instance of ClockCounter from a JSON string
clock_counter_instance = ClockCounter.from_json(json)
# print the JSON string representation of the object
print ClockCounter.to_json()

# convert the object into a dict
clock_counter_dict = clock_counter_instance.to_dict()
# create an instance of ClockCounter from a dict
clock_counter_form_dict = clock_counter.from_dict(clock_counter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


