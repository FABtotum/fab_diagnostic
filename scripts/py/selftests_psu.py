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

def test_case():
	from fabtotum.utils.pyro.gcodeclient import GCodeServiceClient
	from fabtotum.fabui.config import ConfigService
	from selftests_common import getEndstopValues, getFrontPanelStatus
	
	# Pyro GCodeService wrapper
	gcs = GCodeServiceClient()
	config = ConfigService()
	
	try:
		safety_door = config.get('settings', 'safety.door')
	except KeyError:
		safety_door = 0

	try:
		switch = config.get('settings', 'switch')
	except KeyError:
		switch = 0
	
	try:
		bed_enabled = config.get('settings', 'hardware')['bed']['enable']
	except KeyError:
		bed_enabled = True
	
	####################################################################
	
	RETR = 0
	
	# Read 24VDC
	reply = gcs.send("M751")
	if reply:
		#V_24V:24.562 V
		try:
			V = float(reply[0].split(':')[1].split()[0])
			if V > 19.200 and V < 28.800:
				print "[V] PSU Voltage nominal 24V DC (+/-20% tolerance): {0}V".format(V)
			else:
				print "CRITICAL: PSU Voltage anomaly. Expected 24V DC +/-20%, got : {0}V".format(V)
				RETR = 1
		except:
			print "No response for M751"
			RETR = 1
	else:
		print "No response for M751"
		RETR = 1
	
	# Read 5VDC
	reply = gcs.send("M752")
	if reply:
		#V_5V:4.979 V
		try:
			V = float(reply[0].split(':')[1].split()[0])
			if V > 4.0 and V < 6.0:
				print "[V] 5V DC Power Supply is Nominal (+/-20% tolerance): {0}V".format(V)
			else:
				print "CRITICAL: 5V DC Power Supply anomaly. Expected 5V DC +/-20%, got : {0}V".format(V)
				RETR = 1
		except:
			print "No response for M752"
			RETR = 1
	else:
		print "No response for M752"
		RETR = 1
		
	# Read Current
	reply = gcs.send("M753")
	if reply:
		#Isinked:0.000 A
		try:
			A= float(reply[0].split(':')[1].split()[0])
			if A < 0.5:
				print "[A] Power consumption is Nominal : {0}A < 500mA".format(A)
			else:
				print "CRITICAL: Power consumption Anomaly : {0}A, expected < 500mA".format(A)
				RETR = 1
		except:
			print "No response for M753"
			RETR = 1
	else:
		print "No response for M753"
		RETR = 1
	
	# Result
	exit(RETR)

if __name__ == "__main__":
	test_case()
