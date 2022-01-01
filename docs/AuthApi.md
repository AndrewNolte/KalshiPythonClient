# kalshi.AuthApi

All URIs are relative to *https://trading-api.kalshi.com/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login**](AuthApi.md#login) | **POST** /log_in | Login
[**logout**](AuthApi.md#logout) | **POST** /log_out | Logout
[**reset_password**](AuthApi.md#reset_password) | **POST** /passwords/reset | ResetPassword
[**reset_password_confirm**](AuthApi.md#reset_password_confirm) | **PUT** /passwords/reset/{code}/confirm | ResetPasswordConfirm


# **login**
> LoginResponse login()

Login

End-point to start a rest session with Kalshi.

### Example

```python
import time
import kalshi
from kalshi.api import auth_api
from kalshi.model.login_response import LoginResponse
from kalshi.model.login_request import LoginRequest
from pprint import pprint
# Defining the host is optional and defaults to https://trading-api.kalshi.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kalshi.Configuration(
    host = "https://trading-api.kalshi.com/v1"
)


# Enter a context with an instance of the API client
with kalshi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    login_request = LoginRequest(
        email="email_example",
        password="password_example",
    ) # LoginRequest | Login input data (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Login
        api_response = api_instance.login(login_request=login_request)
        pprint(api_response)
    except kalshi.ApiException as e:
        print("Exception when calling AuthApi->login: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_request** | [**LoginRequest**](LoginRequest.md)| Login input data | [optional]

### Return type

[**LoginResponse**](LoginResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** |  |  * Set-Cookie - Access token is set on a cookie named &#39;sessions&#39; as well <br>  |
**400** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**401** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**403** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**500** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**503** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> logout()

Logout

End-point to terminates your session with Kalshi.

### Example

* Api Key Authentication (cookie):
```python
import time
import kalshi
from kalshi.api import auth_api
from pprint import pprint
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
    api_instance = auth_api.AuthApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Logout
        api_instance.logout()
    except kalshi.ApiException as e:
        print("Exception when calling AuthApi->logout: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

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
**503** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password**
> reset_password()

ResetPassword

End-point to request a password reset email link.  To be used in case you forget your password.

### Example

```python
import time
import kalshi
from kalshi.api import auth_api
from kalshi.model.reset_password_request import ResetPasswordRequest
from pprint import pprint
# Defining the host is optional and defaults to https://trading-api.kalshi.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kalshi.Configuration(
    host = "https://trading-api.kalshi.com/v1"
)


# Enter a context with an instance of the API client
with kalshi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    reset_password_request = ResetPasswordRequest(
        email="email_example",
    ) # ResetPasswordRequest | Reset password input data (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ResetPassword
        api_instance.reset_password(reset_password_request=reset_password_request)
    except kalshi.ApiException as e:
        print("Exception when calling AuthApi->reset_password: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reset_password_request** | [**ResetPasswordRequest**](ResetPasswordRequest.md)| Reset password input data | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | No fields are returned on the response. |  -  |
**400** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**500** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**503** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password_confirm**
> reset_password_confirm(code)

ResetPasswordConfirm

End-point to finish the password reset flow.  The code param on the path should be filled with the verification code sent by email.

### Example

```python
import time
import kalshi
from kalshi.api import auth_api
from kalshi.model.confirm_password_reset_request import ConfirmPasswordResetRequest
from pprint import pprint
# Defining the host is optional and defaults to https://trading-api.kalshi.com/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = kalshi.Configuration(
    host = "https://trading-api.kalshi.com/v1"
)


# Enter a context with an instance of the API client
with kalshi.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = auth_api.AuthApi(api_client)
    code = "code_example" # str | Should be filled with the verification code received on the sign-up email.
    confirm_password_reset_request = ConfirmPasswordResetRequest(
        password="password_example",
        user_id="user_id_example",
    ) # ConfirmPasswordResetRequest | Data required to finish a password reset. (optional)

    # example passing only required values which don't have defaults set
    try:
        # ResetPasswordConfirm
        api_instance.reset_password_confirm(code)
    except kalshi.ApiException as e:
        print("Exception when calling AuthApi->reset_password_confirm: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # ResetPasswordConfirm
        api_instance.reset_password_confirm(code, confirm_password_reset_request=confirm_password_reset_request)
    except kalshi.ApiException as e:
        print("Exception when calling AuthApi->reset_password_confirm: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Should be filled with the verification code received on the sign-up email. |
 **confirm_password_reset_request** | [**ConfirmPasswordResetRequest**](ConfirmPasswordResetRequest.md)| Data required to finish a password reset. | [optional]

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No fields are returned on the response. |  -  |
**400** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**500** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**503** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

