# coding: utf-8

import unittest
import datetime
from unittest.mock import Mock, patch

import onelogin
from onelogin.models.get_auth_factors200_response import GetAuthFactors200Response
from onelogin.api.multi_factor_authentication_api import MultiFactorAuthenticationApi
from onelogin.rest import ApiException


class TestGetAuthFactorsFix(unittest.TestCase):
    """Test case for get_auth_factors return type fix"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_get_auth_factors_list_response(self):
        """
        Test that GetAuthFactors200Response can be deserialized from a list.
        This test validates the fix where API returns a list of factors
        but model expected a single object.
        """
        # Example response data from API (a list of factors)
        factors_data = [
            {
                "factor_id": 3098,
                "name": "OneLogin SMS",
                "auth_factor_name": "OneLogin SMS"
            },
            {
                "factor_id": 3099,
                "name": "YubiKey",
                "auth_factor_name": "YubiKey"
            }
        ]
        
        # Each item in the list should be deserializable as GetAuthFactors200Response
        factors = [GetAuthFactors200Response.from_dict(factor_data) for factor_data in factors_data]
        
        self.assertEqual(len(factors), 2)
        self.assertEqual(factors[0].factor_id, 3098)
        self.assertEqual(factors[0].name, "OneLogin SMS")
        self.assertEqual(factors[1].factor_id, 3099)
        self.assertEqual(factors[1].name, "YubiKey")

    def test_single_auth_factor_from_dict(self):
        """
        Test that a single auth factor can be created from dict.
        """
        factor_data = {
            "factor_id": 3098,
            "name": "OneLogin SMS",
            "auth_factor_name": "OneLogin SMS"
        }
        
        factor = GetAuthFactors200Response.from_dict(factor_data)
        self.assertEqual(factor.factor_id, 3098)
        self.assertEqual(factor.name, "OneLogin SMS")
        self.assertEqual(factor.auth_factor_name, "OneLogin SMS")

    def test_auth_factor_with_optional_fields(self):
        """
        Test that auth factor works with optional fields.
        """
        factor_data = {
            "factor_id": 3098,
            # name and auth_factor_name are optional
        }
        
        factor = GetAuthFactors200Response.from_dict(factor_data)
        self.assertEqual(factor.factor_id, 3098)
        self.assertIsNone(factor.name)
        self.assertIsNone(factor.auth_factor_name)

    def test_get_auth_factors_api_method_returns_list(self):
        """
        Integration test that verifies the get_auth_factors API method 
        returns List[GetAuthFactors200Response] when called with a mocked API response.
        This validates the fix for the return type change.
        """
        # Create list of GetAuthFactors200Response objects
        factor1 = GetAuthFactors200Response.from_dict({
            "factor_id": 3098,
            "name": "OneLogin SMS",
            "auth_factor_name": "OneLogin SMS"
        })
        factor2 = GetAuthFactors200Response.from_dict({
            "factor_id": 3099,
            "name": "YubiKey",
            "auth_factor_name": "YubiKey"
        })
        expected_result = [factor1, factor2]
        
        # Create API instance
        api = MultiFactorAuthenticationApi()
        
        # Mock the api_client.call_api method to return deserialized objects
        with patch.object(api.api_client, 'call_api', return_value=expected_result) as mock_call_api:
            # Call the method
            result = api.get_auth_factors(user_id=123)
            
            # Verify the result is a list
            self.assertIsInstance(result, list)
            self.assertEqual(len(result), 2)
            
            # Verify each item is a GetAuthFactors200Response instance
            self.assertIsInstance(result[0], GetAuthFactors200Response)
            self.assertIsInstance(result[1], GetAuthFactors200Response)
            
            # Verify the data
            self.assertEqual(result[0].factor_id, 3098)
            self.assertEqual(result[0].name, "OneLogin SMS")
            self.assertEqual(result[1].factor_id, 3099)
            self.assertEqual(result[1].name, "YubiKey")
            
            # Verify call_api was called with correct parameters including the List response type
            mock_call_api.assert_called_once()
            call_args = mock_call_api.call_args
            # Check that response_types_map includes List[GetAuthFactors200Response]
            response_types_map = call_args[1]['response_types_map']
            self.assertEqual(response_types_map['200'], 'List[GetAuthFactors200Response]')


if __name__ == '__main__':
    unittest.main()
