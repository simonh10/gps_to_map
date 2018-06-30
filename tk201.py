#!/usr/bin/python

import re

test="(087074786835BR00180630A5235.1556N00008.3920W000.3140909000.00,00000000L00000000)"

mm = re.compile(r"\((\d+)BR00(.{6})(.)(..)(.{7})(.)(...)(.{7})(.)(.{5})(.{6})(.{6}),(.{8})L(.{8})\)")

print(mm.match(test).groups())

class Tk102gps(object):

    def __init__(self, in_string):
        self._in_string=in_string
        pattern = re.compile(r"\((\d+)BR00(.{6})(.)(..)(.{7})(.)(...)(.{7})(.)(.{5})(.{6})(.{6}),(.{8})L(.{8})\)")
        info = pattern.match(self._in_string)
        if info:
            serial = info.group(1)
            yymmdd = info.group(2)
            state = info.group(3)
            lat_major = info.group(4)

