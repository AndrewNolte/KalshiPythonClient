# openapi_client.AccountApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_subscription**](AccountApi.md#change_subscription) | **PUT** /users/{user_id}/subscribe | ChangeSubscription
[**notification_mark_read**](AccountApi.md#notification_mark_read) | **PUT** /users/{user_id}/notifications/{notification_id}/read | NotificationMarkRead
[**user_get_account_history**](AccountApi.md#user_get_account_history) | **GET** /users/{user_id}/account/history | UserGetAccountHistory
[**user_get_notifications**](AccountApi.md#user_get_notifications) | **GET** /users/{user_id}/notifications | UserGetNotifications


# **change_subscription**
> change_subscription(user_id)

ChangeSubscription

End-point for changing e-mail subscription mode for the current user.  This end-point is very useful for users that have a large volume of orders and don't want to be email notified whenever an order is submitted / edited / canceled or matches.  This is specially useful for Market Makers.  The value for the user_id path parameter should match the user_id value returned on the response for the last login request (POST /log_in).

### Example

* Api Key Authentication (cookie):
```python
import time
import openapi_client
from openapi_client.api import account_api
from openapi_client.model.change_subscription_request import ChangeSubscriptionRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/v1"
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
    api_instance = account_api.AccountApi(api_client)
    user_id = "user_id_example" # str | Should be filled with your user_id provided on log_in
    change_subscription_request = ChangeSubscriptionRequest(
        subscription_level="subscription_level_example",
    ) # ChangeSubscriptionRequest | Change subscription data (optional)

    # example passing only required values which don't have defaults set
    try:
        # ChangeSubscription
        api_instance.change_subscription(user_id)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountApi->change_subscription: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ChangeSubscription
        api_instance.change_subscription(user_id, change_subscription_request=change_subscription_request)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountApi->change_subscription: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Should be filled with your user_id provided on log_in |
 **change_subscription_request** | [**ChangeSubscriptionRequest**](ChangeSubscriptionRequest.md)| Change subscription data | [optional]

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

# **notification_mark_read**
> notification_mark_read(user_id, notification_id)

NotificationMarkRead

End-point for marking a notification as read.  The value for the user_id path parameter should match the user_id value returned on the response for the last login request (POST /log_in).  The value for the notification_id path parameter should match the notification_id value of the notification to be marked as read.

### Example

* Api Key Authentication (cookie):
```python
import time
import openapi_client
from openapi_client.api import account_api
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/v1"
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
    api_instance = account_api.AccountApi(api_client)
    user_id = "user_id_example" # str | user_id should be filled with your user_id provided on log_in
    notification_id = "notification_id_example" # str | notification_id should be filled with the id of the notification to be mark as read

    # example passing only required values which don't have defaults set
    try:
        # NotificationMarkRead
        api_instance.notification_mark_read(user_id, notification_id)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountApi->notification_mark_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| user_id should be filled with your user_id provided on log_in |
 **notification_id** | **str**| notification_id should be filled with the id of the notification to be mark as read |

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
**500** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get_account_history**
> UserGetAccountHistoryResponse user_get_account_history(user_id)

UserGetAccountHistory

End-point for getting the logged in user's important past actions and events related to the user's positions.  This contains entries for user's explicit actions but also for market events.  There will be entries for:  submitting, editing / canceling orders requesting deposits and withdrawals trade execution (order matching) market settlements on markets where you have a position  The value for the user_id path parameter should match the user_id value returned on the response for the last login request (POST /log_in).

### Example

* Api Key Authentication (cookie):
```python
import time
import openapi_client
from openapi_client.api import account_api
from openapi_client.model.user_get_account_history_response import UserGetAccountHistoryResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/v1"
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
    api_instance = account_api.AccountApi(api_client)
    user_id = "user_id_example" # str | This parameter should be filled with your user_id provided on log_in
    should_return_deposits = True # bool | If true the response should include deposit entries (optional)
    should_return_withdrawals = True # bool | If true the response should include withdrawal entries (optional)
    should_return_orders = True # bool | If true the response should include order entries (optional)
    should_return_settlements = True # bool | If true the response should include settlement entries (optional)
    should_return_trades = True # bool | If true the response should include trade entries (optional)
    limit = 1 # int | Restricts the response to a return the first \"limit\" amount of acct history items (optional)

    # example passing only required values which don't have defaults set
    try:
        # UserGetAccountHistory
        api_response = api_instance.user_get_account_history(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountApi->user_get_account_history: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # UserGetAccountHistory
        api_response = api_instance.user_get_account_history(user_id, should_return_deposits=should_return_deposits, should_return_withdrawals=should_return_withdrawals, should_return_orders=should_return_orders, should_return_settlements=should_return_settlements, should_return_trades=should_return_trades, limit=limit)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountApi->user_get_account_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| This parameter should be filled with your user_id provided on log_in |
 **should_return_deposits** | **bool**| If true the response should include deposit entries | [optional]
 **should_return_withdrawals** | **bool**| If true the response should include withdrawal entries | [optional]
 **should_return_orders** | **bool**| If true the response should include order entries | [optional]
 **should_return_settlements** | **bool**| If true the response should include settlement entries | [optional]
 **should_return_trades** | **bool**| If true the response should include trade entries | [optional]
 **limit** | **int**| Restricts the response to a return the first \&quot;limit\&quot; amount of acct history items | [optional]

### Return type

[**UserGetAccountHistoryResponse**](UserGetAccountHistoryResponse.md)

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

# **user_get_notifications**
> UserGetNotificationsResponse user_get_notifications(user_id)

UserGetNotifications

End-point for getting notifications for the current logged in user.  The value for the user_id path parameter should match the user_id value returned on the response for the last login request (POST /log_in).

### Example

* Api Key Authentication (cookie):
```python
import time
import openapi_client
from openapi_client.api import account_api
from openapi_client.model.user_get_notifications_response import UserGetNotificationsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/v1"
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
    api_instance = account_api.AccountApi(api_client)
    user_id = "user_id_example" # str | This parameter should be filled with your user_id provided on log_in
    page_size = 1 # int | Optional parameter to specify the number of results per page (optional)
    page_number = 1 # int | Optional parameter to specify which page of the results should be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # UserGetNotifications
        api_response = api_instance.user_get_notifications(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountApi->user_get_notifications: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # UserGetNotifications
        api_response = api_instance.user_get_notifications(user_id, page_size=page_size, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AccountApi->user_get_notifications: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| This parameter should be filled with your user_id provided on log_in |
 **page_size** | **int**| Optional parameter to specify the number of results per page | [optional]
 **page_number** | **int**| Optional parameter to specify which page of the results should be retrieved | [optional]

### Return type

[**UserGetNotificationsResponse**](UserGetNotificationsResponse.md)

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

