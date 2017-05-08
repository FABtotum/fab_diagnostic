#!/bin/bash
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

TOP=$(dirname $0)
. ${TOP}/firmware.env
. ${TOP}/common.sh

#
# Dump eeprom content fo file
#
function test_case()
{
	# Make sure no service is using the serial port
	stop_fabui_services
	
	# Check totumduino bootloader communication
	HEXFILE="/tmp/fabui/eeprom.hex"
	${AVRDUDE} ${AVRDUDE_ARGS} -F -U eeprom:r:${HEXFILE}:i
	RETR=$?
	
	# Start FABUI services
	start_fabui_services
	
	# Result
	return $RETR
}

testcase_cleanup
test_case $@ > /tmp/fabui/testcase.log 2>&1
testcase_evaluate_result $? - /tmp/fabui/eeprom.hex
