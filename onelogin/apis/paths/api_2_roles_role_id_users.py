from onelogin.paths.api_2_roles_role_id_users.get import ApiForget
from onelogin.paths.api_2_roles_role_id_users.post import ApiForpost
from onelogin.paths.api_2_roles_role_id_users.delete import ApiFordelete


class Api2RolesRoleIdUsers(
    ApiForget,
    ApiForpost,
    ApiFordelete,
):
    pass
