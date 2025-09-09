# coding: utf-8

"""
SAML2 Authentication Module

OneLogin_Saml2_Auth is not part of this package. This package (onelogin) is
for OneLogin API management. For SAML2 authentication, you need the
'python3-saml' package.

To fix this import error:

1. Install the correct package:
   pip install python3-saml

2. Import from the correct module:
   from onelogin.saml2.auth import OneLogin_Saml2_Auth

   OR use the newer syntax:
   from onelogin.saml2.auth import Auth as OneLogin_Saml2_Auth

For more information, see: https://github.com/onelogin/python3-saml
"""


class ImportError(Exception):
    """Custom import error with helpful message"""
    pass


def __getattr__(name):
    """
    Intercept attempts to import OneLogin_Saml2_Auth and provide helpful
    error message.
    """
    if name == "OneLogin_Saml2_Auth":
        raise ImportError(
            "OneLogin_Saml2_Auth is not available in this package.\n\n"
            "This package (onelogin) is for OneLogin API management.\n"
            "For SAML2 authentication, you need the 'python3-saml' "
            "package.\n\n"
            "To fix this:\n"
            "1. Install the correct package: pip install python3-saml\n"
            "2. Import from: from onelogin.saml2.auth import "
            "OneLogin_Saml2_Auth\n\n"
            "Note: You may need to uninstall this 'onelogin' package if you "
            "only need SAML2 auth:\n"
            "pip uninstall onelogin\n\n"
            "For more information: https://github.com/onelogin/python3-saml"
        )

    raise AttributeError(
        f"module 'onelogin.saml2.auth' has no attribute '{name}'"
    )


# Make module attributes available for inspection
__all__ = []
