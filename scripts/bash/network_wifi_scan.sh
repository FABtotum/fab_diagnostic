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
. ${TOP}/fabui.env
. ${TOP}/common.sh

#
# Template for making a test_case
#
function test_case()
{
	# Success
	IFACE=$(ifconfig | grep "Link " | grep wlan0 | awk '{print $1}')
	if [ x"$IFACE" == x"wlan0" ]; then
		echo "WiFi interface wlan0 is up."
	else
		echo "WiFi interface wlan0 is down."
		return 1
	fi
	
	iwlist wlan0 scan | grep -E "\s?(Cell|ESSID).+"
	RETR=$?
	
	# Result
	return $RETR
}

testcase_cleanup
test_case $@ > ${TEST_CASE_LOG} 2>&1
testcase_evaluate_result $?
