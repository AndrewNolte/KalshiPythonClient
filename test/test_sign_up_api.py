"""
    Kalshi API.

    This documentation describes Kalshi's rest API for market makers  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.sign_up_api import SignUpApi  # noqa: E501


class TestSignUpApi(unittest.TestCase):
    """SignUpApi unit test stubs"""

    def setUp(self):
        self.api = SignUpApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_send_sign_up_link(self):
        """Test case for send_sign_up_link

        SendSignUpLink  # noqa: E501
        """
        pass

    def test_user_create(self):
        """Test case for user_create

        UserCreate  # noqa: E501
        """
        pass

    def test_user_get_kyc(self):
        """Test case for user_get_kyc

        UserGetKyc  # noqa: E501
        """
        pass

    def test_user_send_email_confirmation(self):
        """Test case for user_send_email_confirmation

        UserSendEmailConfirmation  # noqa: E501
        """
        pass

    def test_user_update_kyc(self):
        """Test case for user_update_kyc

        UserUpdateKyc  # noqa: E501
        """
        pass

    def test_user_update_profile(self):
        """Test case for user_update_profile

        UserUpdateProfile  # noqa: E501
        """
        pass

    def test_user_verify(self):
        """Test case for user_verify

        UserVerify  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()