#!/usr/bin/python


class Statement(object):
    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            self.from_data(args[0])
        else:
            self.from_values(*args)

    def from_data(self, data):
        self.effect = data.get('Effect', "Allow")
        self.actions = data.get('Action', [])
        self.scopes = data.get('Scope', [])

    def from_values(self, effect, actions, scopes):
        self.effect = effect
        self.actions = actions
        self.scopes = scopes
