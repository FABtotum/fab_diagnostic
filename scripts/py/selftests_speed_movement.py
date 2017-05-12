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
	
	# Success
	RETR=0
	
	#~ print "Checking safety measures..."
	if safety_door == 1:
		if not getFrontPanelStatus(gcs):
			print "! Front panel door is opened, please close it or disable door safety."
			gcs.send('M18')
			exit(1)
			
	gcs.send('G27')
	
	for i in [5, 7, 8, 10, 15, 18]:
		speed = int(1000*i)
		print 'Speed F = {0} mm/sec'.format( round(speed / 60.0, 2) )
		gcs.send('G90')
		# Long streight movements
		gcs.send('G0 X3 Y3 F{0}'.format(speed))
		gcs.send('G0 X3 Y232 F{0}'.format(speed))
		gcs.send('G0 X212 Y232 F{0}'.format(speed))
		gcs.send('G0 X212 Y3 F{0}'.format(speed))
		gcs.send('G0 X3 Y3 F{0}'.format(speed))
		
		# Long diagonal movements
		gcs.send('G0 X212 Y212 F{0}'.format(speed))
		gcs.send('G0 X3 Y212 F{0}'.format(speed))
		gcs.send('G0 X212 Y3 F{0}'.format(speed))
		gcs.send('G0 X3 Y3 F{0}'.format(speed))
		
		# Short zig-zag (square) movements
		gcs.send('G0 X50 Y3 F{0}'.format(speed))
		gcs.send('G0 X50  Y20 F{0}'.format(speed))
		gcs.send('G0 X100 Y20 F{0}'.format(speed))
		gcs.send('G0 X100 Y40 F{0}'.format(speed))
		gcs.send('G0 X50  Y40 F{0}'.format(speed))
		gcs.send('G0 X50  Y60 F{0}'.format(speed))
		gcs.send('G0 X100 Y60 F{0}'.format(speed))
		gcs.send('G0 X100 Y80 F{0}'.format(speed))
		gcs.send('G0 X50  Y80 F{0}'.format(speed))
		gcs.send('G0 X50  Y100 F{0}'.format(speed))
		gcs.send('G0 X100 Y100 F{0}'.format(speed))
		gcs.send('G0 X100 Y120 F{0}'.format(speed))
		gcs.send('G0 X50  Y120 F{0}'.format(speed))
		gcs.send('G0 X50  Y140 F{0}'.format(speed))
		gcs.send('G0 X100 Y140 F{0}'.format(speed))
		gcs.send('G0 X100 Y160 F{0}'.format(speed))
		gcs.send('G0 X50  Y160 F{0}'.format(speed))
		gcs.send('G0 X50  Y180 F{0}'.format(speed))
		gcs.send('G0 X100 Y180 F{0}'.format(speed))
		gcs.send('G0 X100 Y200 F{0}'.format(speed))
		
		gcs.send('G0 X3 Y3 F{0}'.format(speed))
		
	# Result
	exit(RETR)

if __name__ == "__main__":
	test_case()
