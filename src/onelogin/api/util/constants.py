# -*- coding: utf-8 -*-

""" Constants class

Copyright (c) 2021, OneLogin, Inc.
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
    GET_USERS_URL = "https://api.%s.onelogin.com/api/%s/users"
    GET_USER_URL = "https://api.%s.onelogin.com/api/%s/users/%s"
    GET_APPS_FOR_USER_URL = "https://api.%s.onelogin.com/api/%s/users/%s/apps"
    GET_ROLES_FOR_USER_URL = "https://api.%s.onelogin.com/api/%s/users/%s/roles"
    GET_CUSTOM_ATTRIBUTES_URL = "https://api.%s.onelogin.com/api/%s/users/custom_attributes"
    CREATE_USER_URL = "https://api.%s.onelogin.com/api/%s/users"
    UPDATE_USER_URL = "https://api.%s.onelogin.com/api/%s/users/%s"
    DELETE_USER_URL = "https://api.%s.onelogin.com/api/%s/users/%s"
    ADD_ROLE_TO_USER_URL = "https://api.%s.onelogin.com/api/%s/users/%s/add_roles"
    DELETE_ROLE_TO_USER_URL = "https://api.%s.onelogin.com/api/%s/users/%s/remove_roles"
    SET_PW_CLEARTEXT = "https://api.%s.onelogin.com/api/%s/users/set_password_clear_text/%s"
    SET_PW_SALT = "https://api.%s.onelogin.com/api/%s/users/set_password_using_salt/%s"
    SET_STATE_TO_USER_URL = "https://api.%s.onelogin.com/api/%s/users/%s/set_state"
    SET_CUSTOM_ATTRIBUTE_TO_USER_URL = "https://api.%s.onelogin.com/api/%s/users/%s/set_custom_attributes"
    LOG_USER_OUT_URL = "https://api.%s.onelogin.com/api/%s/users/%s/logout"
    LOCK_USER_URL = "https://api.%s.onelogin.com/api/%s/users/%s/lock_user"
    GENERATE_MFA_TOKEN_URL = "https://api.%s.onelogin.com/api/%s/users/%s/mfa_token"

    # Apps URL
    GET_APPS_URL = "https://api.%s.onelogin.com/api/%s/apps"

    # Role URLs
    GET_ROLES_URL = "https://api.%s.onelogin.com/api/%s/roles"
    CREATE_ROLE_URL = "https://api.%s.onelogin.com/api/%s/roles"
    GET_ROLE_URL = "https://api.%s.onelogin.com/api/%s/roles/%s"    
    UPDATE_ROLE_URL = "https://api.%s.onelogin.com/api/%s/roles/%s"
    GET_ROLE_APPS_URL = "https://api.%s.onelogin.com/api/%s/roles/%s/apps"
    SET_ROLE_APPS_URL = "https://api.%s.onelogin.com/api/%s/roles/%s/apps"
    GET_ROLE_USERS_URL = "https://api.%s.onelogin.com/api/%s/roles/%s/users"
    ADD_ROLE_USERS_URL = "https://api.%s.onelogin.com/api/%s/roles/%s/users"
    REMOVE_ROLE_USERS_URL = "https://api.%s.onelogin.com/api/%s/roles/%s/users"
    GET_ROLE_ADMINS_URL = "https://api.%s.onelogin.com/api/%s/roles/%s/admins"
    ADD_ROLE_ADMINS_URL = "https://api.%s.onelogin.com/api/%s/roles/%s/admins"
    REMOVE_ROLE_ADMINS_URL = "https://api.%s.onelogin.com/api/%s/roles/%s/admins"
    DELETE_ROLE_URL = "https://api.%s.onelogin.com/api/%s/roles/%s"

    # Event URLS
    GET_EVENT_TYPES_URL = "https://api.%s.onelogin.com/api/%s/events/types"
    GET_EVENTS_URL = "https://api.%s.onelogin.com/api/%s/events"
    CREATE_EVENT_URL = "https://api.%s.onelogin.com/api/%s/events"
    GET_EVENT_URL = "https://api.%s.onelogin.com/api/%s/events/%s"

    # Group URLs
    GET_GROUPS_URL = "https://api.%s.onelogin.com/api/%s/groups"
    CREATE_GROUP_URL = "https://api.%s.onelogin.com/api/%s/groups"
    GET_GROUP_URL = "https://api.%s.onelogin.com/api/%s/groups/%s"

    # Custom Login URLs
    SESSION_LOGIN_TOKEN_URL = "https://api.%s.onelogin.com/api/%s/login/auth"
    GET_TOKEN_VERIFY_FACTOR = "https://api.%s.onelogin.com/api/%s/login/verify_factor"
    
    # SAML Assertion URLs
    GET_SAML_ASSERTION_URL = "https://api.%s.onelogin.com/api/%s/saml_assertion"
    GET_SAML_VERIFY_FACTOR = "https://api.%s.onelogin.com/api/%s/saml_assertion/verify_factor"

    # Multi-Factor Authentication URLs
    GET_FACTORS_URL = "https://api.%s.onelogin.com/api/%s/users/%s/auth_factors"
    ENROLL_FACTOR_URL = "https://api.%s.onelogin.com/api/%s/users/%s/otp_devices"
    GET_ENROLLED_FACTORS_URL = "https://api.%s.onelogin.com/api/%s/users/%s/otp_devices"
    ACTIVATE_FACTOR_URL = "https://api.%s.onelogin.com/api/%s/users/%s/otp_devices/%s/trigger"
    VERIFY_FACTOR_URL = "https://api.%s.onelogin.com/api/%s/users/%s/otp_devices/%s/verify"
    DELETE_FACTOR_URL = "https://api.%s.onelogin.com/api/%s/users/%s/otp_devices/%s"

    # Invite Link URLS
    GENERATE_INVITE_LINK_URL = "https://api.%s.onelogin.com/api/%s/invites/get_invite_link"
    SEND_INVITE_LINK_URL = "https://api.%s.onelogin.com/api/%s/invites/send_invite_link"

    # Embed Apps URL
    EMBED_APP_URL = "https://api.onelogin.com/client/apps/embed2"

    # Privileges URLS
    LIST_PRIVILEGES_URL = "https://api.%s.onelogin.com/api/%s/privileges"
    CREATE_PRIVILEGE_URL = "https://api.%s.onelogin.com/api/%s/privileges"
    UPDATE_PRIVILEGE_URL = "https://api.%s.onelogin.com/api/%s/privileges/%s"
    GET_PRIVILEGE_URL = "https://api.%s.onelogin.com/api/%s/privileges/%s"
    DELETE_PRIVILEGE_URL = "https://api.%s.onelogin.com/api/%s/privileges/%s"
    GET_ROLES_ASSIGNED_TO_PRIVILEGE_URL = "https://api.%s.onelogin.com/api/%s/privileges/%s/roles"
    ASSIGN_ROLES_TO_PRIVILEGE_URL = "https://api.%s.onelogin.com/api/%s/privileges/%s/roles"
    REMOVE_ROLE_FROM_PRIVILEGE_URL = "https://api.%s.onelogin.com/api/%s/privileges/%s/roles/%s"
    GET_USERS_ASSIGNED_TO_PRIVILEGE_URL = "https://api.%s.onelogin.com/api/%s/privileges/%s/users"
    ASSIGN_USERS_TO_PRIVILEGE_URL = "https://api.%s.onelogin.com/api/%s/privileges/%s/users"
    REMOVE_USER_FROM_PRIVILEGE_URL = "https://api.%s.onelogin.com/api/%s/privileges/%s/users/%s"
    VALID_ACTIONS = [
        "apps:List",
        "apps:Get",
        "apps:Create",
        "apps:Update",
        "apps:Delete",
        "apps:ManageRoles",
        "apps:ManageUsers",
        "directories:List",
        "directories:Get",
        "directories:Create",
        "directories:Update",
        "directories:Delete",
        "directories:SyncUsers",
        "directories:RefreshSchema",
        "events:List",
        "events:Get",
        "mappings:List",
        "mappings:Get",
        "mappings:Create",
        "mappings:Update",
        "mappings:Delete",
        "mappings:ReapplyAll",
        "policies:List",
        "policies:user:Get",
        "policies:user:Create",
        "policies:user:Update",
        "policies:user:Delete",
        "policies:app:Get",
        "policies:app:Create",
        "policies:app:Update",
        "policies:app:Delete",
        "privileges:List",
        "privileges:Get",
        "privileges:Create",
        "privileges:Update",
        "privileges:Delete",
        "privileges:ListUsers",
        "privileges:ListRoles",
        "privileges:ManageUsers",
        "privileges:ManageRoles",
        "reports:List",
        "reports:Get",
        "reports:Create",
        "reports:Update",
        "reports:Delete",
        "reports:Run",
        "roles:List",
        "roles:Get",
        "roles:Create",
        "roles:Update",
        "roles:Delete",
        "roles:ManageUsers",
        "roles:ManageApps",
        "trustedidp:List",
        "trustedidp:Get",
        "trustedidp:Create",
        "trustedidp:Update",
        "trustedidp:Delete",
        "users:List",
        "users:Get",
        "users:Create",
        "users:Update",
        "users:Delete",
        "users:Unlock",
        "users:ResetPassword",
        "users:ForceLogout",
        "users:Invite",
        "users:ReapplyMappings",
        "users:ManageRoles",
        "users:ManageApps",
        "users:GenerateTempMfaToken"
    ]
