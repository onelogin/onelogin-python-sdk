# coding: utf-8

import unittest

import onelogin
from onelogin.api.invite_links_api import InviteLinksApi  # noqa: E501
from onelogin.rest import ApiException


class TestInviteLinksApi(unittest.TestCase):
    """InviteLinksApi unit test stubs"""

    def setUp(self):
        self.api = onelogin.api.invite_links_api.InviteLinksApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_invite_link(self):
        """Test case for get_invite_link

        Generate Invite Link  # noqa: E501
        """
        pass

    def test_send_invite_link(self):
        """Test case for send_invite_link

        Send  Invite Link  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
