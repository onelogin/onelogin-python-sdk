# coding: utf-8

"""
    OneLogin API

    OpenAPI Specification for OneLogin  # noqa: E501

    The version of the OpenAPI document: 3.1.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import unittest

import onelogin
from onelogin.api.groups_api import GroupsApi  # noqa: E501
from onelogin.rest import ApiException


class TestGroupsApi(unittest.TestCase):
    """GroupsApi unit test stubs"""

    def setUp(self):
        self.api = onelogin.api.groups_api.GroupsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_group_by_id(self):
        """Test case for get_group_by_id

        Get Group by ID  # noqa: E501
        """
        pass

    def test_get_groups(self):
        """Test case for get_groups

        Get Groups  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
