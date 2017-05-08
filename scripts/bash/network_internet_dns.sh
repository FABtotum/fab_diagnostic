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
	DNS=$(cat /etc/resolv.conf | grep nameserver | awk '{print $2}')
	
	RETR=1
	total=0
	pass=0
	for NS in $(echo $DNS); do
		echo "=== $NS ==="
		echo "ping $NS -c 3"
		ping $NS -c 3
		if [ x"$?" == x"0" ]; then
			RETR=0
			let "pass+=1"
		fi
		let "total+=1"
	done
	
	echo
	echo "Summary:"
	echo "$pass of $total nameservers are accesible."
	
	# Result
	return $RETR
}

testcase_cleanup
test_case $@ > ${TEST_CASE_LOG} 2>&1
testcase_evaluate_result $?
