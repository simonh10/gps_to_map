#!/usr/bin/python

import re

test="(087074786835BR00180630A5235.1556N00008.3920W000.3140909000.00,00000000L00000000)"

mm = re.compile(r"\((\d+)BR00(.{6})(.)(..)(.{7})(.)(...)(.{7})(.)(.{5})(.{6})(.{6}),(.{8})L(.{8})\)")

print(mm.match(test).groups())
