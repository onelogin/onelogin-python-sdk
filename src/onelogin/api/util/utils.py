#!/usr/bin/python

from dateutil import parser


def exception_handler(func):
    def decorator(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]

    return decorator

def exception_handler_return_false(func):
    def decorator(self, *args, **kwargs):
        try:
            return func(self, *args, **kwargs)
        except Exception as e:
            self.error = 500
            self.error_description = e.args[0]
        return False

    return decorator

def str2bool(v):
    if v is None:
        return None
    elif type(v) == bool:
        return v
    else:
        return v.lower() in ("yes", "true", "t", "1")

def str2date(v):
    return None if v is None else parser.parse(v)

def str2int(v):
    return None if v is None else int(v)
