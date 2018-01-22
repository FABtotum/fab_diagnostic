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
	
	# Success
	RETR=0
	
	#~ print "Checking safety measures..."
	if safety_door == 1:
		if not getFrontPanelStatus(gcs):
			print _("! Front panel door is opened, please close it or disable door safety.")
			gcs.send('M18')
			exit(1)
	
	endstops_start = getEndstopValues(gcs)
	
	if switch == 0: # x_min endstop
		if not endstops_start['x_min'] or not endstops_start['y_max']:
			print _("Move the head to front-left corner so that it triggeres the endstops")
			#~ print "  Note: if you have done this and still get this error message, it could be the x_min is damaged"
			gcs.send('M18')
			exit(1)
	else:
		if not endstops_start['x_max'] or not endstops_start['y_max']:
			print _("Move the head to front-right corner so that it triggeres the endstops")
			gcs.send('M18')
			exit(1)
		
	gcs.send('G27')
	
	## check X endstops
	# Home all axis without probe
	endstops_after_g27 = getEndstopValues(gcs)
	if switch == 0:
		if endstops_start['x_min'] and not endstops_after_g27['x_min']:
			print _("x_min endstop: PASSED")
		else:
			print _("x_min endstop: FAILED")
			gcs.send('M18')
			exit(1)
	else:
		if endstops_start['x_max'] and not endstops_after_g27['x_max']:
			print _("x_max endstop: PASSED")
		else:
			print _("x_max endstop: FAILED")
			gcs.send('M18')
			exit(1)
			
	if endstops_start['y_max'] and not endstops_after_g27['y_max']:
		print _("y_max endstop: PASSED")
	else:
		print _("x_max endstop: FAILED")
		gcs.send('M18')
		exit(1)
		
	## check Z endstop
	# move the platform up
	gcs.send('G91')
	gcs.send('G0 Z-10.00 F1000.00')
	gcs.send('M400')
	endstops_tmp = getEndstopValues(gcs)
	
	if not endstops_tmp['z_max'] and endstops_after_g27['z_max']:
		print _("z_max endstop: PASSED")
	else:
		print _("z_max endstop: FAILED")
		gcs.send('M18')
		exit(1)
	
	# If x_min is used for homing then check x_max
	if switch == 0:
		reply = gcs.send('M734')
		endstop_warning = reply[0]
		# Disable endstop warning
		reply = gcs.send('M734 S0')
		# Move head to x_max position
		gcs.send('G90')
		gcs.send('G0 X234.00 F1000.00')
		gcs.send('M400')
		endstops_tmp = getEndstopValues(gcs)
		# Move away from the endstop
		gcs.send('G91')
		gcs.send('G0 X-10 F1000.00')
		gcs.send('M400')
		
		# Restore enable endstop warning
		reply = gcs.send('M734 S{0}'.format(endstop_warning))
		
		if not endstops_start['x_max'] and endstops_tmp['x_max']:
			print _("x_max endstop: PASSED")
		else:
			print _("x_max endstop: FAILED")
			gcs.send('M18')
			exit(1)
	
	## Check y_min endstop
	reply = gcs.send('M734')
	endstop_warning = reply[0]
	# Disable endstop warning
	reply = gcs.send('M734 S0')
	# Move head to y_min position
	gcs.send('G90')
	gcs.send('G0 Y245.0 F1000.00')
	gcs.send('M400')
	endstops_tmp = getEndstopValues(gcs)
	# Move away from the endstop
	gcs.send('G91')
	gcs.send('G0 Y-10 F1000.00')
	gcs.send('M400')
	# Restore enable endstop warning
	reply = gcs.send('M734 S{0}'.format(endstop_warning))
	
	if not endstops_start['y_min'] and endstops_tmp['y_min']:
		print _("y_min endstop: PASSED")
	else:
		print _("y_min endstop: FAILED")
		gcs.send('M18')
		exit(1)
			
	# Result
	exit(RETR)

if __name__ == "__main__":
	test_case()
