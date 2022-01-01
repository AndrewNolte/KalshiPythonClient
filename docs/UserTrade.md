# UserTrade

Represents a trade from the user perspective.  A trade is created whenever an order is fully or partially matched, so there can be multiple trades with the same order_id. It is guaranteed that the sum of the count field for all the trades with the same order_id field shouldn't exceed the place_count on the order.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**create_date** | **datetime** |  | [optional] 
**id** | **str** |  | [optional] 
**is_taker** | **bool** |  | [optional] 
**is_yes** | **bool** |  | [optional] 
**market_id** | **str** |  | [optional] 
**order_id** | **str** |  | [optional] 
**price** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


