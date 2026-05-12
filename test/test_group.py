# coding: utf-8

import unittest
import datetime

import onelogin
from onelogin.models.group import Group  # noqa: E501
from onelogin.rest import ApiException

class TestGroup(unittest.TestCase):
    """Group unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Group
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Group`
        """
        model = onelogin.models.group.Group()  # noqa: E501
        if include_optional :
            return Group(
                id = 425741, 
                name = 'group.security.policy.default', 
                reference = 'null'
            )
        else :
            return Group(
        )
        """

    def testGroup(self):
        """Test Group"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
