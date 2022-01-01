"""
    Kalshi API.

    This documentation describes Kalshi's rest API for market makers  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import kalshi
from kalshi.api.account_api import AccountApi  # noqa: E501


class TestAccountApi(unittest.TestCase):
    """AccountApi unit test stubs"""

    def setUp(self):
        self.api = AccountApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_change_subscription(self):
        """Test case for change_subscription

        ChangeSubscription  # noqa: E501
        """
        pass

    def test_get_notification_preferences(self):
        """Test case for get_notification_preferences

        GetNotificationPreferences  # noqa: E501
        """
        pass

    def test_notification_mark_read(self):
        """Test case for notification_mark_read

        NotificationMarkRead  # noqa: E501
        """
        pass

    def test_user_get_account_history(self):
        """Test case for user_get_account_history

        UserGetAccountHistory  # noqa: E501
        """
        pass

    def test_user_get_notifications(self):
        """Test case for user_get_notifications

        UserGetNotifications  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()