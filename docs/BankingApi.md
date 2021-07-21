# openapi_client.BankingApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_deposits**](BankingApi.md#get_user_deposits) | **GET** /users/{user_id}/deposits | GetUserDeposits
[**get_user_withdrawals**](BankingApi.md#get_user_withdrawals) | **GET** /users/{user_id}/withdrawals | GetUserWithdrawals
[**user_create_plaid_link_token**](BankingApi.md#user_create_plaid_link_token) | **POST** /users/{user_id}/plaid/link_token | UserCreatePlaidLinkToken
[**user_link_bank_accounts**](BankingApi.md#user_link_bank_accounts) | **POST** /users/{user_id}/banks/linked_accounts | UserLinkBankAccounts
[**user_list_ledgerx_bank_accounts**](BankingApi.md#user_list_ledgerx_bank_accounts) | **GET** /users/{user_id}/banks/linked_accounts | UserListLedgerxBankAccounts
[**user_request_deposit**](BankingApi.md#user_request_deposit) | **POST** /users/{user_id}/deposits | UserRequestDeposit
[**user_request_withdrawal**](BankingApi.md#user_request_withdrawal) | **POST** /users/{user_id}/withdrawals | UserRequestWithdrawal


# **get_user_deposits**
> GetUserDepositsResponse get_user_deposits(user_id)

GetUserDeposits

End-point for getting all deposits for the logged in user.  The value for the user_id path parameter should match the user_id value returned on the response for the last login request (POST /log_in).

### Example

* Api Key Authentication (cookie):
```python
import time
import openapi_client
from openapi_client.api import banking_api
from openapi_client.model.get_user_deposits_response import GetUserDepositsResponse
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
    api_instance = banking_api.BankingApi(api_client)
    user_id = "user_id_example" # str | This parameter should be filled with your user_id provided on log_in
    page_size = 1 # int | Number of deposits in each page. (optional)
    page_number = 1 # int | Number of the page to be retrieved. (optional)

    # example passing only required values which don't have defaults set
    try:
        # GetUserDeposits
        api_response = api_instance.get_user_deposits(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BankingApi->get_user_deposits: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GetUserDeposits
        api_response = api_instance.get_user_deposits(user_id, page_size=page_size, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BankingApi->get_user_deposits: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| This parameter should be filled with your user_id provided on log_in |
 **page_size** | **int**| Number of deposits in each page. | [optional]
 **page_number** | **int**| Number of the page to be retrieved. | [optional]

### Return type

[**GetUserDepositsResponse**](GetUserDepositsResponse.md)

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

# **get_user_withdrawals**
> GetUserWithdrawalsResponse get_user_withdrawals(user_id)

GetUserWithdrawals

End-point for getting all withdrawals for the logged in user.  The value for the user_id path parameter should match the user_id value returned on the response for the last login request (POST /log_in).

### Example

* Api Key Authentication (cookie):
```python
import time
import openapi_client
from openapi_client.api import banking_api
from openapi_client.model.get_user_withdrawals_response import GetUserWithdrawalsResponse
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
    api_instance = banking_api.BankingApi(api_client)
    user_id = "user_id_example" # str | This parameter should be filled with your user_id provided on log_in
    page_size = 1 # int | Number of withdrawals in each page. (optional)
    page_number = 1 # int | Number of the page to be retrieved. (optional)

    # example passing only required values which don't have defaults set
    try:
        # GetUserWithdrawals
        api_response = api_instance.get_user_withdrawals(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BankingApi->get_user_withdrawals: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # GetUserWithdrawals
        api_response = api_instance.get_user_withdrawals(user_id, page_size=page_size, page_number=page_number)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BankingApi->get_user_withdrawals: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| This parameter should be filled with your user_id provided on log_in |
 **page_size** | **int**| Number of withdrawals in each page. | [optional]
 **page_number** | **int**| Number of the page to be retrieved. | [optional]

### Return type

[**GetUserWithdrawalsResponse**](GetUserWithdrawalsResponse.md)

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

# **user_create_plaid_link_token**
> UserCreatePlaidLinkTokenResponse user_create_plaid_link_token(user_id)

UserCreatePlaidLinkToken

End-point for creating a link token. This is required to be able to connect bank accounts via Plaid.  Look at plaid docs (https://plaid.com/docs/api/tokens/#linktokencreate) for more information on the token and how plaid works.  The value for the user_id path parameter should match the user_id value returned on the response for the last login request (POST /log_in).

### Example

* Api Key Authentication (cookie):
```python
import time
import openapi_client
from openapi_client.api import banking_api
from openapi_client.model.user_create_plaid_link_token_response import UserCreatePlaidLinkTokenResponse
from openapi_client.model.user_create_plaid_link_token_request import UserCreatePlaidLinkTokenRequest
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
    api_instance = banking_api.BankingApi(api_client)
    user_id = "user_id_example" # str | This parameter should be filled with your user_id provided on log_in
    user_create_plaid_link_token_request = UserCreatePlaidLinkTokenRequest(
        bank_account_id="bank_account_id_example",
    ) # UserCreatePlaidLinkTokenRequest | Input for getting a token. If bank_account_id is filled it will generate a re-connection token. (optional)

    # example passing only required values which don't have defaults set
    try:
        # UserCreatePlaidLinkToken
        api_response = api_instance.user_create_plaid_link_token(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BankingApi->user_create_plaid_link_token: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # UserCreatePlaidLinkToken
        api_response = api_instance.user_create_plaid_link_token(user_id, user_create_plaid_link_token_request=user_create_plaid_link_token_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BankingApi->user_create_plaid_link_token: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| This parameter should be filled with your user_id provided on log_in |
 **user_create_plaid_link_token_request** | [**UserCreatePlaidLinkTokenRequest**](UserCreatePlaidLinkTokenRequest.md)| Input for getting a token. If bank_account_id is filled it will generate a re-connection token. | [optional]

### Return type

[**UserCreatePlaidLinkTokenResponse**](UserCreatePlaidLinkTokenResponse.md)

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

# **user_link_bank_accounts**
> user_link_bank_accounts(user_id)

UserLinkBankAccounts

End-point for submitting to finish bank account linking.  This end-point sends the bank accounts connected by the user in the front-end to our clearing house.  The value for the user_id path parameter should match the user_id value returned on the response for the last login request (POST /log_in).

### Example

* Api Key Authentication (cookie):
```python
import time
import openapi_client
from openapi_client.api import banking_api
from openapi_client.model.user_link_bank_accounts_request import UserLinkBankAccountsRequest
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
    api_instance = banking_api.BankingApi(api_client)
    user_id = "user_id_example" # str | This parameter should be filled with your user_id provided on log_in
    user_link_bank_accounts_request = UserLinkBankAccountsRequest(
        accounts=[
            "accounts_example",
        ],
        link_token="link_token_example",
        public_token="public_token_example",
    ) # UserLinkBankAccountsRequest | Input for finishing the bank accounts link. (optional)

    # example passing only required values which don't have defaults set
    try:
        # UserLinkBankAccounts
        api_instance.user_link_bank_accounts(user_id)
    except openapi_client.ApiException as e:
        print("Exception when calling BankingApi->user_link_bank_accounts: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # UserLinkBankAccounts
        api_instance.user_link_bank_accounts(user_id, user_link_bank_accounts_request=user_link_bank_accounts_request)
    except openapi_client.ApiException as e:
        print("Exception when calling BankingApi->user_link_bank_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| This parameter should be filled with your user_id provided on log_in |
 **user_link_bank_accounts_request** | [**UserLinkBankAccountsRequest**](UserLinkBankAccountsRequest.md)| Input for finishing the bank accounts link. | [optional]

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
**201** | No fields are returned on the response. |  -  |
**400** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**401** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**403** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**500** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**503** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_list_ledgerx_bank_accounts**
> UserListLedgerxBankAccountsResponse user_list_ledgerx_bank_accounts(user_id)

UserListLedgerxBankAccounts

End-point for getting connected accounts from the clearing house.  The value for the user_id path parameter should match the user_id value returned on the response for the last login request (POST /log_in).

### Example

* Api Key Authentication (cookie):
```python
import time
import openapi_client
from openapi_client.api import banking_api
from openapi_client.model.user_list_ledgerx_bank_accounts_response import UserListLedgerxBankAccountsResponse
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
    api_instance = banking_api.BankingApi(api_client)
    user_id = "user_id_example" # str | Should be filled with your user_id provided on log_in

    # example passing only required values which don't have defaults set
    try:
        # UserListLedgerxBankAccounts
        api_response = api_instance.user_list_ledgerx_bank_accounts(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BankingApi->user_list_ledgerx_bank_accounts: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Should be filled with your user_id provided on log_in |

### Return type

[**UserListLedgerxBankAccountsResponse**](UserListLedgerxBankAccountsResponse.md)

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

# **user_request_deposit**
> UserDepositResponse user_request_deposit(user_id)

UserRequestDeposit

End-point for starting deposits on the logged in user's account.  The value for the user_id path parameter should match the user_id value returned on the response for the last login request (POST /log_in).  In order to request deposits you need to have connected at least one account using (POST /user/{user_id}/banks/linked_accounts).

### Example

* Api Key Authentication (cookie):
```python
import time
import openapi_client
from openapi_client.api import banking_api
from openapi_client.model.user_deposit_request import UserDepositRequest
from openapi_client.model.user_deposit_response import UserDepositResponse
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
    api_instance = banking_api.BankingApi(api_client)
    user_id = "user_id_example" # str | This parameter should be filled with your user_id provided on log_in
    user_deposit_request = UserDepositRequest(
        amount_cents=1,
        bank_id="bank_id_example",
        fee_cents=1,
    ) # UserDepositRequest | Input for starting a deposit. (optional)

    # example passing only required values which don't have defaults set
    try:
        # UserRequestDeposit
        api_response = api_instance.user_request_deposit(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BankingApi->user_request_deposit: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # UserRequestDeposit
        api_response = api_instance.user_request_deposit(user_id, user_deposit_request=user_deposit_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BankingApi->user_request_deposit: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| This parameter should be filled with your user_id provided on log_in |
 **user_deposit_request** | [**UserDepositRequest**](UserDepositRequest.md)| Input for starting a deposit. | [optional]

### Return type

[**UserDepositResponse**](UserDepositResponse.md)

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

# **user_request_withdrawal**
> UserWithdrawalResponse user_request_withdrawal(user_id)

UserRequestWithdrawal

End-point for starting deposits on the logged in user's account.  The value for the user_id path parameter should match the user_id value returned on the response for the last login request (POST /log_in).  In order to request deposits you need to have connected at least one account using (POST /user/{user_id}/banks/linked_accounts).

### Example

* Api Key Authentication (cookie):
```python
import time
import openapi_client
from openapi_client.api import banking_api
from openapi_client.model.user_withdrawal_response import UserWithdrawalResponse
from openapi_client.model.user_withdrawal_request import UserWithdrawalRequest
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
    api_instance = banking_api.BankingApi(api_client)
    user_id = "user_id_example" # str | This parameter should be filled with your user_id provided on log_in
    user_withdrawal_request = UserWithdrawalRequest(
        amount_cents=1,
        bank_id="bank_id_example",
        fee_cents=1,
    ) # UserWithdrawalRequest | Input for getting a token. If bank_account_id is filled it will generate a re-connection token. (optional)

    # example passing only required values which don't have defaults set
    try:
        # UserRequestWithdrawal
        api_response = api_instance.user_request_withdrawal(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BankingApi->user_request_withdrawal: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # UserRequestWithdrawal
        api_response = api_instance.user_request_withdrawal(user_id, user_withdrawal_request=user_withdrawal_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BankingApi->user_request_withdrawal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| This parameter should be filled with your user_id provided on log_in |
 **user_withdrawal_request** | [**UserWithdrawalRequest**](UserWithdrawalRequest.md)| Input for getting a token. If bank_account_id is filled it will generate a re-connection token. | [optional]

### Return type

[**UserWithdrawalResponse**](UserWithdrawalResponse.md)

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

