# Order

Represents user orders in the api.  When an order is matched multiple trades can be created this can be tracked by looking into the trade.order_id field.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**close_cancel_count** | **int** |  | [optional] 
**create_ts** | **datetime** |  | [optional] 
**decrease_count** | **int** |  | [optional] 
**expiration_ts** | **datetime** |  | [optional] 
**extra_cost** | **int** |  | [optional] 
**extra_count** | **int** |  | [optional] 
**fcc_cancel_count** | **int** |  | [optional] 
**is_yes** | **bool** |  | [optional] 
**last_update_op** | **str** |  | [optional] 
**maker_fill_count** | **int** |  | [optional] 
**market_id** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**place_count** | **int** |  | [optional] 
**price** | **int** |  | [optional] 
**queue_position** | **int** |  | [optional] 
**remaining_count** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**taker_fees** | **int** |  | [optional] 
**taker_fill_cost** | **int** |  | [optional] 
**taker_fill_count** | **int** |  | [optional] 
**user_id** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


