# kalshi.RangedMarketsApi

All URIs are relative to *https://trading-api.kalshi.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ranged_market_by_ticker**](RangedMarketsApi.md#get_ranged_market_by_ticker) | **GET** /ranged_markets_by_ticker/{ticker} | GetRangedMarketByTicker


# **get_ranged_market_by_ticker**
> GetRangedMarketByTickerResponse get_ranged_market_by_ticker(ticker)

GetRangedMarketByTicker

End-point for getting data about a ranged market by its ticker

### Example

```python
import time
import kalshi
from kalshi.api import ranged_markets_api
from kalshi.model.get_ranged_market_by_ticker_response import GetRangedMarketByTickerResponse
from pprint import pprint
# Defining the host is optional and defaults to https://trading-api.kalshi.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kalshi.Configuration(
    host = "https://trading-api.kalshi.com/v1"
)


# Enter a context with an instance of the API client
with kalshi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = ranged_markets_api.RangedMarketsApi(api_client)
    ticker = "ticker_example" # str | Should be the ticker of the ranged market

    # example passing only required values which don't have defaults set
    try:
        # GetRangedMarketByTicker
        api_response = api_instance.get_ranged_market_by_ticker(ticker)
        pprint(api_response)
    except kalshi.ApiException as e:
        print("Exception when calling RangedMarketsApi->get_ranged_market_by_ticker: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ticker** | **str**| Should be the ticker of the ranged market |

### Return type

[**GetRangedMarketByTickerResponse**](GetRangedMarketByTickerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | GetRangedMarketByTickerResponse |  -  |
**400** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**401** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**403** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**404** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**500** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

