# -*- coding: utf-8 -*-

""" Constants class

Copyright (c) 2017, OneLogin, Inc.
All rights reserved.

Constants class of the OneLogin's Python SDK.

"""


class Constants(object):
    """

    This class defines all the constants that will be used
    in the OneLogin's Python SDK.

    """

    # OAuth2 Tokens URLs
    TOKEN_REQUEST_URL = "https://api.%s.onelogin.com/auth/oauth2/v2/token"
    TOKEN_REFRESH_URL = "https://api.%s.onelogin.com/auth/oauth2/v2/token"
    TOKEN_REVOKE_URL = "https://api.%s.onelogin.com/auth/oauth2/revoke"
    GET_RATE_URL = "https://api.%s.onelogin.com/auth/rate_limit"

    # User URLs
    GET_USERS_URL = "https://api.%s.onelogin.com/api/1/users"
    GET_USER_URL = "https://api.%s.onelogin.com/api/1/users/%s"
    GET_APPS_FOR_USER_URL = "https://api.%s.onelogin.com/api/1/users/%s/apps"
    GET_ROLES_FOR_USER_URL = "https://api.%s.onelogin.com/api/1/users/%s/roles"
    GET_CUSTOM_ATTRIBUTES_URL = "https://api.%s.onelogin.com/api/1/users/custom_attributes"
    CREATE_USER_URL = "https://api.%s.onelogin.com/api/1/users"
    UPDATE_USER_URL = "https://api.%s.onelogin.com/api/1/users/%s"
    DELETE_USER_URL = "https://api.%s.onelogin.com/api/1/users/%s"
    ADD_ROLE_TO_USER_URL = "https://api.%s.onelogin.com/api/1/users/%s/add_roles"
    DELETE_ROLE_TO_USER_URL = "https://api.%s.onelogin.com/api/1/users/%s/remove_roles"
    SET_PW_CLEARTEXT = "https://api.%s.onelogin.com/api/1/users/set_password_clear_text/%s"
    SET_PW_SALT = "https://api.%s.onelogin.com/api/1/users/set_password_using_salt/%s"
    SET_STATE_TO_USER_URL = "https://api.%s.onelogin.com/api/1/users/%s/set_state"
    SET_CUSTOM_ATTRIBUTE_TO_USER_URL = "https://api.%s.onelogin.com/api/1/users/%s/set_custom_attributes"
    LOG_USER_OUT_URL = "https://api.%s.onelogin.com/api/1/users/%s/logout"
    LOCK_USER_URL = "https://api.%s.onelogin.com/api/1/users/%s/lock_user"

    # Role URLs
    GET_ROLES_URL = "https://api.%s.onelogin.com/api/1/roles"
    CREATE_ROLE_URL = "https://api.%s.onelogin.com/api/1/roles"
    GET_ROLE_URL = "https://api.%s.onelogin.com/api/1/roles/%s"

    # Event URLS
    GET_EVENT_TYPES_URL = "https://api.%s.onelogin.com/api/1/events/types"
    GET_EVENTS_URL = "https://api.%s.onelogin.com/api/1/events"
    CREATE_EVENT_URL = "https://api.%s.onelogin.com/api/1/events"
    GET_EVENT_URL = "https://api.%s.onelogin.com/api/1/events/%s"

    # Group URLs
    GET_GROUPS_URL = "https://api.%s.onelogin.com/api/1/groups"
    CREATE_GROUP_URL = "https://api.%s.onelogin.com/api/1/groups"
    GET_GROUP_URL = "https://api.%s.onelogin.com/api/1/groups/%s"

    # Custom Login URLs
    SESSION_LOGIN_TOKEN_URL = "https://api.%s.onelogin.com/api/1/login/auth"
    GET_TOKEN_VERIFY_FACTOR = "https://api.%s.onelogin.com/api/1/login/verify_factor"
    SESSION_API_TOKEN_URL = "https://admin.%s.onelogin.com/session_via_api_token"

    # SAML Assertion URLs
    GET_SAML_ASSERTION_URL = "https://api.%s.onelogin.com/api/1/saml_assertion"
    GET_SAML_VERIFY_FACTOR = "https://api.%s.onelogin.com/api/1/saml_assertion/verify_factor"

    # Multi-Factor Authentication URLs
    GET_FACTORS_URL = "https://api.%s.onelogin.com/api/1/users/%s/auth_factors"
    ENROLL_FACTOR_URL = "https://api.%s.onelogin.com/api/1/users/%s/otp_devices"
    GET_ENROLLED_FACTORS_URL = "https://api.%s.onelogin.com/api/1/users/%s/otp_devices"
    ACTIVATE_FACTOR_URL = "https://api.%s.onelogin.com/api/1/users/%s/otp_devices/%s/trigger"
    VERIFY_FACTOR_URL = "https://api.%s.onelogin.com/api/1/users/%s/otp_devices/%s/verify"
    DELETE_FACTOR_URL = "https://api.%s.onelogin.com/api/1/users/%s/otp_devices/%s"

    # Invite Link URLS
    GENERATE_INVITE_LINK_URL = "https://api.%s.onelogin.com/api/1/invites/get_invite_link"
    SEND_INVITE_LINK_URL = "https://api.%s.onelogin.com/api/1/invites/send_invite_link"

    # Embed Apps URL
    EMBED_APP_URL = "https://api.onelogin.com/client/apps/embed2"
