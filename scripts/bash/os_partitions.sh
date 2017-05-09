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
# Template for making a test_case
#
function test_case()
{
	# Log of partition table
	fdisk -u -l /dev/mmcblk0
	echo
	
	. /mnt/live/mnt/boot/earlyboot/earlyboot.conf
	
	TABLE=$(fdisk -ul /dev/mmcblk0 | grep "^/dev/mmcblk0" | awk '{print $1 ":" $7}')
	PARTS=""
	for pt_info in $(echo $PARTITIONS); do
		NUM=$(echo $pt_info | awk -F: '{print $1}')
		FS=$(echo $pt_info | awk -F: '{print $3}' | awk -F, '{print $1}')
		SZ=$(echo $pt_info | awk -F: '{print $5}' | awk -F, '{print $1}')
		PARTS="${PARTS} ${NUM}:${FS}:${SZ}"
	done
	
	python ${TOP}/../py/os_partitions.py "$TABLE" "$PARTS"
	RETR=$?
	# Result
	return $RETR
}

testcase_cleanup
test_case $@ > ${TEST_CASE_LOG} 2>&1
testcase_evaluate_result $?
