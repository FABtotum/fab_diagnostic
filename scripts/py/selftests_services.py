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

from translation import _, setLanguage

def test_case():
	from selftests_common import shell_exec, check_pid
	
	# Success
	RETR=0
	
	fabtotum_service 	= True
	xmlrpc_service		= True
	gpiominitor_service	= True
	websocket_service	= True
	
	soc_id = shell_exec('</proc/cpuinfo grep Hardware | awk \'{print $3}\'')[0].strip()
	if soc_id == 'BCM2709':
		# RPiv3
		pass
	else:
		# RPiv1
		xmlrpc_service = False # Is running inside fabtotum_service
		
	if fabtotum_service:
		print _("Checking FABTotums service:"),
		try:
			with open('/run/fabtotumservices.pid', 'r') as f:
				pid = int(f.read());
				if check_pid(pid):
					print "OK"
		except Exception as e:
			print "NOT RUNNING"
			print "Exception:", str(e)
			RETR=1
		
	if xmlrpc_service:
		print _("Checking XML-RPC service:"),
		try:
			with open('/run/xmlrpcserver.pid', 'r') as f:
				pid = int(f.read());
				if check_pid(pid):
					print "OK"
		except Exception as e:
			print "NOT RUNNING"
			print "Exception:", str(e)
			RETR=1
		
	if gpiominitor_service:
		print _("Checking GPIO monitor service:"),
		try:
			with open('/run/gpiomonitor.pid', 'r') as f:
				pid = int(f.read());
				if check_pid(pid):
					print "OK"
		except Exception as e:
			print "NOT RUNNING"
			print "Exception:", str(e)
			RETR=1
		
	if websocket_service:
		print _("Checking WebSocket service:"),
		try:
			with open('/run/webSocket.pid', 'r') as f:
				pid = int(f.read());
				if check_pid(pid):
					print "OK"
		except Exception as e:
			print "NOT RUNNING"
			print "Exception:", str(e)
			RETR=1
	
	# Result
	exit(RETR)

if __name__ == "__main__":
	test_case()
