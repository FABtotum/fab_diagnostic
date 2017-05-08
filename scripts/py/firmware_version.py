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
def test_case():
	import serial
	baud_rate 	= 250000
	port 		= '/dev/ttyAMA0'
	ser = serial.Serial(port, baud_rate, timeout=0.5)
	ser.flushInput()
	
	ser.write("M765\r\n")
	fw_version=ser.readline().rstrip()
	ser.close()
	
	if fw_version:
		print fw_version
		# Success
		exit(0)
		
	# Failed
	exit(1)

if __name__ == "__main__":
    test_case()
