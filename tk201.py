#!/usr/bin/python

import re
import sys

class Tk102gps(object):

    def __init__(self, in_string):
        self._in_string=in_string
        pattern = re.compile(r".*?(\d+)BR00(.{6})(.)(..)(.{7})(.)(...)(.{7})(.)(.{5})(.{6})(.{6}),(.{8})L(.{8}).*")
        info = pattern.match(self._in_string)
        if info:
            self.serial = info.group(1)
            self.yymmdd = info.group(2)
            self.state = info.group(3)
            self.lat_major = info.group(4)
            self.lat_minor = info.group(5)
            self.lat_indicator = info.group(6)
            self.long_major = info.group(7)
            self.long_minor = info.group(8)
            self.long_indicator = info.group(9)
            self.speed = info.group(10)
            self.tim = info.group(11)
            self.orientation = info.group(12)
            self.io_state = info.group(13)
            self.milepost = info.group(14)
            self.mile_data = info.group(15)
        else:
            raise ValueError("doesn't match pattern")

    def to_dict(self):
        return {
                'serial':self.serial,
                'yymmdd':self.yymmdd,
                'state':self.state,
                'lat_major':self.lat_major,
                'lat_minor':self.lat_minor,
                'lat_indicator':self.lat_indicator,
                'long_major':self.long_major,
                'long_minor':self.long_minor,
                'long_indicator':self.long_indicator,
                'speed':self.speed,
                'time':self.tim,
                'orientation':self.orientation,
                'io_state':self.io_state,
                'milepost':self.milepost,
                'mile_data':self.mile_date
                }

if __name__ == '__main__':
    for line in sys.stdin:
        try:
            dd = Tk201gps(line)
            print(dd)
        except Exception as e:
            pass
