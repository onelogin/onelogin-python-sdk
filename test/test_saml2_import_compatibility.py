# coding: utf-8

"""
Test import behavior for SAML2 compatibility module
"""

import pytest
from onelogin.saml2.auth import ImportError


class TestSaml2ImportCompatibility:
    """Test the SAML2 import compatibility module"""

    def test_import_onelogin_saml2_auth_raises_helpful_error(self):
        """Test that importing OneLogin_Saml2_Auth raises a helpful error message"""
        
        # Attempt to import OneLogin_Saml2_Auth
        with pytest.raises(ImportError) as exc_info:
            from onelogin.saml2.auth import OneLogin_Saml2_Auth
        
        # Verify the error message contains helpful guidance
        error_message = str(exc_info.value)
        assert "OneLogin_Saml2_Auth is not available in this package" in error_message
        assert "python3-saml" in error_message
        assert "pip install python3-saml" in error_message
        assert "https://github.com/onelogin/python3-saml" in error_message

    def test_getattr_for_nonexistent_attribute_raises_attribute_error(self):
        """Test that accessing non-existent attributes raises AttributeError"""
        
        import onelogin.saml2.auth
        with pytest.raises(AttributeError) as exc_info:
            getattr(onelogin.saml2.auth, 'NonExistentClass')
        
        error_message = str(exc_info.value)
        assert "module 'onelogin.saml2.auth' has no attribute 'NonExistentClass'" in error_message

    def test_saml2_module_can_be_imported(self):
        """Test that the saml2 module itself can be imported without error"""
        
        import onelogin.saml2
        # Should not raise any errors
        
    def test_saml2_auth_module_can_be_imported(self):
        """Test that the saml2.auth module itself can be imported without error"""
        
        import onelogin.saml2.auth
        # Should not raise any errors

    def test_saml2_auth_module_has_empty_all_list(self):
        """Test that __all__ is defined and empty"""
        
        import onelogin.saml2.auth
        assert hasattr(onelogin.saml2.auth, '__all__')
        assert onelogin.saml2.auth.__all__ == []