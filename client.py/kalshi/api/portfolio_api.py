"""
    Kalshi API.

    This documentation describes Kalshi's rest API for market makers  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from kalshi.api_client import ApiClient, Endpoint as _Endpoint
from kalshi.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from kalshi.model.user_get_portfolio_history_request import UserGetPortfolioHistoryRequest
from kalshi.model.user_get_portfolio_history_response import UserGetPortfolioHistoryResponse


class PortfolioApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __user_get_portfolio_history(
            self,
            user_id,
            **kwargs
        ):
            """UserGetPortfolioHistory  # noqa: E501

            End-point for getting the logged in user's portfolio historical track.  The value for the user_id path parameter should match the user_id value returned on the response for the last login request (POST /log_in).  # noqa: E501
            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.user_get_portfolio_history(user_id, async_req=True)
            >>> result = thread.get()

            Args:
                user_id (str): This parameter should be filled with your user_id provided on log_in

            Keyword Args:
                user_get_portfolio_history_request (UserGetPortfolioHistoryRequest): Order create input data. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                UserGetPortfolioHistoryResponse
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['user_id'] = \
                user_id
            return self.call_with_http_info(**kwargs)

        self.user_get_portfolio_history = _Endpoint(
            settings={
                'response_type': (UserGetPortfolioHistoryResponse,),
                'auth': [
                    'cookie'
                ],
                'endpoint_path': '/users/{user_id}/portfolio/history',
                'operation_id': 'user_get_portfolio_history',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'user_id',
                    'user_get_portfolio_history_request',
                ],
                'required': [
                    'user_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'user_id':
                        (str,),
                    'user_get_portfolio_history_request':
                        (UserGetPortfolioHistoryRequest,),
                },
                'attribute_map': {
                    'user_id': 'user_id',
                },
                'location_map': {
                    'user_id': 'path',
                    'user_get_portfolio_history_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__user_get_portfolio_history
        )