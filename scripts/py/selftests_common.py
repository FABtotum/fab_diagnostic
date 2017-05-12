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

import os

def shell_exec(cmd):
	""" Execute shell command """
	stdin,stdout = os.popen2(cmd)
	stdin.close()
	lines = stdout.readlines(); 
	stdout.close()
	return lines

def check_pid(pid):        
	""" Check for the existence of a unix pid. """
	try:
		os.kill(pid, 0)
	except OSError:
		return False
	else:
		return True

def getEndstopValues(gcs):
	""" Return endstop values. True is TRIGGERED """
	endstops = {
		'x_min': False,
		'x_max': False,
		'y_min': False,
		'y_max': False,
		'z_min': False,
		'z_max': False
	}
	
	reply = gcs.send('M119')
	
	for line in reply:
		tmp = line.split(':')
		if tmp[0] in endstops:
			endstops[ tmp[0] ] = (tmp[1].strip() == 'TRIGGERED')
	
	return endstops

def getFilamentStatus(gcs):
	""" Return filament status. True means Filament is detected """
	reply = gcs.send('M740')
	if reply:
		return reply[0].strip() == 'TRIGGERED'
		
	return False
	
def getFrontPanelStatus(gcs):
	""" Return front panel status. True means Closed """
	reply = gcs.send('M741')
	if reply:
		return reply[0].strip() == 'TRIGGERED'
		
	return False
	
def getSpoolPanelStatus(gcs):
	""" Return front panel status. True means Closed """
	reply = gcs.send('M742')
	if reply:
		return reply[0].strip() == 'TRIGGERED'
		
	return False
	
def getBedStatus(gcs):
	""" Return front panel status. True means heated side up """
	reply = gcs.send('M744')
	if reply:
		return reply[0].strip() == 'TRIGGERED'
		
	return False
	
def getHeadStatus(gcs):
	""" Return front panel status. True means head is in place """
	reply = gcs.send('M745')
	if reply:
		return reply[0].strip() == 'TRIGGERED'
		
	return False
