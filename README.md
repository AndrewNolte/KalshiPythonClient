# kalshi
This documentation describes Kalshi's rest API for market makers

# Authentication

<!-- ReDoc-Inject: <security-definitions> -->

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import kalshi
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import kalshi
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import kalshi
from pprint import pprint
from kalshi.api import account_api
from kalshi.model.change_subscription_request import ChangeSubscriptionRequest
from kalshi.model.get_notification_preferences_response import GetNotificationPreferencesResponse
from kalshi.model.user_get_account_history_response import UserGetAccountHistoryResponse
from kalshi.model.user_get_notifications_response import UserGetNotificationsResponse
# Defining the host is optional and defaults to https://trading-api.kalshi.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kalshi.Configuration(
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
with kalshi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = account_api.AccountApi(api_client)
    user_id = "user_id_example" # str | Should be filled with your user_id provided on log_in
change_subscription_request = ChangeSubscriptionRequest(
        subscription_level="subscription_level_example",
    ) # ChangeSubscriptionRequest | Change subscription data (optional)

    try:
        # ChangeSubscription
        api_instance.change_subscription(user_id, change_subscription_request=change_subscription_request)
    except kalshi.ApiException as e:
        print("Exception when calling AccountApi->change_subscription: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://trading-api.kalshi.com/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountApi* | [**change_subscription**](docs/AccountApi.md#change_subscription) | **PUT** /users/{user_id}/subscribe | ChangeSubscription
*AccountApi* | [**get_notification_preferences**](docs/AccountApi.md#get_notification_preferences) | **GET** /users/{user_id}/notifications/preferences | GetNotificationPreferences
*AccountApi* | [**notification_mark_read**](docs/AccountApi.md#notification_mark_read) | **PUT** /users/{user_id}/notifications/{notification_id}/read | NotificationMarkRead
*AccountApi* | [**user_get_account_history**](docs/AccountApi.md#user_get_account_history) | **GET** /users/{user_id}/account/history | UserGetAccountHistory
*AccountApi* | [**user_get_notifications**](docs/AccountApi.md#user_get_notifications) | **GET** /users/{user_id}/notifications | UserGetNotifications
*AuthApi* | [**login**](docs/AuthApi.md#login) | **POST** /log_in | Login
*AuthApi* | [**logout**](docs/AuthApi.md#logout) | **POST** /log_out | Logout
*AuthApi* | [**reset_password**](docs/AuthApi.md#reset_password) | **POST** /passwords/reset | ResetPassword
*AuthApi* | [**reset_password_confirm**](docs/AuthApi.md#reset_password_confirm) | **PUT** /passwords/reset/{code}/confirm | ResetPasswordConfirm
*DefaultApi* | [**get_trades**](docs/DefaultApi.md#get_trades) | **GET** /trades | GetTrades
*ExchangeApi* | [**get_exchange_status**](docs/ExchangeApi.md#get_exchange_status) | **GET** /exchange/status | 
*MarketApi* | [**get_market**](docs/MarketApi.md#get_market) | **GET** /markets/{market_id} | GetMarket
*MarketApi* | [**get_market_by_ticker**](docs/MarketApi.md#get_market_by_ticker) | **GET** /markets_by_ticker/{ticker_name} | GetMarketByTicker
*MarketApi* | [**get_market_by_ticker_cached**](docs/MarketApi.md#get_market_by_ticker_cached) | **GET** /cached/markets_by_ticker/{ticker_name} | GetMarketByTickerCached
*MarketApi* | [**get_market_cached**](docs/MarketApi.md#get_market_cached) | **GET** /cached/markets/{market_id} | GetMarketCached
*MarketApi* | [**get_market_history**](docs/MarketApi.md#get_market_history) | **GET** /markets/{market_id}/stats_history | GetMarketHistory
*MarketApi* | [**get_market_history_cached**](docs/MarketApi.md#get_market_history_cached) | **GET** /cached/markets/{market_id}/stats_history | GetMarketHistoryCached
*MarketApi* | [**get_market_order_book_cached**](docs/MarketApi.md#get_market_order_book_cached) | **GET** /markets/{market_id}/order_book | GetMarketOrderBookCached
*MarketApi* | [**get_markets**](docs/MarketApi.md#get_markets) | **GET** /markets | GetMarkets
*MarketApi* | [**get_markets_cached**](docs/MarketApi.md#get_markets_cached) | **GET** /cached/markets | GetMarketsCached
*PortfolioApi* | [**user_get_portfolio_history**](docs/PortfolioApi.md#user_get_portfolio_history) | **GET** /users/{user_id}/portfolio/history | UserGetPortfolioHistory
*RangedMarketApi* | [**get_ranged_market**](docs/RangedMarketApi.md#get_ranged_market) | **GET** /ranged_markets/{ranged_market_id} | GetRangedMarket
*RangedMarketsApi* | [**get_ranged_market_by_ticker**](docs/RangedMarketsApi.md#get_ranged_market_by_ticker) | **GET** /ranged_markets_by_ticker/{ticker} | GetRangedMarketByTicker
*UserApi* | [**user_add_watchlist**](docs/UserApi.md#user_add_watchlist) | **PUT** /users/{user_id}/watchlist/{market_id} | UserAddWatchlist
*UserApi* | [**user_change_password**](docs/UserApi.md#user_change_password) | **PUT** /users/{user_id}/password | UserChangePassword
*UserApi* | [**user_get_balance**](docs/UserApi.md#user_get_balance) | **GET** /users/{user_id}/balance | UserGetBalance
*UserApi* | [**user_get_market_position**](docs/UserApi.md#user_get_market_position) | **GET** /users/{user_id}/positions/{market_id} | UserGetMarketPosition
*UserApi* | [**user_get_market_positions**](docs/UserApi.md#user_get_market_positions) | **GET** /users/{user_id}/positions | UserGetMarketPositions
*UserApi* | [**user_get_profile**](docs/UserApi.md#user_get_profile) | **GET** /users/{user_id} | UserGetProfile
*UserApi* | [**user_get_watchlist**](docs/UserApi.md#user_get_watchlist) | **GET** /users/{user_id}/watchlist | UserGetWatchlist
*UserApi* | [**user_order_cancel**](docs/UserApi.md#user_order_cancel) | **DELETE** /users/{user_id}/orders/{order_id} | UserOrderCancel
*UserApi* | [**user_order_create**](docs/UserApi.md#user_order_create) | **POST** /users/{user_id}/orders | UserOrderCreate
*UserApi* | [**user_order_decrease**](docs/UserApi.md#user_order_decrease) | **POST** /users/{user_id}/orders/{order_id}/decrease | UserOrderDecrease
*UserApi* | [**user_orders_get**](docs/UserApi.md#user_orders_get) | **GET** /users/{user_id}/orders | UserOrdersGet
*UserApi* | [**user_remove_watchlist**](docs/UserApi.md#user_remove_watchlist) | **DELETE** /users/{user_id}/watchlist/{market_id} | UserRemoveWatchlist
*UserApi* | [**user_trades_get**](docs/UserApi.md#user_trades_get) | **GET** /users/{user_id}/trades | UserTradesGet


## Documentation For Models

 - [AccountHistoryEntry](docs/AccountHistoryEntry.md)
 - [AccountHistoryEntryData](docs/AccountHistoryEntryData.md)
 - [BankAccountDetails](docs/BankAccountDetails.md)
 - [ChangeSubscriptionRequest](docs/ChangeSubscriptionRequest.md)
 - [ConfirmPasswordResetRequest](docs/ConfirmPasswordResetRequest.md)
 - [CreateUserRequest](docs/CreateUserRequest.md)
 - [CreateUserResponse](docs/CreateUserResponse.md)
 - [Deposit](docs/Deposit.md)
 - [DepositHistory](docs/DepositHistory.md)
 - [GetMarketHistoryResponse](docs/GetMarketHistoryResponse.md)
 - [GetMarketOrderBookResponse](docs/GetMarketOrderBookResponse.md)
 - [GetNotificationPreferencesResponse](docs/GetNotificationPreferencesResponse.md)
 - [GetRangedMarketByTickerResponse](docs/GetRangedMarketByTickerResponse.md)
 - [GetRangedMarketResponse](docs/GetRangedMarketResponse.md)
 - [GetRangedMarketsResponse](docs/GetRangedMarketsResponse.md)
 - [GetUserDepositsResponse](docs/GetUserDepositsResponse.md)
 - [GetUserWithdrawalsResponse](docs/GetUserWithdrawalsResponse.md)
 - [LoginRequest](docs/LoginRequest.md)
 - [LoginResponse](docs/LoginResponse.md)
 - [Market](docs/Market.md)
 - [MarketPosition](docs/MarketPosition.md)
 - [MarketStatsPoint](docs/MarketStatsPoint.md)
 - [Notification](docs/Notification.md)
 - [NotificationList](docs/NotificationList.md)
 - [Order](docs/Order.md)
 - [OrderBook](docs/OrderBook.md)
 - [OrderHistory](docs/OrderHistory.md)
 - [OrderList](docs/OrderList.md)
 - [PortfolioMeasurement](docs/PortfolioMeasurement.md)
 - [PriceLevel](docs/PriceLevel.md)
 - [PublicTrade](docs/PublicTrade.md)
 - [PublicTradeList](docs/PublicTradeList.md)
 - [RangedMarket](docs/RangedMarket.md)
 - [ResetPasswordRequest](docs/ResetPasswordRequest.md)
 - [SettlementHistory](docs/SettlementHistory.md)
 - [SettlementSource](docs/SettlementSource.md)
 - [SubscriptionPreference](docs/SubscriptionPreference.md)
 - [TradeHistory](docs/TradeHistory.md)
 - [TradesGetResponse](docs/TradesGetResponse.md)
 - [User](docs/User.md)
 - [UserChangePasswordRequest](docs/UserChangePasswordRequest.md)
 - [UserDepositRequest](docs/UserDepositRequest.md)
 - [UserDepositResponse](docs/UserDepositResponse.md)
 - [UserGetAccountHistoryResponse](docs/UserGetAccountHistoryResponse.md)
 - [UserGetBalanceResponse](docs/UserGetBalanceResponse.md)
 - [UserGetMarketPositionResponse](docs/UserGetMarketPositionResponse.md)
 - [UserGetMarketPositionsResponse](docs/UserGetMarketPositionsResponse.md)
 - [UserGetMarketResponse](docs/UserGetMarketResponse.md)
 - [UserGetMarketsResponse](docs/UserGetMarketsResponse.md)
 - [UserGetNotificationsResponse](docs/UserGetNotificationsResponse.md)
 - [UserGetPortfolioHistoryRequest](docs/UserGetPortfolioHistoryRequest.md)
 - [UserGetPortfolioHistoryResponse](docs/UserGetPortfolioHistoryResponse.md)
 - [UserGetPortfolioValueResponse](docs/UserGetPortfolioValueResponse.md)
 - [UserGetProfileResponse](docs/UserGetProfileResponse.md)
 - [UserGetWatchlistResponse](docs/UserGetWatchlistResponse.md)
 - [UserListLedgerxBankAccountsResponse](docs/UserListLedgerxBankAccountsResponse.md)
 - [UserOrderCreateRequest](docs/UserOrderCreateRequest.md)
 - [UserOrderCreateResponse](docs/UserOrderCreateResponse.md)
 - [UserOrderDecreaseRequest](docs/UserOrderDecreaseRequest.md)
 - [UserOrderDecreaseResponse](docs/UserOrderDecreaseResponse.md)
 - [UserOrdersGetResponse](docs/UserOrdersGetResponse.md)
 - [UserTrade](docs/UserTrade.md)
 - [UserTradeList](docs/UserTradeList.md)
 - [UserTradesGetResponse](docs/UserTradesGetResponse.md)
 - [UserUpdateProfileRequest](docs/UserUpdateProfileRequest.md)
 - [UserWithdrawalRequest](docs/UserWithdrawalRequest.md)
 - [UserWithdrawalResponse](docs/UserWithdrawalResponse.md)
 - [Watchlist](docs/Watchlist.md)
 - [Withdrawal](docs/Withdrawal.md)
 - [WithdrawalHistory](docs/WithdrawalHistory.md)


## Documentation For Authorization


## cookie

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author




## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in kalshi.apis and kalshi.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from kalshi.api.default_api import DefaultApi`
- `from kalshi.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import kalshi
from kalshi.apis import *
from kalshi.models import *
```

