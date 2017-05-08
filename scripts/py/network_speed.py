#!/bin/env python
# -*- coding: utf-8; -*-
#
# (c) 2017 FABtotum, http://www.fabtotum.com
#
# This file is part of FABUI.
#
# FABUI is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# FABUI is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with FABUI.  If not, see <http://www.gnu.org/licenses/>.

#
# Initialize totumduino and read firmware version
#
def test_case(args):
	time = args[1].split()
	minutes = float(time[1][:-1])
	seconds = float(time[2][:-1])
	total_time = minutes * 60.0 + seconds
	print "{0}MBps".format( round(10.0 / total_time, 2) )
	# Success
	exit(0)

if __name__ == "__main__":
	import sys
	test_case(sys.argv)
