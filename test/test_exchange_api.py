"""
    Kalshi API.

    This documentation describes Kalshi's rest API for market makers  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import kalshi
from kalshi.api.exchange_api import ExchangeApi  # noqa: E501


class TestExchangeApi(unittest.TestCase):
    """ExchangeApi unit test stubs"""

    def setUp(self):
        self.api = ExchangeApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_exchange_status(self):
        """Test case for get_exchange_status

        """
        pass


if __name__ == '__main__':
    unittest.main()
