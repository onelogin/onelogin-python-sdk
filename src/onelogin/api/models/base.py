#!/usr/bin/python


class Base(object):

    def __str__(self):
        id_str = " %s" % self.id if hasattr(self, "id") else ""
        return "%s%s:  %r" % (self.__class__.__name__, id_str, self.__dict__)
