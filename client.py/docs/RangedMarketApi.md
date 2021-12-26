# openapi_client.RangedMarketApi

All URIs are relative to *https://trading-api.kalshi.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ranged_market**](RangedMarketApi.md#get_ranged_market) | **GET** /ranged_markets/{ranged_market_id} | GetRangedMarket


# **get_ranged_market**
> GetRangedMarketResponse get_ranged_market(ranged_market_id)

GetRangedMarket

End-point for getting data about a ranged market

### Example

```python
import time
import openapi_client
from openapi_client.api import ranged_market_api
from openapi_client.model.get_ranged_market_response import GetRangedMarketResponse
from pprint import pprint
# Defining the host is optional and defaults to https://trading-api.kalshi.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://trading-api.kalshi.com/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ranged_market_api.RangedMarketApi(api_client)
    ranged_market_id = "ranged_market_id_example" # str | Should be filled in with a ranged market id

    # example passing only required values which don't have defaults set
    try:
        # GetRangedMarket
        api_response = api_instance.get_ranged_market(ranged_market_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling RangedMarketApi->get_ranged_market: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ranged_market_id** | **str**| Should be filled in with a ranged market id |

### Return type

[**GetRangedMarketResponse**](GetRangedMarketResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GetRangedMarketResponse |  -  |
**400** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**401** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**403** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**404** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**500** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

