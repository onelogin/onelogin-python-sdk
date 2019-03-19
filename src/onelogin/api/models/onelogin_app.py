#!/usr/bin/python


class OneLoginApp(object):
    def __init__(self, data):
        app_id = data.get('id', None)
        self.id = int(app_id) if app_id is not None else None
        connector_id = data.get('connector_id', None)
        self.connector_id = int(connector_id) if connector_id is not None else None
        self.name = data.get('name', '')
        self.extension = data.get('extension', None)
        self.icon = data.get('icon', '')        
        self.visible = data.get('visible', None)
        self.provisioning = data.get('provisioning', None)
