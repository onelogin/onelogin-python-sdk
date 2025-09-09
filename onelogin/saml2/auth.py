# coding: utf-8

"""
SAML2 Authentication Module

This module provides compatibility for users expecting to import
OneLogin_Saml2_Auth from onelogin.saml2.auth. However, OneLogin_Saml2_Auth is
actually provided by the 'python3-saml' package, not this onelogin package.

This onelogin package is for OneLogin API management, while python3-saml is
for SAML2 authentication integration.
"""

import os
import site


def _check_python3_saml_installed():
    """Check if python3-saml is installed by looking for its onelogin.saml2.auth module"""
    for site_dir in site.getsitepackages() + [site.getusersitepackages()]:
        if site_dir and os.path.exists(site_dir):
            potential_path = os.path.join(site_dir, 'onelogin', 'saml2', 'auth.py')
            if os.path.exists(potential_path):
                return True
    return False


def __getattr__(name):
    """
    Intercept attempts to import OneLogin_Saml2_Auth and provide helpful
    error message based on whether python3-saml is detected.
    """
    if name == "OneLogin_Saml2_Auth":
        python3_saml_installed = _check_python3_saml_installed()
        
        if python3_saml_installed:
            # python3-saml is installed but there's a namespace conflict
            raise ImportError(
                "OneLogin_Saml2_Auth is not available due to a package namespace conflict.\n\n"
                "You have both 'onelogin' (API management) and 'python3-saml' (SAML authentication) installed.\n"
                "These packages both provide 'onelogin' modules, causing a conflict.\n\n"
                "To fix this conflict:\n\n"
                "OPTION 1 - If you only need SAML authentication:\n"
                "  1. Uninstall this package: pip uninstall onelogin\n"
                "  2. Then import will work: from onelogin.saml2.auth import OneLogin_Saml2_Auth\n\n"
                "OPTION 2 - If you need both packages:\n"
                "  1. Import directly from python3-saml's location in site-packages\n"
                "  2. See: https://github.com/onelogin/python3-saml for documentation\n\n"
                "OPTION 3 - Use virtual environments to separate the packages\n\n"
                "To check your installations: pip list | grep -E '(onelogin|python3-saml)'"
            )
        else:
            # python3-saml is not installed
            raise ImportError(
                "OneLogin_Saml2_Auth is not available in this package.\n\n"
                "This package (onelogin) is for OneLogin API management.\n"
                "For SAML2 authentication, you need the 'python3-saml' package.\n\n"
                "To fix this:\n"
                "1. Install the correct package: pip install python3-saml\n"
                "2. Import from: from onelogin.saml2.auth import OneLogin_Saml2_Auth\n\n"
                "For more information: https://github.com/onelogin/python3-saml"
            )

    raise AttributeError(
        f"module 'onelogin.saml2.auth' has no attribute '{name}'"
    )


# Make module attributes available for inspection
__all__ = []
