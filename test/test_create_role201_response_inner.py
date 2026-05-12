# coding: utf-8

import unittest
import datetime

import onelogin
from onelogin.models.create_role201_response_inner import CreateRole201ResponseInner  # noqa: E501
from onelogin.rest import ApiException

class TestCreateRole201ResponseInner(unittest.TestCase):
    """CreateRole201ResponseInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test CreateRole201ResponseInner
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateRole201ResponseInner`
        """
        model = onelogin.models.create_role201_response_inner.CreateRole201ResponseInner()  # noqa: E501
        if include_optional :
            return CreateRole201ResponseInner(
                id = 56
            )
        else :
            return CreateRole201ResponseInner(
        )
        """

    def testCreateRole201ResponseInner(self):
        """Test CreateRole201ResponseInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

    def test_from_dict_with_id(self):
        """Test that CreateRole201ResponseInner can be deserialized from a dict containing an id."""
        result = CreateRole201ResponseInner.from_dict({"id": 123456})
        self.assertIsInstance(result, CreateRole201ResponseInner)
        self.assertEqual(result.id, 123456)

    def test_from_dict_none(self):
        """Test that from_dict handles None gracefully."""
        result = CreateRole201ResponseInner.from_dict(None)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
