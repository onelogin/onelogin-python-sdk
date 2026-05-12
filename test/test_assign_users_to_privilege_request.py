# coding: utf-8

import unittest
import datetime

import onelogin
from onelogin.models.assign_users_to_privilege_request import AssignUsersToPrivilegeRequest  # noqa: E501
from onelogin.rest import ApiException

class TestAssignUsersToPrivilegeRequest(unittest.TestCase):
    """AssignUsersToPrivilegeRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test AssignUsersToPrivilegeRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AssignUsersToPrivilegeRequest`
        """
        model = onelogin.models.assign_users_to_privilege_request.AssignUsersToPrivilegeRequest()  # noqa: E501
        if include_optional :
            return AssignUsersToPrivilegeRequest(
                users = [
                    56
                    ]
            )
        else :
            return AssignUsersToPrivilegeRequest(
        )
        """

    def testAssignUsersToPrivilegeRequest(self):
        """Test AssignUsersToPrivilegeRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
