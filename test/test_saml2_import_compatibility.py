# coding: utf-8

"""
Test import behavior for SAML2 compatibility module
"""

import pytest
import os
import site


class TestSaml2ImportCompatibility:
    """Test the SAML2 import compatibility module"""

    def test_import_onelogin_saml2_auth_raises_helpful_error(self):
        """Test that importing OneLogin_Saml2_Auth raises a helpful error message"""
        
        # Attempt to import OneLogin_Saml2_Auth
        with pytest.raises(ImportError) as exc_info:
            from onelogin.saml2.auth import OneLogin_Saml2_Auth
        
        # Verify the error message contains helpful guidance
        error_message = str(exc_info.value)
        assert "OneLogin_Saml2_Auth is not available" in error_message
        assert "python3-saml" in error_message
        
        # The specific message depends on whether python3-saml is detected
        python3_saml_installed = self._check_python3_saml_installed()
        
        if python3_saml_installed:
            # Should show namespace conflict message
            assert "namespace conflict" in error_message
            assert "both 'onelogin'" in error_message
            assert "pip uninstall onelogin" in error_message
        else:
            # Should show installation instruction message
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

    def test_python3_saml_detection_function(self):
        """Test that the python3-saml detection function works correctly"""
        
        import onelogin.saml2.auth
        result = onelogin.saml2.auth._check_python3_saml_installed()
        # Should return a boolean
        assert isinstance(result, bool)
        
        # Test by checking if the expected path exists manually
        expected_exists = False
        for site_dir in site.getsitepackages() + [site.getusersitepackages()]:
            if site_dir and os.path.exists(site_dir):
                potential_path = os.path.join(site_dir, 'onelogin', 'saml2', 'auth.py')
                if os.path.exists(potential_path):
                    expected_exists = True
                    break
        
        assert result == expected_exists

    def _check_python3_saml_installed(self):
        """Helper method to check if python3-saml is installed"""
        for site_dir in site.getsitepackages() + [site.getusersitepackages()]:
            if site_dir and os.path.exists(site_dir):
                potential_path = os.path.join(site_dir, 'onelogin', 'saml2', 'auth.py')
                if os.path.exists(potential_path):
                    return True
        return False