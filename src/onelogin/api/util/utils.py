#!/usr/bin/python

from dateutil import parser

import sys
if sys.version_info[0] >= 3:
    unicode = str


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
    if v is not None and (isinstance(v, str) and v.isdigit()) or(isinstance(v, unicode) and v.isnumeric()):
        return int(v)
    else:
        return v
