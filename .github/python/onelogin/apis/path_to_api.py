import typing_extensions

from onelogin.paths import PathValues
from onelogin.apis.paths.auth_oauth2_v2_token import AuthOauth2V2Token
from onelogin.apis.paths.auth_oauth2_revoke import AuthOauth2Revoke
from onelogin.apis.paths.auth_rate_limit import AuthRateLimit
from onelogin.apis.paths.api_2_api_authorizations import Api2ApiAuthorizations
from onelogin.apis.paths.api_2_api_authorizations_api_auth_id import Api2ApiAuthorizationsApiAuthId
from onelogin.apis.paths.api_2_api_authorizations_api_auth_id_scopes import Api2ApiAuthorizationsApiAuthIdScopes
from onelogin.apis.paths.api_2_api_authorizations_api_auth_id_scopes_scope_id import Api2ApiAuthorizationsApiAuthIdScopesScopeId
from onelogin.apis.paths.api_2_api_authorizations_api_auth_id_claims import Api2ApiAuthorizationsApiAuthIdClaims
from onelogin.apis.paths.api_2_api_authorizations_api_auth_id_claims_claim_id import Api2ApiAuthorizationsApiAuthIdClaimsClaimId
from onelogin.apis.paths.api_2_api_authorizations_api_auth_id_clients import Api2ApiAuthorizationsApiAuthIdClients
from onelogin.apis.paths.api_2_api_authorizations_api_auth_id_clients_client_app_id import Api2ApiAuthorizationsApiAuthIdClientsClientAppId
from onelogin.apis.paths.api_1_events import Api1Events
from onelogin.apis.paths.api_1_events_event_id import Api1EventsEventId
from onelogin.apis.paths.api_1_events_types import Api1EventsTypes
from onelogin.apis.paths.api_1_groups import Api1Groups
from onelogin.apis.paths.api_1_groups_group_id import Api1GroupsGroupId
from onelogin.apis.paths.api_1_invites_get_invite_link import Api1InvitesGetInviteLink
from onelogin.apis.paths.api_1_invites_send_invite_link import Api1InvitesSendInviteLink
from onelogin.apis.paths.api_1_users import Api1Users
from onelogin.apis.paths.api_1_users_user_id import Api1UsersUserId
from onelogin.apis.paths.api_1_users_user_id_apps import Api1UsersUserIdApps
from onelogin.apis.paths.api_1_users_user_id_roles import Api1UsersUserIdRoles
from onelogin.apis.paths.api_1_users_set_password_clear_text_user_id import Api1UsersSetPasswordClearTextUserId
from onelogin.apis.paths.api_1_users_set_password_using_salt_user_id import Api1UsersSetPasswordUsingSaltUserId
from onelogin.apis.paths.api_1_users_custom_attributes import Api1UsersCustomAttributes
from onelogin.apis.paths.api_1_users_user_id_auth_factor import Api1UsersUserIdAuthFactor
from onelogin.apis.paths.api_1_users_user_id_logout import Api1UsersUserIdLogout
from onelogin.apis.paths.api_1_users_user_id_lock_user import Api1UsersUserIdLockUser
from onelogin.apis.paths.api_1_users_user_id_otp_devices import Api1UsersUserIdOtpDevices
from onelogin.apis.paths.api_1_users_user_id_mfa_token import Api1UsersUserIdMfaToken
from onelogin.apis.paths.api_1_users_user_id_add_roles import Api1UsersUserIdAddRoles
from onelogin.apis.paths.api_1_users_user_id_set_state import Api1UsersUserIdSetState
from onelogin.apis.paths.api_1_users_user_id_remove_roles import Api1UsersUserIdRemoveRoles
from onelogin.apis.paths.api_1_users_user_id_otp_devices_device_id import Api1UsersUserIdOtpDevicesDeviceId
from onelogin.apis.paths.api_1_users_user_id_otp_devices_device_id_verify import Api1UsersUserIdOtpDevicesDeviceIdVerify
from onelogin.apis.paths.api_1_users_user_id_otp_devices_device_id_trigger import Api1UsersUserIdOtpDevicesDeviceIdTrigger
from onelogin.apis.paths.api_1_privileges import Api1Privileges
from onelogin.apis.paths.api_1_privileges_privilege_id import Api1PrivilegesPrivilegeId
from onelogin.apis.paths.api_1_privileges_privilege_id_roles import Api1PrivilegesPrivilegeIdRoles
from onelogin.apis.paths.api_1_privileges_privilege_id_roles_role_id import Api1PrivilegesPrivilegeIdRolesRoleId
from onelogin.apis.paths.api_1_privileges_privilege_id_users import Api1PrivilegesPrivilegeIdUsers
from onelogin.apis.paths.api_1_privileges_privilege_id_users_user_id import Api1PrivilegesPrivilegeIdUsersUserId
from onelogin.apis.paths.api_1_roles import Api1Roles
from onelogin.apis.paths.api_1_roles_role_id import Api1RolesRoleId
from onelogin.apis.paths.api_1_saml_assertion import Api1SamlAssertion
from onelogin.apis.paths.api_1_saml_assertion_verify_factor import Api1SamlAssertionVerifyFactor
from onelogin.apis.paths.api_2_saml_assertion import Api2SamlAssertion
from onelogin.apis.paths.api_2_saml_assertion_verify_factor import Api2SamlAssertionVerifyFactor
from onelogin.apis.paths.api_2_mappings import Api2Mappings
from onelogin.apis.paths.api_2_mappings_mapping_id import Api2MappingsMappingId
from onelogin.apis.paths.api_2_mappings_conditions import Api2MappingsConditions
from onelogin.apis.paths.api_2_mappings_conditions_mapping_condition_value_operators import Api2MappingsConditionsMappingConditionValueOperators
from onelogin.apis.paths.api_2_mappings_conditions_mapping_condition_value_values import Api2MappingsConditionsMappingConditionValueValues
from onelogin.apis.paths.api_2_mappings_actions import Api2MappingsActions
from onelogin.apis.paths.api_2_mappings_actions_mapping_action_value_values import Api2MappingsActionsMappingActionValueValues
from onelogin.apis.paths.api_2_mappings_sort import Api2MappingsSort
from onelogin.apis.paths.api_2_apps import Api2Apps
from onelogin.apis.paths.api_2_apps_app_id import Api2AppsAppId
from onelogin.apis.paths.api_2_apps_app_id_parameters_parameter_id import Api2AppsAppIdParametersParameterId
from onelogin.apis.paths.api_2_apps_app_id_users import Api2AppsAppIdUsers
from onelogin.apis.paths.api_2_apps_app_id_rules import Api2AppsAppIdRules
from onelogin.apis.paths.api_2_apps_app_id_rules_rule_id import Api2AppsAppIdRulesRuleId
from onelogin.apis.paths.api_2_apps_app_id_rules_conditions import Api2AppsAppIdRulesConditions
from onelogin.apis.paths.api_2_apps_app_id_rules_conditions_rule_condition_value_operators import Api2AppsAppIdRulesConditionsRuleConditionValueOperators
from onelogin.apis.paths.api_2_apps_app_id_rules_conditions_rule_condition_value_values import Api2AppsAppIdRulesConditionsRuleConditionValueValues
from onelogin.apis.paths.api_2_apps_app_id_rules_actions import Api2AppsAppIdRulesActions
from onelogin.apis.paths.api_2_apps_app_id_rules_actions_rule_action_value_values import Api2AppsAppIdRulesActionsRuleActionValueValues
from onelogin.apis.paths.api_2_apps_app_id_rules_sort import Api2AppsAppIdRulesSort
from onelogin.apis.paths.api_2_connectors import Api2Connectors
from onelogin.apis.paths.api_2_risk_rules import Api2RiskRules
from onelogin.apis.paths.api_2_risk_rules_rule_id import Api2RiskRulesRuleId
from onelogin.apis.paths.api_2_risk_events import Api2RiskEvents
from onelogin.apis.paths.api_2_risk_scores import Api2RiskScores
from onelogin.apis.paths.api_2_risk_verify import Api2RiskVerify
from onelogin.apis.paths.api_2_mfa_users_user_id_registrations_registration_id import Api2MfaUsersUserIdRegistrationsRegistrationId
from onelogin.apis.paths.api_2_mfa_users_user_id_registrations import Api2MfaUsersUserIdRegistrations
from onelogin.apis.paths.api_2_mfa_users_user_id_devices import Api2MfaUsersUserIdDevices
from onelogin.apis.paths.api_2_mfa_users_user_id_devices_device_id import Api2MfaUsersUserIdDevicesDeviceId
from onelogin.apis.paths.api_2_mfa_users_user_id_verifications_verification_id import Api2MfaUsersUserIdVerificationsVerificationId
from onelogin.apis.paths.api_2_mfa_users_user_id_verifications import Api2MfaUsersUserIdVerifications
from onelogin.apis.paths.api_2_mfa_users_user_id_factors import Api2MfaUsersUserIdFactors
from onelogin.apis.paths.api_2_mfa_users_user_id_mfa_token import Api2MfaUsersUserIdMfaToken
from onelogin.apis.paths.api_2_roles import Api2Roles
from onelogin.apis.paths.api_2_roles_role_id import Api2RolesRoleId
from onelogin.apis.paths.api_2_roles_role_id_apps import Api2RolesRoleIdApps
from onelogin.apis.paths.api_2_roles_role_id_users import Api2RolesRoleIdUsers
from onelogin.apis.paths.api_2_roles_role_id_admins import Api2RolesRoleIdAdmins
from onelogin.apis.paths.api_2_hooks import Api2Hooks
from onelogin.apis.paths.api_2_hooks_hook_id import Api2HooksHookId
from onelogin.apis.paths.api_2_hooks_hook_id_logs import Api2HooksHookIdLogs
from onelogin.apis.paths.api_2_hooks_envs import Api2HooksEnvs
from onelogin.apis.paths.api_2_hooks_envs_envvar_id import Api2HooksEnvsEnvvarId
from onelogin.apis.paths.api_2_users import Api2Users
from onelogin.apis.paths.api_2_users_user_id import Api2UsersUserId
from onelogin.apis.paths.api_2_users_user_id_apps import Api2UsersUserIdApps
from onelogin.apis.paths.api_2_branding_brands import Api2BrandingBrands
from onelogin.apis.paths.api_2_branding_brands_brand_id import Api2BrandingBrandsBrandId
from onelogin.apis.paths.api_2_branding_brands_brand_id_templates import Api2BrandingBrandsBrandIdTemplates
from onelogin.apis.paths.api_2_branding_brands_brand_id_templates_template_id import Api2BrandingBrandsBrandIdTemplatesTemplateId
from onelogin.apis.paths.api_2_branding_brands_brand_id_apps import Api2BrandingBrandsBrandIdApps
from onelogin.apis.paths.api_2_branding_email_settings import Api2BrandingEmailSettings
from onelogin.apis.paths.api_2_branding_brands_brand_id_templates_template_type_locale import Api2BrandingBrandsBrandIdTemplatesTemplateTypeLocale
from onelogin.apis.paths.api_2_branding_brands_master_templates_template_type import Api2BrandingBrandsMasterTemplatesTemplateType

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.AUTH_OAUTH2_V2_TOKEN: AuthOauth2V2Token,
        PathValues.AUTH_OAUTH2_REVOKE: AuthOauth2Revoke,
        PathValues.AUTH_RATE_LIMIT: AuthRateLimit,
        PathValues.API_2_API_AUTHORIZATIONS: Api2ApiAuthorizations,
        PathValues.API_2_API_AUTHORIZATIONS_API_AUTH_ID: Api2ApiAuthorizationsApiAuthId,
        PathValues.API_2_API_AUTHORIZATIONS_API_AUTH_ID_SCOPES: Api2ApiAuthorizationsApiAuthIdScopes,
        PathValues.API_2_API_AUTHORIZATIONS_API_AUTH_ID_SCOPES_SCOPE_ID: Api2ApiAuthorizationsApiAuthIdScopesScopeId,
        PathValues.API_2_API_AUTHORIZATIONS_API_AUTH_ID_CLAIMS: Api2ApiAuthorizationsApiAuthIdClaims,
        PathValues.API_2_API_AUTHORIZATIONS_API_AUTH_ID_CLAIMS_CLAIM_ID: Api2ApiAuthorizationsApiAuthIdClaimsClaimId,
        PathValues.API_2_API_AUTHORIZATIONS_API_AUTH_ID_CLIENTS: Api2ApiAuthorizationsApiAuthIdClients,
        PathValues.API_2_API_AUTHORIZATIONS_API_AUTH_ID_CLIENTS_CLIENT_APP_ID: Api2ApiAuthorizationsApiAuthIdClientsClientAppId,
        PathValues.API_1_EVENTS: Api1Events,
        PathValues.API_1_EVENTS_EVENT_ID: Api1EventsEventId,
        PathValues.API_1_EVENTS_TYPES: Api1EventsTypes,
        PathValues.API_1_GROUPS: Api1Groups,
        PathValues.API_1_GROUPS_GROUP_ID: Api1GroupsGroupId,
        PathValues.API_1_INVITES_GET_INVITE_LINK: Api1InvitesGetInviteLink,
        PathValues.API_1_INVITES_SEND_INVITE_LINK: Api1InvitesSendInviteLink,
        PathValues.API_1_USERS: Api1Users,
        PathValues.API_1_USERS_USER_ID: Api1UsersUserId,
        PathValues.API_1_USERS_USER_ID_APPS: Api1UsersUserIdApps,
        PathValues.API_1_USERS_USER_ID_ROLES: Api1UsersUserIdRoles,
        PathValues.API_1_USERS_SET_PASSWORD_CLEAR_TEXT_USER_ID: Api1UsersSetPasswordClearTextUserId,
        PathValues.API_1_USERS_SET_PASSWORD_USING_SALT_USER_ID: Api1UsersSetPasswordUsingSaltUserId,
        PathValues.API_1_USERS_CUSTOM_ATTRIBUTES: Api1UsersCustomAttributes,
        PathValues.API_1_USERS_USER_ID_AUTH_FACTOR: Api1UsersUserIdAuthFactor,
        PathValues.API_1_USERS_USER_ID_LOGOUT: Api1UsersUserIdLogout,
        PathValues.API_1_USERS_USER_ID_LOCK_USER: Api1UsersUserIdLockUser,
        PathValues.API_1_USERS_USER_ID_OTP_DEVICES: Api1UsersUserIdOtpDevices,
        PathValues.API_1_USERS_USER_ID_MFA_TOKEN: Api1UsersUserIdMfaToken,
        PathValues.API_1_USERS_USER_ID_ADD_ROLES: Api1UsersUserIdAddRoles,
        PathValues.API_1_USERS_USER_ID_SET_STATE: Api1UsersUserIdSetState,
        PathValues.API_1_USERS_USER_ID_REMOVE_ROLES: Api1UsersUserIdRemoveRoles,
        PathValues.API_1_USERS_USER_ID_OTP_DEVICES_DEVICE_ID: Api1UsersUserIdOtpDevicesDeviceId,
        PathValues.API_1_USERS_USER_ID_OTP_DEVICES_DEVICE_ID_VERIFY: Api1UsersUserIdOtpDevicesDeviceIdVerify,
        PathValues.API_1_USERS_USER_ID_OTP_DEVICES_DEVICE_ID_TRIGGER: Api1UsersUserIdOtpDevicesDeviceIdTrigger,
        PathValues.API_1_PRIVILEGES: Api1Privileges,
        PathValues.API_1_PRIVILEGES_PRIVILEGE_ID: Api1PrivilegesPrivilegeId,
        PathValues.API_1_PRIVILEGES_PRIVILEGE_ID_ROLES: Api1PrivilegesPrivilegeIdRoles,
        PathValues.API_1_PRIVILEGES_PRIVILEGE_ID_ROLES_ROLE_ID: Api1PrivilegesPrivilegeIdRolesRoleId,
        PathValues.API_1_PRIVILEGES_PRIVILEGE_ID_USERS: Api1PrivilegesPrivilegeIdUsers,
        PathValues.API_1_PRIVILEGES_PRIVILEGE_ID_USERS_USER_ID: Api1PrivilegesPrivilegeIdUsersUserId,
        PathValues.API_1_ROLES: Api1Roles,
        PathValues.API_1_ROLES_ROLE_ID: Api1RolesRoleId,
        PathValues.API_1_SAML_ASSERTION: Api1SamlAssertion,
        PathValues.API_1_SAML_ASSERTION_VERIFY_FACTOR: Api1SamlAssertionVerifyFactor,
        PathValues.API_2_SAML_ASSERTION: Api2SamlAssertion,
        PathValues.API_2_SAML_ASSERTION_VERIFY_FACTOR: Api2SamlAssertionVerifyFactor,
        PathValues.API_2_MAPPINGS: Api2Mappings,
        PathValues.API_2_MAPPINGS_MAPPING_ID: Api2MappingsMappingId,
        PathValues.API_2_MAPPINGS_CONDITIONS: Api2MappingsConditions,
        PathValues.API_2_MAPPINGS_CONDITIONS_MAPPING_CONDITION_VALUE_OPERATORS: Api2MappingsConditionsMappingConditionValueOperators,
        PathValues.API_2_MAPPINGS_CONDITIONS_MAPPING_CONDITION_VALUE_VALUES: Api2MappingsConditionsMappingConditionValueValues,
        PathValues.API_2_MAPPINGS_ACTIONS: Api2MappingsActions,
        PathValues.API_2_MAPPINGS_ACTIONS_MAPPING_ACTION_VALUE_VALUES: Api2MappingsActionsMappingActionValueValues,
        PathValues.API_2_MAPPINGS_SORT: Api2MappingsSort,
        PathValues.API_2_APPS: Api2Apps,
        PathValues.API_2_APPS_APP_ID: Api2AppsAppId,
        PathValues.API_2_APPS_APP_ID_PARAMETERS_PARAMETER_ID: Api2AppsAppIdParametersParameterId,
        PathValues.API_2_APPS_APP_ID_USERS: Api2AppsAppIdUsers,
        PathValues.API_2_APPS_APP_ID_RULES: Api2AppsAppIdRules,
        PathValues.API_2_APPS_APP_ID_RULES_RULE_ID: Api2AppsAppIdRulesRuleId,
        PathValues.API_2_APPS_APP_ID_RULES_CONDITIONS: Api2AppsAppIdRulesConditions,
        PathValues.API_2_APPS_APP_ID_RULES_CONDITIONS_RULE_CONDITION_VALUE_OPERATORS: Api2AppsAppIdRulesConditionsRuleConditionValueOperators,
        PathValues.API_2_APPS_APP_ID_RULES_CONDITIONS_RULE_CONDITION_VALUE_VALUES: Api2AppsAppIdRulesConditionsRuleConditionValueValues,
        PathValues.API_2_APPS_APP_ID_RULES_ACTIONS: Api2AppsAppIdRulesActions,
        PathValues.API_2_APPS_APP_ID_RULES_ACTIONS_RULE_ACTION_VALUE_VALUES: Api2AppsAppIdRulesActionsRuleActionValueValues,
        PathValues.API_2_APPS_APP_ID_RULES_SORT: Api2AppsAppIdRulesSort,
        PathValues.API_2_CONNECTORS: Api2Connectors,
        PathValues.API_2_RISK_RULES: Api2RiskRules,
        PathValues.API_2_RISK_RULES_RULE_ID: Api2RiskRulesRuleId,
        PathValues.API_2_RISK_EVENTS: Api2RiskEvents,
        PathValues.API_2_RISK_SCORES: Api2RiskScores,
        PathValues.API_2_RISK_VERIFY: Api2RiskVerify,
        PathValues.API_2_MFA_USERS_USER_ID_REGISTRATIONS_REGISTRATION_ID: Api2MfaUsersUserIdRegistrationsRegistrationId,
        PathValues.API_2_MFA_USERS_USER_ID_REGISTRATIONS: Api2MfaUsersUserIdRegistrations,
        PathValues.API_2_MFA_USERS_USER_ID_DEVICES: Api2MfaUsersUserIdDevices,
        PathValues.API_2_MFA_USERS_USER_ID_DEVICES_DEVICE_ID: Api2MfaUsersUserIdDevicesDeviceId,
        PathValues.API_2_MFA_USERS_USER_ID_VERIFICATIONS_VERIFICATION_ID: Api2MfaUsersUserIdVerificationsVerificationId,
        PathValues.API_2_MFA_USERS_USER_ID_VERIFICATIONS: Api2MfaUsersUserIdVerifications,
        PathValues.API_2_MFA_USERS_USER_ID_FACTORS: Api2MfaUsersUserIdFactors,
        PathValues.API_2_MFA_USERS_USER_ID_MFA_TOKEN: Api2MfaUsersUserIdMfaToken,
        PathValues.API_2_ROLES: Api2Roles,
        PathValues.API_2_ROLES_ROLE_ID: Api2RolesRoleId,
        PathValues.API_2_ROLES_ROLE_ID_APPS: Api2RolesRoleIdApps,
        PathValues.API_2_ROLES_ROLE_ID_USERS: Api2RolesRoleIdUsers,
        PathValues.API_2_ROLES_ROLE_ID_ADMINS: Api2RolesRoleIdAdmins,
        PathValues.API_2_HOOKS: Api2Hooks,
        PathValues.API_2_HOOKS_HOOK_ID: Api2HooksHookId,
        PathValues.API_2_HOOKS_HOOK_ID_LOGS: Api2HooksHookIdLogs,
        PathValues.API_2_HOOKS_ENVS: Api2HooksEnvs,
        PathValues.API_2_HOOKS_ENVS_ENVVAR_ID: Api2HooksEnvsEnvvarId,
        PathValues.API_2_USERS: Api2Users,
        PathValues.API_2_USERS_USER_ID: Api2UsersUserId,
        PathValues.API_2_USERS_USER_ID_APPS: Api2UsersUserIdApps,
        PathValues.API_2_BRANDING_BRANDS: Api2BrandingBrands,
        PathValues.API_2_BRANDING_BRANDS_BRAND_ID: Api2BrandingBrandsBrandId,
        PathValues.API_2_BRANDING_BRANDS_BRAND_ID_TEMPLATES: Api2BrandingBrandsBrandIdTemplates,
        PathValues.API_2_BRANDING_BRANDS_BRAND_ID_TEMPLATES_TEMPLATE_ID: Api2BrandingBrandsBrandIdTemplatesTemplateId,
        PathValues.API_2_BRANDING_BRANDS_BRAND_ID_APPS: Api2BrandingBrandsBrandIdApps,
        PathValues.API_2_BRANDING_EMAIL_SETTINGS: Api2BrandingEmailSettings,
        PathValues.API_2_BRANDING_BRANDS_BRAND_ID_TEMPLATES_TEMPLATE_TYPE_LOCALE: Api2BrandingBrandsBrandIdTemplatesTemplateTypeLocale,
        PathValues.API_2_BRANDING_BRANDS_MASTER_TEMPLATES_TEMPLATE_TYPE: Api2BrandingBrandsMasterTemplatesTemplateType,
    }
)

