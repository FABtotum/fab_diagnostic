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
	RETR=0

	echo ">> colibrimngr --help"
	colibrimngr --help
	if [ x"$?" != x"0" ]; then
		RETR=1
	fi
	
	echo
	echo ">> buxybox --help"
	busybox --help
	if [ x"$?" != x"0" ]; then
		RETR=1
	fi
	
	echo
	echo ">> ifup -V"
	ifup -V
	if [ x"$?" != x"0" ]; then
		RETR=1
	fi
	
	echo
	echo ">> iwconfig --help"
	iwconfig --help
	if [ x"$?" != x"0" ]; then
		RETR=1
	fi
	
	echo
	echo ">> dhcpcd --version"
	dhcpcd --version
	if [ x"$?" != x"0" ]; then
		RETR=1
	fi
	
	echo
	echo ">> dnsmasq --version"
	dnsmasq --version
	if [ x"$?" != x"0" ]; then
		RETR=1
	fi

	echo
	echo ">> wpa_supplicant -v"
	wpa_supplicant -v
	if [ x"$?" != x"0" ]; then
		RETR=1
	fi

	echo
	echo ">> hostapd -v"
	hostapd -v
	if [ x"$?" != x"1" ]; then
		RETR=1
	fi
	
	echo
	echo ">> sudo -V"
	sudo -V
	if [ x"$?" != x"0" ]; then
		RETR=1
	fi
	
	echo
	echo ">> avrdude-original --help"
	avrdude-original --help
	if [ x"$?" != x"0" ]; then
		RETR=1
	fi
	
	echo
	echo ">> strace -V"
	strace -V
	if [ x"$?" != x"0" ]; then
		RETR=1
	fi
	
	# Result
	return $RETR
}

testcase_cleanup
test_case $@ > ${TEST_CASE_LOG} 2>&1
testcase_evaluate_result $?
