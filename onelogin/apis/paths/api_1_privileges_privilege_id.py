from onelogin.paths.api_1_privileges_privilege_id.get import ApiForget
from onelogin.paths.api_1_privileges_privilege_id.put import ApiForput
from onelogin.paths.api_1_privileges_privilege_id.delete import ApiFordelete


class Api1PrivilegesPrivilegeId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
