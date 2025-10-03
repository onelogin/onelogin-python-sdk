# coding: utf-8

"""
    OneLogin API

    Test for custom_attributes support in User model

    The version of the OpenAPI document: 3.1.1
"""


import unittest
import json

import onelogin
from onelogin.models.user import User
from onelogin.rest import ApiException


class TestUserCustomAttributes(unittest.TestCase):
    """User custom_attributes unit test"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_user_with_custom_attributes(self):
        """Test User with custom_attributes"""
        # Create a user with custom_attributes
        user_data = {
            "id": 123,
            "username": "test_user",
            "email": "test@example.com",
            "firstname": "Test",
            "lastname": "User",
            "custom_attributes": {
                "department_code": "ENG001",
                "employee_id": "12345",
                "cost_center": "CC-100"
            }
        }
        
        # Test from_dict
        user = User.from_dict(user_data)
        
        # Verify basic fields
        self.assertEqual(user.id, 123)
        self.assertEqual(user.username, "test_user")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.firstname, "Test")
        self.assertEqual(user.lastname, "User")
        
        # Verify custom_attributes
        self.assertIsNotNone(user.custom_attributes)
        self.assertIsInstance(user.custom_attributes, dict)
        self.assertEqual(user.custom_attributes.get("department_code"), "ENG001")
        self.assertEqual(user.custom_attributes.get("employee_id"), "12345")
        self.assertEqual(user.custom_attributes.get("cost_center"), "CC-100")

    def test_user_without_custom_attributes(self):
        """Test User without custom_attributes"""
        user_data = {
            "id": 456,
            "username": "test_user2",
            "email": "test2@example.com"
        }
        
        user = User.from_dict(user_data)
        
        self.assertEqual(user.id, 456)
        self.assertEqual(user.username, "test_user2")
        self.assertIsNone(user.custom_attributes)

    def test_user_to_dict_with_custom_attributes(self):
        """Test User to_dict with custom_attributes"""
        user = User(
            id=789,
            username="test_user3",
            email="test3@example.com",
            custom_attributes={
                "location": "San Francisco",
                "employee_type": "Full-time"
            }
        )
        
        user_dict = user.to_dict()
        
        self.assertEqual(user_dict["id"], 789)
        self.assertEqual(user_dict["username"], "test_user3")
        self.assertEqual(user_dict["email"], "test3@example.com")
        self.assertIn("custom_attributes", user_dict)
        self.assertEqual(user_dict["custom_attributes"]["location"], "San Francisco")
        self.assertEqual(user_dict["custom_attributes"]["employee_type"], "Full-time")

    def test_user_from_json_with_custom_attributes(self):
        """Test User from_json with custom_attributes"""
        json_str = '''{
            "id": 999,
            "username": "test_user4",
            "email": "test4@example.com",
            "custom_attributes": {
                "badge_number": "B12345",
                "clearance_level": "Level 2"
            }
        }'''
        
        user = User.from_json(json_str)
        
        self.assertEqual(user.id, 999)
        self.assertEqual(user.username, "test_user4")
        self.assertIsNotNone(user.custom_attributes)
        self.assertEqual(user.custom_attributes.get("badge_number"), "B12345")
        self.assertEqual(user.custom_attributes.get("clearance_level"), "Level 2")


if __name__ == '__main__':
    unittest.main()
