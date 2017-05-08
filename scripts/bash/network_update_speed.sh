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
	#~ echo -e "GET http://fabtotum.com HTTP/1.0\n\n" | nc google.com 80 -w 5 > /dev/null 2>&1
	#~ time wget update.fabtotum.com/testfile -O /tmp/testfile &> /tmp/output
	true
	RETR=$?
	if [ x"$RETR" == x"0" ];
		echo "Connection to update server is available."
	else
		echo "No connection to update server."
	fi
	
	TIME=$(cat /tmp/output | grep real)
	
	rm -f /tmp/testfile
	rm -f /tmp/output
	
	# Result
	return $RETR
}

testcase_cleanup
test_case $@ > ${TEST_CASE_LOG} 2>&1
testcase_evaluate_result $?
