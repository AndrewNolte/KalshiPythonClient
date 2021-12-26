# openapi_client.UserApi

All URIs are relative to *https://trading-api.kalshi.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_add_watchlist**](UserApi.md#user_add_watchlist) | **PUT** /users/{user_id}/watchlist/{market_id} | UserAddWatchlist
[**user_change_password**](UserApi.md#user_change_password) | **PUT** /users/{user_id}/password | UserChangePassword
[**user_get_balance**](UserApi.md#user_get_balance) | **GET** /users/{user_id}/balance | UserGetBalance
[**user_get_market_position**](UserApi.md#user_get_market_position) | **GET** /users/{user_id}/positions/{market_id} | UserGetMarketPosition
[**user_get_market_positions**](UserApi.md#user_get_market_positions) | **GET** /users/{user_id}/positions | UserGetMarketPositions
[**user_get_profile**](UserApi.md#user_get_profile) | **GET** /users/{user_id} | UserGetProfile
[**user_get_watchlist**](UserApi.md#user_get_watchlist) | **GET** /users/{user_id}/watchlist | UserGetWatchlist
[**user_order_cancel**](UserApi.md#user_order_cancel) | **DELETE** /users/{user_id}/orders/{order_id} | UserOrderCancel
[**user_order_create**](UserApi.md#user_order_create) | **POST** /users/{user_id}/orders | UserOrderCreate
[**user_order_decrease**](UserApi.md#user_order_decrease) | **POST** /users/{user_id}/orders/{order_id}/decrease | UserOrderDecrease
[**user_orders_get**](UserApi.md#user_orders_get) | **GET** /users/{user_id}/orders | UserOrdersGet
[**user_remove_watchlist**](UserApi.md#user_remove_watchlist) | **DELETE** /users/{user_id}/watchlist/{market_id} | UserRemoveWatchlist
[**user_trades_get**](UserApi.md#user_trades_get) | **GET** /users/{user_id}/trades | UserTradesGet


# **user_add_watchlist**
> user_add_watchlist(user_id, market_id)

UserAddWatchlist

End-point for adding a market to the logged in user's watchlist.  The value for the user_id path parameter should match the user_id value returned on the response for the last login request (POST /log_in).  The value for the market_id path parameter should match the id value of the market to be added.

### Example

* Api Key Authentication (cookie):
```python
import time
import openapi_client
from openapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://trading-api.kalshi.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://trading-api.kalshi.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | user_id should be filled with your user_id provided on log_in
    market_id = "market_id_example" # str | market_id should be filled with the id of the market to be added to the watchlist

    # example passing only required values which don't have defaults set
    try:
        # UserAddWatchlist
        api_instance.user_add_watchlist(user_id, market_id)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->user_add_watchlist: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| user_id should be filled with your user_id provided on log_in |
 **market_id** | **str**| market_id should be filled with the id of the market to be added to the watchlist |

### Return type

void (empty response body)

### Authorization

[cookie](../README.md#cookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No fields are returned on the response. |  -  |
**400** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**401** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**403** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**404** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**500** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_change_password**
> user_change_password(user_id)

UserChangePassword

End-point for updating logged-in user password.  The value for the user_id path parameter should match the user_id value returned on the response for the last login request (POST /log_in).

### Example

* Api Key Authentication (cookie):
```python
import time
import openapi_client
from openapi_client.api import user_api
from openapi_client.model.user_change_password_request import UserChangePasswordRequest
from pprint import pprint
# Defining the host is optional and defaults to https://trading-api.kalshi.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://trading-api.kalshi.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | This parameter should be filled with your user_id provided on log_in
    user_change_password_request = UserChangePasswordRequest(
        new_password="new_password_example",
        old_password="old_password_example",
    ) # UserChangePasswordRequest | Change password input fields. (optional)

    # example passing only required values which don't have defaults set
    try:
        # UserChangePassword
        api_instance.user_change_password(user_id)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->user_change_password: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # UserChangePassword
        api_instance.user_change_password(user_id, user_change_password_request=user_change_password_request)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->user_change_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| This parameter should be filled with your user_id provided on log_in |
 **user_change_password_request** | [**UserChangePasswordRequest**](UserChangePasswordRequest.md)| Change password input fields. | [optional]

### Return type

void (empty response body)

### Authorization

[cookie](../README.md#cookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No fields are returned on the response. |  -  |
**400** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**401** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**403** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**500** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get_balance**
> UserGetBalanceResponse user_get_balance(user_id)

UserGetBalance

End-point for getting the balance of the logged in user.  The value for the user_id path parameter should match the user_id value returned on the response for the last login request (POST /log_in).

### Example

* Api Key Authentication (cookie):
```python
import time
import openapi_client
from openapi_client.api import user_api
from openapi_client.model.user_get_balance_response import UserGetBalanceResponse
from pprint import pprint
# Defining the host is optional and defaults to https://trading-api.kalshi.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://trading-api.kalshi.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | Should be filled with your user_id provided on log_in

    # example passing only required values which don't have defaults set
    try:
        # UserGetBalance
        api_response = api_instance.user_get_balance(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->user_get_balance: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Should be filled with your user_id provided on log_in |

### Return type

[**UserGetBalanceResponse**](UserGetBalanceResponse.md)

### Authorization

[cookie](../README.md#cookie)

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

# **user_get_market_position**
> UserGetMarketPositionResponse user_get_market_position(user_id, market_id)

UserGetMarketPosition

End-point for getting the market positions for the logged in user, in a specific market.  The value for the user_id path parameter should match the user_id value returned on the response for the last login request (POST /log_in).  The value for the market_id path parameter should match the id value of the target market.

### Example

* Api Key Authentication (cookie):
```python
import time
import openapi_client
from openapi_client.api import user_api
from openapi_client.model.user_get_market_position_response import UserGetMarketPositionResponse
from pprint import pprint
# Defining the host is optional and defaults to https://trading-api.kalshi.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://trading-api.kalshi.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | Should be filled with your user_id provided on log_in
    market_id = "market_id_example" # str | Should be filled with the id of the target market

    # example passing only required values which don't have defaults set
    try:
        # UserGetMarketPosition
        api_response = api_instance.user_get_market_position(user_id, market_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->user_get_market_position: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Should be filled with your user_id provided on log_in |
 **market_id** | **str**| Should be filled with the id of the target market |

### Return type

[**UserGetMarketPositionResponse**](UserGetMarketPositionResponse.md)

### Authorization

[cookie](../README.md#cookie)

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
**404** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**500** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get_market_positions**
> UserGetMarketPositionsResponse user_get_market_positions(user_id)

UserGetMarketPositions

End-point for getting all market positions for the logged in user.  The value for the user_id path parameter should match the user_id value returned on the response for the last login request (POST /log_in).

### Example

* Api Key Authentication (cookie):
```python
import time
import openapi_client
from openapi_client.api import user_api
from openapi_client.model.user_get_market_positions_response import UserGetMarketPositionsResponse
from pprint import pprint
# Defining the host is optional and defaults to https://trading-api.kalshi.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://trading-api.kalshi.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | Should be filled with your user_id provided on log_in

    # example passing only required values which don't have defaults set
    try:
        # UserGetMarketPositions
        api_response = api_instance.user_get_market_positions(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->user_get_market_positions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Should be filled with your user_id provided on log_in |

### Return type

[**UserGetMarketPositionsResponse**](UserGetMarketPositionsResponse.md)

### Authorization

[cookie](../README.md#cookie)

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

# **user_get_profile**
> UserGetProfileResponse user_get_profile(user_id)

UserGetProfile

End-point for retrieving the logged in user's profile.  The value for the user_id path parameter should match the user_id value returned on the response for the last login request (POST /log_in).

### Example

* Api Key Authentication (cookie):
```python
import time
import openapi_client
from openapi_client.api import user_api
from openapi_client.model.user_get_profile_response import UserGetProfileResponse
from pprint import pprint
# Defining the host is optional and defaults to https://trading-api.kalshi.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://trading-api.kalshi.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | Should be filled with your user_id provided on log_in

    # example passing only required values which don't have defaults set
    try:
        # UserGetProfile
        api_response = api_instance.user_get_profile(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->user_get_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Should be filled with your user_id provided on log_in |

### Return type

[**UserGetProfileResponse**](UserGetProfileResponse.md)

### Authorization

[cookie](../README.md#cookie)

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
**503** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get_watchlist**
> UserGetWatchlistResponse user_get_watchlist(user_id)

UserGetWatchlist

End-point for getting the market watchlist for the logged in user.  The value for the user_id path parameter should match the user_id value returned on the response for the last login request (POST /log_in).

### Example

* Api Key Authentication (cookie):
```python
import time
import openapi_client
from openapi_client.api import user_api
from openapi_client.model.user_get_watchlist_response import UserGetWatchlistResponse
from pprint import pprint
# Defining the host is optional and defaults to https://trading-api.kalshi.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://trading-api.kalshi.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | Should be filled with your user_id provided on log_in

    # example passing only required values which don't have defaults set
    try:
        # UserGetWatchlist
        api_response = api_instance.user_get_watchlist(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->user_get_watchlist: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Should be filled with your user_id provided on log_in |

### Return type

[**UserGetWatchlistResponse**](UserGetWatchlistResponse.md)

### Authorization

[cookie](../README.md#cookie)

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

# **user_order_cancel**
> UserOrderDecreaseResponse user_order_cancel(user_id, order_id)

UserOrderCancel

End-point for canceling orders.  The value for the user_id path parameter should match the user_id value returned on the response for the last login request (POST /log_in). The value for the order_id should match the id field of the order you want to decrease. Commonly delete end-points return 204 status with no body content on success. But we can't completely delete the order, as it may be partially filled already. So what the delete end-point does is just reducing the order completely zeroing the remaining resting contracts on it. The zeroed order is returned on the response payload, as a form of validation for the client.

### Example

* Api Key Authentication (cookie):
```python
import time
import openapi_client
from openapi_client.api import user_api
from openapi_client.model.user_order_decrease_response import UserOrderDecreaseResponse
from pprint import pprint
# Defining the host is optional and defaults to https://trading-api.kalshi.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://trading-api.kalshi.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | This parameter should be filled with your user_id provided on log_in
    order_id = "order_id_example" # str | This order_id should be filled with the id of the order to be decrease

    # example passing only required values which don't have defaults set
    try:
        # UserOrderCancel
        api_response = api_instance.user_order_cancel(user_id, order_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->user_order_cancel: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| This parameter should be filled with your user_id provided on log_in |
 **order_id** | **str**| This order_id should be filled with the id of the order to be decrease |

### Return type

[**UserOrderDecreaseResponse**](UserOrderDecreaseResponse.md)

### Authorization

[cookie](../README.md#cookie)

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
**503** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_order_create**
> UserOrderCreateResponse user_order_create(user_id)

UserOrderCreate

End-point for submitting orders in a market.  The value for the user_id path parameter should match the user_id value returned on the response for the last login request (POST /log_in).

### Example

* Api Key Authentication (cookie):
```python
import time
import openapi_client
from openapi_client.api import user_api
from openapi_client.model.user_order_create_request import UserOrderCreateRequest
from openapi_client.model.user_order_create_response import UserOrderCreateResponse
from pprint import pprint
# Defining the host is optional and defaults to https://trading-api.kalshi.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://trading-api.kalshi.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | This parameter should be filled with your user_id provided on log_in
    user_order_create_request = UserOrderCreateRequest(
        count=1,
        expiration_unix_ts=1,
        market_id="market_id_example",
        max_cost_cents=1,
        price=1,
        sell_position_capped=True,
        side="side_example",
    ) # UserOrderCreateRequest | Order create input data (optional)

    # example passing only required values which don't have defaults set
    try:
        # UserOrderCreate
        api_response = api_instance.user_order_create(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->user_order_create: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # UserOrderCreate
        api_response = api_instance.user_order_create(user_id, user_order_create_request=user_order_create_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->user_order_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| This parameter should be filled with your user_id provided on log_in |
 **user_order_create_request** | [**UserOrderCreateRequest**](UserOrderCreateRequest.md)| Order create input data | [optional]

### Return type

[**UserOrderCreateResponse**](UserOrderCreateResponse.md)

### Authorization

[cookie](../README.md#cookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**401** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**403** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**500** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**503** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_order_decrease**
> UserOrderDecreaseResponse user_order_decrease(user_id, order_id)

UserOrderDecrease

End-point for decreasing the number of contracts on orders. This is the only kind of edit we support on orders.  The value for the user_id path parameter should match the user_id value returned on the response for the last login request (POST /log_in).  The value for the order_id should match the id field of the order you want to decrease.

### Example

* Api Key Authentication (cookie):
```python
import time
import openapi_client
from openapi_client.api import user_api
from openapi_client.model.user_order_decrease_request import UserOrderDecreaseRequest
from openapi_client.model.user_order_decrease_response import UserOrderDecreaseResponse
from pprint import pprint
# Defining the host is optional and defaults to https://trading-api.kalshi.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://trading-api.kalshi.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | This parameter should be filled with your user_id provided on log_in
    order_id = "order_id_example" # str | This order_id should be filled with the id of the order to be decrease
    user_order_decrease_request = UserOrderDecreaseRequest(
        count=1,
    ) # UserOrderDecreaseRequest | Order data (optional)

    # example passing only required values which don't have defaults set
    try:
        # UserOrderDecrease
        api_response = api_instance.user_order_decrease(user_id, order_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->user_order_decrease: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # UserOrderDecrease
        api_response = api_instance.user_order_decrease(user_id, order_id, user_order_decrease_request=user_order_decrease_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->user_order_decrease: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| This parameter should be filled with your user_id provided on log_in |
 **order_id** | **str**| This order_id should be filled with the id of the order to be decrease |
 **user_order_decrease_request** | [**UserOrderDecreaseRequest**](UserOrderDecreaseRequest.md)| Order data | [optional]

### Return type

[**UserOrderDecreaseResponse**](UserOrderDecreaseResponse.md)

### Authorization

[cookie](../README.md#cookie)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**401** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**403** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**500** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**503** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_orders_get**
> UserOrdersGetResponse user_orders_get(user_id)

UserOrdersGet

End-point for getting all orders for the logged in user.  The value for the user_id path parameter should match the user_id value returned on the response for the last login request (POST /log_in).

### Example

* Api Key Authentication (cookie):
```python
import time
import openapi_client
from openapi_client.api import user_api
from openapi_client.model.user_orders_get_response import UserOrdersGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://trading-api.kalshi.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://trading-api.kalshi.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | This parameter should be filled with your user_id provided on log_in
    market_id = "market_id_example" # str | Restricts the response to orders in a single market (optional)
    is_yes = True # bool | Restricts the response to orders in a single direction (yes or no) (optional)
    min_price = 1 # int | Restricts the response to orders within a minimum price (optional)
    max_price = 1 # int | Restricts the response to orders within a maximum price (optional)
    min_place_count = 1 # int | Restricts the response to orders within a minimum place count (optional)
    max_place_count = 1 # int | Restricts the response to orders within a maximum place count (optional)
    min_initial_count = 1 # int | Restricts the response to orders within a minimum initial count (optional)
    max_initial_count = 1 # int | Restricts the response to orders within a maximum initial count (optional)
    min_remaining_count = 1 # int | Restricts the response to orders within a minimum remaining resting contracts count (optional)
    max_remaining_count = 1 # int | Restricts the response to orders within a maximum remaining resting contracts count (optional)
    min_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Restricts the response to orders after a timestamp (optional)
    max_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Restricts the response to orders before a timestamp (optional)
    get_queue_position = True # bool | If true, gets the queue placement for every resting order returned (optional)
    status = "status_example" # str | Restricts the response to orders that have a certain status: resting, canceled, or executed (optional)
    page_size = 1 # int | Parameter to specify the number of results per page (optional)
    page_number = 1 # int | Parameter to specify which page of the results should be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # UserOrdersGet
        api_response = api_instance.user_orders_get(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->user_orders_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # UserOrdersGet
        api_response = api_instance.user_orders_get(user_id, market_id=market_id, is_yes=is_yes, min_price=min_price, max_price=max_price, min_place_count=min_place_count, max_place_count=max_place_count, min_initial_count=min_initial_count, max_initial_count=max_initial_count, min_remaining_count=min_remaining_count, max_remaining_count=max_remaining_count, min_date=min_date, max_date=max_date, get_queue_position=get_queue_position, status=status, page_size=page_size, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->user_orders_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| This parameter should be filled with your user_id provided on log_in |
 **market_id** | **str**| Restricts the response to orders in a single market | [optional]
 **is_yes** | **bool**| Restricts the response to orders in a single direction (yes or no) | [optional]
 **min_price** | **int**| Restricts the response to orders within a minimum price | [optional]
 **max_price** | **int**| Restricts the response to orders within a maximum price | [optional]
 **min_place_count** | **int**| Restricts the response to orders within a minimum place count | [optional]
 **max_place_count** | **int**| Restricts the response to orders within a maximum place count | [optional]
 **min_initial_count** | **int**| Restricts the response to orders within a minimum initial count | [optional]
 **max_initial_count** | **int**| Restricts the response to orders within a maximum initial count | [optional]
 **min_remaining_count** | **int**| Restricts the response to orders within a minimum remaining resting contracts count | [optional]
 **max_remaining_count** | **int**| Restricts the response to orders within a maximum remaining resting contracts count | [optional]
 **min_date** | **datetime**| Restricts the response to orders after a timestamp | [optional]
 **max_date** | **datetime**| Restricts the response to orders before a timestamp | [optional]
 **get_queue_position** | **bool**| If true, gets the queue placement for every resting order returned | [optional]
 **status** | **str**| Restricts the response to orders that have a certain status: resting, canceled, or executed | [optional]
 **page_size** | **int**| Parameter to specify the number of results per page | [optional]
 **page_number** | **int**| Parameter to specify which page of the results should be retrieved | [optional]

### Return type

[**UserOrdersGetResponse**](UserOrdersGetResponse.md)

### Authorization

[cookie](../README.md#cookie)

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

# **user_remove_watchlist**
> user_remove_watchlist(user_id, market_id)

UserRemoveWatchlist

End-point for removing a market from the logged in user's watchlist.  The value for the user_id path parameter should match the user_id value returned on the response for the last login request (POST /log_in).  The value for the market_id path parameter should match the id value of the market to be added.

### Example

* Api Key Authentication (cookie):
```python
import time
import openapi_client
from openapi_client.api import user_api
from pprint import pprint
# Defining the host is optional and defaults to https://trading-api.kalshi.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://trading-api.kalshi.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | Should be filled with your user_id provided on log_in
    market_id = "market_id_example" # str | Should be filled with the id of the target market

    # example passing only required values which don't have defaults set
    try:
        # UserRemoveWatchlist
        api_instance.user_remove_watchlist(user_id, market_id)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->user_remove_watchlist: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Should be filled with your user_id provided on log_in |
 **market_id** | **str**| Should be filled with the id of the target market |

### Return type

void (empty response body)

### Authorization

[cookie](../README.md#cookie)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No fields are returned on the response. |  -  |
**400** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**401** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**403** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**404** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**500** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**503** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_trades_get**
> UserTradesGetResponse user_trades_get(user_id)

UserTradesGet

End-point for getting all trades for the logged in user.  The value for the user_id path parameter should match the user_id value returned on the response for the last login request (POST /log_in).

### Example

* Api Key Authentication (cookie):
```python
import time
import openapi_client
from openapi_client.api import user_api
from openapi_client.model.user_trades_get_response import UserTradesGetResponse
from pprint import pprint
# Defining the host is optional and defaults to https://trading-api.kalshi.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://trading-api.kalshi.com/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: cookie
configuration.api_key['cookie'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookie'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = user_api.UserApi(api_client)
    user_id = "user_id_example" # str | This parameter should be filled with your user_id provided on log_in
    market_id = "market_id_example" # str | Restricts the response to trades in a specific market. (optional)
    order_id = "order_id_example" # str | Restricts the response to trades related to a specific order. (optional)
    min_price = 1 # int | Restricts the response to trades within a minimum price. (optional)
    max_price = 1 # int | Restricts the response to trades within a maximum price. (optional)
    min_count = 1 # int | Restricts the response to trades within a minimum contracts count. (optional)
    max_count = 1 # int | Restricts the response to trades within a maximum contracts count. (optional)
    min_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Restricts the response to trades after a timestamp. (optional)
    max_date = dateutil_parser('1970-01-01T00:00:00.00Z') # datetime | Restricts the response to trades before a timestamp. (optional)
    page_size = 1 # int | Parameter to specify the number of results per page (optional)
    page_number = 1 # int | Parameter to specify which page of the results should be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # UserTradesGet
        api_response = api_instance.user_trades_get(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->user_trades_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # UserTradesGet
        api_response = api_instance.user_trades_get(user_id, market_id=market_id, order_id=order_id, min_price=min_price, max_price=max_price, min_count=min_count, max_count=max_count, min_date=min_date, max_date=max_date, page_size=page_size, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling UserApi->user_trades_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| This parameter should be filled with your user_id provided on log_in |
 **market_id** | **str**| Restricts the response to trades in a specific market. | [optional]
 **order_id** | **str**| Restricts the response to trades related to a specific order. | [optional]
 **min_price** | **int**| Restricts the response to trades within a minimum price. | [optional]
 **max_price** | **int**| Restricts the response to trades within a maximum price. | [optional]
 **min_count** | **int**| Restricts the response to trades within a minimum contracts count. | [optional]
 **max_count** | **int**| Restricts the response to trades within a maximum contracts count. | [optional]
 **min_date** | **datetime**| Restricts the response to trades after a timestamp. | [optional]
 **max_date** | **datetime**| Restricts the response to trades before a timestamp. | [optional]
 **page_size** | **int**| Parameter to specify the number of results per page | [optional]
 **page_number** | **int**| Parameter to specify which page of the results should be retrieved | [optional]

### Return type

[**UserTradesGetResponse**](UserTradesGetResponse.md)

### Authorization

[cookie](../README.md#cookie)

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

