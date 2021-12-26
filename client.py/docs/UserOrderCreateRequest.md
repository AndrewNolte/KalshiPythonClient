# UserOrderCreateRequest

Request for submitting an order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | Specifies how many contracts should be bought | 
**market_id** | **str** | Specifies the id of the market for this order | 
**price** | **int** |  | 
**side** | **str** | Specifies if this is a &#39;yes&#39; or &#39;no&#39; order | 
**expiration_unix_ts** | **int** | Specifies the expiration time of the order, in unix seconds.  If this is not supplied, or is 0, the order won&#39;t expire. | [optional] 
**max_cost_cents** | **int** |  | [optional] 
**sell_position_capped** | **bool** | Specifies whether the order place count should be capped by the members current position. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


