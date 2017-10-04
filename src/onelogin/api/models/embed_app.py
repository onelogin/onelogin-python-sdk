#!/usr/bin/python


class EmbedApp(object):
    def __init__(self, data):
        app_id = data.get('id', None)
        self.id = int(app_id) if app_id is not None else None
        self.name = data.get('name', '')
        self.icon = data.get('icon', '')
        provisioned = data.get('provisioned', '')
        self.provisioned = int(provisioned) if provisioned is not None else None
        extension_required = data.get('extension_required', None)
        self.extension_required = extension_required.lower() in ("yes", "true", "1") if extension_required is not None else None
        login_id = data.get('login_id', None)
        self.login_id = int(login_id) if login_id is not None else None
        personal = data.get('personal', None)
        self.personal = personal.lower() in ("yes", "true", "1") if personal is not None else None
