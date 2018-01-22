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

import time
from fabtotum.fabui.gpusher import GCodePusher
from translation import _, setLanguage

class TestCase(GCodePusher):
	
	def __init__(self):
		super(TestCase, self).__init__()
	
	def trace(self, log_msg):
		print log_msg
		self.trace_logger.info(log_msg)
	
	def run(self):
		self.resetTrace()
		self.trace(_('Preparing test'))
		self.send('M104 S0')
		self.send('M140 S0')
		
		#exit(200)
		
		self.trace(_('== Bed heating started =='))
		
		RETR = 1
		timeout_60   = 120 # sec => 2 min
		timeout_100  = 300 # sec => 5 min
		duration = 0
		tgt_temp1_reached = False
		tgt_temp1 = 60.0 # C
		tgt_temp2 = 100.0 # C
		
		PRINT_INTERVAL = 5
		print_cnt = PRINT_INTERVAL
		
		self.send('M140 S{0}'.format(tgt_temp2))
		
		while True:
			temps = self.get_temperature_history()
			try:
				nozzle_temp = float(temps['bed_temp'][-1])
			except:
				self.trace(_("Error reading temperatures"))
				break
			
			if print_cnt == PRINT_INTERVAL:
				print_cnt = 1
				self.trace(_('@{0}sec, Bed: {1}C').format(duration, nozzle_temp) )
			else:
				print_cnt = print_cnt +1

			if (nozzle_temp >= tgt_temp1) and not tgt_temp1_reached:
				self.trace('_(Target #1 {0}C temperature reached in {1}sec)'.format(tgt_temp1, duration))
				tgt_temp1_reached = True
				
			if duration >= timeout_60 and nozzle_temp < tgt_temp1:
				self.trace(_("Temperature didn't reach {0}C in {1} seconds.").format(tgt_temp1, timeout_60) )
				break
			
			if nozzle_temp >= tgt_temp2:
				RETR = 0
				self.trace(_('Target #2 {0}C temperature reached in {1}sec').format(tgt_temp2, duration))
				break

			
			time.sleep(1)
			duration = duration +1
			if (timeout_100 - duration) == 0:
				self.trace(_("Temperature didn't reach {0}C in {1} seconds.").format(tgt_temp2, timeout_100) )
				break
		
		self.send('M140 S0')
		
		self.trace(_('== Bed heating finished =='))
		self.stop()
		exit(RETR)

if __name__ == "__main__":
	tc = TestCase()
	tc.run()