path_to_api = PathToApi(
    {
        PathValues.AUTH_OAUTH2_V2_TOKEN: AuthOauth2V2Token,
        PathValues.AUTH_OAUTH2_REVOKE: AuthOauth2Revoke,
        PathValues.AUTH_RATE_LIMIT: AuthRateLimit,
        PathValues.API_2_API_AUTHORIZATIONS: Api2ApiAuthorizations,
        PathValues.API_2_API_AUTHORIZATIONS_API_AUTH_ID: Api2ApiAuthorizationsApiAuthId,
        PathValues.API_2_API_AUTHORIZATIONS_API_AUTH_ID_SCOPES: Api2ApiAuthorizationsApiAuthIdScopes,
        PathValues.API_2_API_AUTHORIZATIONS_API_AUTH_ID_SCOPES_SCOPE_ID: Api2ApiAuthorizationsApiAuthIdScopesScopeId,
        PathValues.API_2_API_AUTHORIZATIONS_API_AUTH_ID_CLAIMS: Api2ApiAuthorizationsApiAuthIdClaims,
        PathValues.API_2_API_AUTHORIZATIONS_API_AUTH_ID_CLAIMS_CLAIM_ID: Api2ApiAuthorizationsApiAuthIdClaimsClaimId,
        PathValues.API_2_API_AUTHORIZATIONS_API_AUTH_ID_CLIENTS: Api2ApiAuthorizationsApiAuthIdClients,
        PathValues.API_2_API_AUTHORIZATIONS_API_AUTH_ID_CLIENTS_CLIENT_APP_ID: Api2ApiAuthorizationsApiAuthIdClientsClientAppId,
        PathValues.API_1_EVENTS: Api1Events,
        PathValues.API_1_EVENTS_EVENT_ID: Api1EventsEventId,
        PathValues.API_1_EVENTS_TYPES: Api1EventsTypes,
        PathValues.API_1_GROUPS: Api1Groups,
        PathValues.API_1_GROUPS_GROUP_ID: Api1GroupsGroupId,
        PathValues.API_1_INVITES_GET_INVITE_LINK: Api1InvitesGetInviteLink,
        PathValues.API_1_INVITES_SEND_INVITE_LINK: Api1InvitesSendInviteLink,
        PathValues.API_1_USERS: Api1Users,
        PathValues.API_1_USERS_USER_ID: Api1UsersUserId,
        PathValues.API_1_USERS_USER_ID_APPS: Api1UsersUserIdApps,
        PathValues.API_1_USERS_USER_ID_ROLES: Api1UsersUserIdRoles,
        PathValues.API_1_USERS_SET_PASSWORD_CLEAR_TEXT_USER_ID: Api1UsersSetPasswordClearTextUserId,
        PathValues.API_1_USERS_SET_PASSWORD_USING_SALT_USER_ID: Api1UsersSetPasswordUsingSaltUserId,
        PathValues.API_1_USERS_CUSTOM_ATTRIBUTES: Api1UsersCustomAttributes,
        PathValues.API_1_USERS_USER_ID_AUTH_FACTOR: Api1UsersUserIdAuthFactor,
        PathValues.API_1_USERS_USER_ID_LOGOUT: Api1UsersUserIdLogout,
        PathValues.API_1_USERS_USER_ID_LOCK_USER: Api1UsersUserIdLockUser,
        PathValues.API_1_USERS_USER_ID_OTP_DEVICES: Api1UsersUserIdOtpDevices,
        PathValues.API_1_USERS_USER_ID_MFA_TOKEN: Api1UsersUserIdMfaToken,
        PathValues.API_1_USERS_USER_ID_ADD_ROLES: Api1UsersUserIdAddRoles,
        PathValues.API_1_USERS_USER_ID_SET_STATE: Api1UsersUserIdSetState,
        PathValues.API_1_USERS_USER_ID_REMOVE_ROLES: Api1UsersUserIdRemoveRoles,
        PathValues.API_1_USERS_USER_ID_OTP_DEVICES_DEVICE_ID: Api1UsersUserIdOtpDevicesDeviceId,
        PathValues.API_1_USERS_USER_ID_OTP_DEVICES_DEVICE_ID_VERIFY: Api1UsersUserIdOtpDevicesDeviceIdVerify,
        PathValues.API_1_USERS_USER_ID_OTP_DEVICES_DEVICE_ID_TRIGGER: Api1UsersUserIdOtpDevicesDeviceIdTrigger,
        PathValues.API_1_PRIVILEGES: Api1Privileges,
        PathValues.API_1_PRIVILEGES_PRIVILEGE_ID: Api1PrivilegesPrivilegeId,
        PathValues.API_1_PRIVILEGES_PRIVILEGE_ID_ROLES: Api1PrivilegesPrivilegeIdRoles,
        PathValues.API_1_PRIVILEGES_PRIVILEGE_ID_ROLES_ROLE_ID: Api1PrivilegesPrivilegeIdRolesRoleId,
        PathValues.API_1_PRIVILEGES_PRIVILEGE_ID_USERS: Api1PrivilegesPrivilegeIdUsers,
        PathValues.API_1_PRIVILEGES_PRIVILEGE_ID_USERS_USER_ID: Api1PrivilegesPrivilegeIdUsersUserId,
        PathValues.API_1_ROLES: Api1Roles,
        PathValues.API_1_ROLES_ROLE_ID: Api1RolesRoleId,
        PathValues.API_1_SAML_ASSERTION: Api1SamlAssertion,
        PathValues.API_1_SAML_ASSERTION_VERIFY_FACTOR: Api1SamlAssertionVerifyFactor,
        PathValues.API_2_SAML_ASSERTION: Api2SamlAssertion,
        PathValues.API_2_SAML_ASSERTION_VERIFY_FACTOR: Api2SamlAssertionVerifyFactor,
        PathValues.API_2_MAPPINGS: Api2Mappings,
        PathValues.API_2_MAPPINGS_MAPPING_ID: Api2MappingsMappingId,
        PathValues.API_2_MAPPINGS_CONDITIONS: Api2MappingsConditions,
        PathValues.API_2_MAPPINGS_CONDITIONS_MAPPING_CONDITION_VALUE_OPERATORS: Api2MappingsConditionsMappingConditionValueOperators,
        PathValues.API_2_MAPPINGS_CONDITIONS_MAPPING_CONDITION_VALUE_VALUES: Api2MappingsConditionsMappingConditionValueValues,
        PathValues.API_2_MAPPINGS_ACTIONS: Api2MappingsActions,
        PathValues.API_2_MAPPINGS_ACTIONS_MAPPING_ACTION_VALUE_VALUES: Api2MappingsActionsMappingActionValueValues,
        PathValues.API_2_MAPPINGS_SORT: Api2MappingsSort,
        PathValues.API_2_APPS: Api2Apps,
        PathValues.API_2_APPS_APP_ID: Api2AppsAppId,
        PathValues.API_2_APPS_APP_ID_PARAMETERS_PARAMETER_ID: Api2AppsAppIdParametersParameterId,
        PathValues.API_2_APPS_APP_ID_USERS: Api2AppsAppIdUsers,
        PathValues.API_2_APPS_APP_ID_RULES: Api2AppsAppIdRules,
        PathValues.API_2_APPS_APP_ID_RULES_RULE_ID: Api2AppsAppIdRulesRuleId,
        PathValues.API_2_APPS_APP_ID_RULES_CONDITIONS: Api2AppsAppIdRulesConditions,
        PathValues.API_2_APPS_APP_ID_RULES_CONDITIONS_RULE_CONDITION_VALUE_OPERATORS: Api2AppsAppIdRulesConditionsRuleConditionValueOperators,
        PathValues.API_2_APPS_APP_ID_RULES_CONDITIONS_RULE_CONDITION_VALUE_VALUES: Api2AppsAppIdRulesConditionsRuleConditionValueValues,
        PathValues.API_2_APPS_APP_ID_RULES_ACTIONS: Api2AppsAppIdRulesActions,
        PathValues.API_2_APPS_APP_ID_RULES_ACTIONS_RULE_ACTION_VALUE_VALUES: Api2AppsAppIdRulesActionsRuleActionValueValues,
        PathValues.API_2_APPS_APP_ID_RULES_SORT: Api2AppsAppIdRulesSort,
        PathValues.API_2_CONNECTORS: Api2Connectors,
        PathValues.API_2_RISK_RULES: Api2RiskRules,
        PathValues.API_2_RISK_RULES_RULE_ID: Api2RiskRulesRuleId,
        PathValues.API_2_RISK_EVENTS: Api2RiskEvents,
        PathValues.API_2_RISK_SCORES: Api2RiskScores,
        PathValues.API_2_RISK_VERIFY: Api2RiskVerify,
        PathValues.API_2_MFA_USERS_USER_ID_REGISTRATIONS_REGISTRATION_ID: Api2MfaUsersUserIdRegistrationsRegistrationId,
        PathValues.API_2_MFA_USERS_USER_ID_REGISTRATIONS: Api2MfaUsersUserIdRegistrations,
        PathValues.API_2_MFA_USERS_USER_ID_DEVICES: Api2MfaUsersUserIdDevices,
        PathValues.API_2_MFA_USERS_USER_ID_DEVICES_DEVICE_ID: Api2MfaUsersUserIdDevicesDeviceId,
        PathValues.API_2_MFA_USERS_USER_ID_VERIFICATIONS_VERIFICATION_ID: Api2MfaUsersUserIdVerificationsVerificationId,
        PathValues.API_2_MFA_USERS_USER_ID_VERIFICATIONS: Api2MfaUsersUserIdVerifications,
        PathValues.API_2_MFA_USERS_USER_ID_FACTORS: Api2MfaUsersUserIdFactors,
        PathValues.API_2_MFA_USERS_USER_ID_MFA_TOKEN: Api2MfaUsersUserIdMfaToken,
        PathValues.API_2_ROLES: Api2Roles,
        PathValues.API_2_ROLES_ROLE_ID: Api2RolesRoleId,
        PathValues.API_2_ROLES_ROLE_ID_APPS: Api2RolesRoleIdApps,
        PathValues.API_2_ROLES_ROLE_ID_USERS: Api2RolesRoleIdUsers,
        PathValues.API_2_ROLES_ROLE_ID_ADMINS: Api2RolesRoleIdAdmins,
        PathValues.API_2_HOOKS: Api2Hooks,
        PathValues.API_2_HOOKS_HOOK_ID: Api2HooksHookId,
        PathValues.API_2_HOOKS_HOOK_ID_LOGS: Api2HooksHookIdLogs,
        PathValues.API_2_HOOKS_ENVS: Api2HooksEnvs,
        PathValues.API_2_HOOKS_ENVS_ENVVAR_ID: Api2HooksEnvsEnvvarId,
        PathValues.API_2_USERS: Api2Users,
        PathValues.API_2_USERS_USER_ID: Api2UsersUserId,
        PathValues.API_2_USERS_USER_ID_APPS: Api2UsersUserIdApps,
        PathValues.API_2_BRANDING_BRANDS: Api2BrandingBrands,
        PathValues.API_2_BRANDING_BRANDS_BRAND_ID: Api2BrandingBrandsBrandId,
        PathValues.API_2_BRANDING_BRANDS_BRAND_ID_TEMPLATES: Api2BrandingBrandsBrandIdTemplates,
        PathValues.API_2_BRANDING_BRANDS_BRAND_ID_TEMPLATES_TEMPLATE_ID: Api2BrandingBrandsBrandIdTemplatesTemplateId,
        PathValues.API_2_BRANDING_BRANDS_BRAND_ID_APPS: Api2BrandingBrandsBrandIdApps,
        PathValues.API_2_BRANDING_EMAIL_SETTINGS: Api2BrandingEmailSettings,
        PathValues.API_2_BRANDING_BRANDS_BRAND_ID_TEMPLATES_TEMPLATE_TYPE_LOCALE: Api2BrandingBrandsBrandIdTemplatesTemplateTypeLocale,
        PathValues.API_2_BRANDING_BRANDS_MASTER_TEMPLATES_TEMPLATE_TYPE: Api2BrandingBrandsMasterTemplatesTemplateType,
    }
)
