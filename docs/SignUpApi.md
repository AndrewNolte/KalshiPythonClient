# openapi_client.SignUpApi

All URIs are relative to *http://localhost/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_sign_up_link**](SignUpApi.md#send_sign_up_link) | **POST** /users/resume_sign_up | SendSignUpLink
[**user_create**](SignUpApi.md#user_create) | **POST** /users | UserCreate
[**user_get_kyc**](SignUpApi.md#user_get_kyc) | **GET** /users/{user_id}/kyc | UserGetKyc
[**user_send_email_confirmation**](SignUpApi.md#user_send_email_confirmation) | **POST** /users/{user_id}/email_confirmation | UserSendEmailConfirmation
[**user_update_kyc**](SignUpApi.md#user_update_kyc) | **PUT** /users/{user_id}/kyc | UserUpdateKyc
[**user_update_profile**](SignUpApi.md#user_update_profile) | **PUT** /users/{user_id} | UserUpdateProfile
[**user_verify**](SignUpApi.md#user_verify) | **POST** /users/{user_id}/verify | UserVerify


# **send_sign_up_link**
> send_sign_up_link()

SendSignUpLink

End-point for sending a link to resume sign-up. To be used in case the user verification e-mail is lost.

### Example

* Api Key Authentication (cookie):
```python
import time
import openapi_client
from openapi_client.api import sign_up_api
from openapi_client.model.send_sign_up_link_request import SendSignUpLinkRequest
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
    api_instance = sign_up_api.SignUpApi(api_client)
    send_sign_up_link_request = SendSignUpLinkRequest(
        email="email_example",
    ) # SendSignUpLinkRequest | User send sign-up link input fields. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # SendSignUpLink
        api_instance.send_sign_up_link(send_sign_up_link_request=send_sign_up_link_request)
    except openapi_client.ApiException as e:
        print("Exception when calling SignUpApi->send_sign_up_link: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_sign_up_link_request** | [**SendSignUpLinkRequest**](SendSignUpLinkRequest.md)| User send sign-up link input fields. | [optional]

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
**202** | No fields are returned on the response. |  -  |
**400** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**401** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**403** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**500** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**503** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_create**
> CreateUserResponse user_create()

UserCreate

End-point for creating an user. A call to this end-point starts the sign-up flow.

### Example

```python
import time
import openapi_client
from openapi_client.api import sign_up_api
from openapi_client.model.create_user_request import CreateUserRequest
from openapi_client.model.create_user_response import CreateUserResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sign_up_api.SignUpApi(api_client)
    create_user_request = CreateUserRequest(
        area_code="022",
        country_code="1",
        email="john@example.com",
        password="s3cr3t",
        phone_number="4759128",
    ) # CreateUserRequest | User create input data. (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # UserCreate
        api_response = api_instance.user_create(create_user_request=create_user_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SignUpApi->user_create: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_request** | [**CreateUserRequest**](CreateUserRequest.md)| User create input data. | [optional]

### Return type

[**CreateUserResponse**](CreateUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** |  |  -  |
**400** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**500** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_get_kyc**
> GetUserKycResponse user_get_kyc(user_id)

UserGetKyc

End-point for retrieving your user kyc profile.  The value for the user_id path parameter should match the user_id value returned on the response for the last login request (POST /log_in).

### Example

* Api Key Authentication (cookie):
```python
import time
import openapi_client
from openapi_client.api import sign_up_api
from openapi_client.model.get_user_kyc_response import GetUserKycResponse
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
    api_instance = sign_up_api.SignUpApi(api_client)
    user_id = "user_id_example" # str | Should be filled with your user_id provided on log_in

    # example passing only required values which don't have defaults set
    try:
        # UserGetKyc
        api_response = api_instance.user_get_kyc(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SignUpApi->user_get_kyc: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Should be filled with your user_id provided on log_in |

### Return type

[**GetUserKycResponse**](GetUserKycResponse.md)

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

# **user_send_email_confirmation**
> user_send_email_confirmation(user_id)

UserSendEmailConfirmation

End-point for re-sending email verification. To be used in case e-mail verification doesn't arrive or verification code is expired.  The value for the user_id path parameter should match the user_id value returned on the response for the create user request (POST /users).

### Example

* Api Key Authentication (cookie):
```python
import time
import openapi_client
from openapi_client.api import sign_up_api
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
    api_instance = sign_up_api.SignUpApi(api_client)
    user_id = "user_id_example" # str | Should be filled with your user_id provided on log_in

    # example passing only required values which don't have defaults set
    try:
        # UserSendEmailConfirmation
        api_instance.user_send_email_confirmation(user_id)
    except openapi_client.ApiException as e:
        print("Exception when calling SignUpApi->user_send_email_confirmation: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| Should be filled with your user_id provided on log_in |

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
**202** | No fields are returned on the response. |  -  |
**400** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**401** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**403** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**500** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**503** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_update_kyc**
> user_update_kyc(user_id)

UserUpdateKyc

End-point for submitting / updating your user kyc profile during sign-up.  The value for the user_id path parameter should match the user_id value returned on the response for the create user request (POST /users).

### Example

* Api Key Authentication (cookie):
```python
import time
import openapi_client
from openapi_client.api import sign_up_api
from openapi_client.model.user_update_kyc_request import UserUpdateKycRequest
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
    api_instance = sign_up_api.SignUpApi(api_client)
    user_id = "user_id_example" # str | This parameter should be filled with your user_id provided on log_in
    user_update_kyc_request = UserUpdateKycRequest(
        ssn="123456789",
    ) # UserUpdateKycRequest | User verification input fields. (optional)

    # example passing only required values which don't have defaults set
    try:
        # UserUpdateKyc
        api_instance.user_update_kyc(user_id)
    except openapi_client.ApiException as e:
        print("Exception when calling SignUpApi->user_update_kyc: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # UserUpdateKyc
        api_instance.user_update_kyc(user_id, user_update_kyc_request=user_update_kyc_request)
    except openapi_client.ApiException as e:
        print("Exception when calling SignUpApi->user_update_kyc: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| This parameter should be filled with your user_id provided on log_in |
 **user_update_kyc_request** | [**UserUpdateKycRequest**](UserUpdateKycRequest.md)| User verification input fields. | [optional]

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
**503** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_update_profile**
> user_update_profile(user_id)

UserUpdateProfile

End-point for submitting your user profile during sign-up, or updating it after sign-up is complete.  The value for the user_id path parameter should match the user_id value returned either in the response for the last login request (POST /log_in) or for the create user request (POST /users).

### Example

* Api Key Authentication (cookie):
```python
import time
import openapi_client
from openapi_client.api import sign_up_api
from openapi_client.model.user_update_profile_request import UserUpdateProfileRequest
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
    api_instance = sign_up_api.SignUpApi(api_client)
    user_id = "user_id_example" # str | This parameter should be filled with your user_id provided on log_in
    user_update_profile_request = UserUpdateProfileRequest(
        birth_date="birth_date_example",
        city="city_example",
        country="US",
        finished_fre=True,
        first_name="first_name_example",
        last_name="last_name_example",
        postal_code="92044",
        state="NY",
        street1="street1_example",
        street2="street2_example",
        use_bid_ask=True,
        watchlist=[
            "watchlist_example",
        ],
    ) # UserUpdateProfileRequest | Editable user fields (optional)

    # example passing only required values which don't have defaults set
    try:
        # UserUpdateProfile
        api_instance.user_update_profile(user_id)
    except openapi_client.ApiException as e:
        print("Exception when calling SignUpApi->user_update_profile: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # UserUpdateProfile
        api_instance.user_update_profile(user_id, user_update_profile_request=user_update_profile_request)
    except openapi_client.ApiException as e:
        print("Exception when calling SignUpApi->user_update_profile: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| This parameter should be filled with your user_id provided on log_in |
 **user_update_profile_request** | [**UserUpdateProfileRequest**](UserUpdateProfileRequest.md)| Editable user fields | [optional]

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

# **user_verify**
> LoginResponse user_verify(user_id)

UserVerify

End-point for completing email verification during sign-up.  The value for the user_id path parameter should match the user_id value returned on the email verification link query param.

### Example

```python
import time
import openapi_client
from openapi_client.api import sign_up_api
from openapi_client.model.login_response import LoginResponse
from openapi_client.model.user_verify_request import UserVerifyRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost/v1"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = sign_up_api.SignUpApi(api_client)
    user_id = "user_id_example" # str | This parameter should be filled with your user_id provided on log_in
    user_verify_request = UserVerifyRequest(
        code="code_example",
    ) # UserVerifyRequest | User email verification input data (optional)

    # example passing only required values which don't have defaults set
    try:
        # UserVerify
        api_response = api_instance.user_verify(user_id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SignUpApi->user_verify: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # UserVerify
        api_response = api_instance.user_verify(user_id, user_verify_request=user_verify_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SignUpApi->user_verify: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**| This parameter should be filled with your user_id provided on log_in |
 **user_verify_request** | [**UserVerifyRequest**](UserVerifyRequest.md)| User email verification input data | [optional]

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
**500** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |
**503** | JSONError is a generic structure for API error responses. |  * code -  <br>  * details -  <br>  * message -  <br>  * service -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

