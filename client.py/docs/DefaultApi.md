# openapi_client.DefaultApi

All URIs are relative to *https://trading-api.kalshi.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_trades**](DefaultApi.md#get_trades) | **GET** /trades | GetTrades


# **get_trades**
> TradesGetResponse get_trades()

GetTrades

End-point for getting all trades for all markets.

### Example

```python
import time
import openapi_client
from openapi_client.api import default_api
from openapi_client.model.trades_get_response import TradesGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://trading-api.kalshi.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://trading-api.kalshi.com/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    trades_date = "trades_date_example" # str | Restricts the response to trades during a certain day. Format: YYYY-MM-DD (optional)
    page_size = 1 # int | Parameter to specify the number of results per page (optional)
    page_number = 1 # int | Parameter to specify which page of the results should be retrieved (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GetTrades
        api_response = api_instance.get_trades(trades_date=trades_date, page_size=page_size, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DefaultApi->get_trades: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trades_date** | **str**| Restricts the response to trades during a certain day. Format: YYYY-MM-DD | [optional]
 **page_size** | **int**| Parameter to specify the number of results per page | [optional]
 **page_number** | **int**| Parameter to specify which page of the results should be retrieved | [optional]

### Return type

[**TradesGetResponse**](TradesGetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  -  |
**400** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**401** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**403** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**500** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

