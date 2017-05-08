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

. firmware.env
. common.sh

#
# Not sure it is possible to read those values using arduino bootloader
#
function test_case()
{
	# Make sure no service is using the serial port
	stop_fabui_services
	
	# Check totumduino bootloader communication
	${AVRDUDE} ${AVRDUDE_ARGS} -U lfuse:r:lfuse.hex:i -v
	RETR=$?
	${AVRDUDE} ${AVRDUDE_ARGS} -U hfuse:r:hfuse.hex:i -v
	RETR=$?
	
	# Start FABUI services
	start_fabui_services
	
	# Result
	exit $RETR
}

test_case $@ 2>&1
