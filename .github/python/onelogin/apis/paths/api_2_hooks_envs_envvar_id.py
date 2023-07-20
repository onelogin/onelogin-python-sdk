from onelogin.paths.api_2_hooks_envs_envvar_id.get import ApiForget
from onelogin.paths.api_2_hooks_envs_envvar_id.put import ApiForput
from onelogin.paths.api_2_hooks_envs_envvar_id.delete import ApiFordelete


class Api2HooksEnvsEnvvarId(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
