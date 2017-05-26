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

class TestCase(GCodePusher):
	
	def __init__(self):
		super(TestCase, self).__init__()
	
	def trace(self, log_msg):
		print log_msg
		self.trace_logger.info(log_msg)
	
	def run(self):
		self.resetTrace()
		self.trace('Preparing test')
		self.send('M104 S0')
		self.send('M140 S0')
		
		RETR = 1
		
		head_info = self.config.get_current_head_info()
		self.trace('Installed head: {0}'.format(head_info['name']))
		
		reply = self.send("M745")
		if reply[-2] != 'TRIGGERED':
			self.trace('Please insert a printing head.')
			self.stop()
			exit(RETR)
		
		if "print" in head_info['capabilities']:
			self.trace('Max allowed temperature: {0}C'.format(head_info['max_temp']))
			self.trace('PID: {0}'.format(head_info['pid']))
		else:
			self.trace('Head does not support heating.')
			self.trace('Skipping test.')
			self.stop()
			exit(200)
		
		self.trace('== Nozzle heating started ==')
		
		
		# v2 head 21C -> 200C: 140s
		# v1 head     -> 200C:
		# pro_head    -> 200C:
		timeout  = 240 # sec => 4 min
		duration = 0
		tgt_temp = 200.0 # C
		
		PRINT_INTERVAL = 5
		print_cnt = PRINT_INTERVAL
		
		self.send('M104 S{0}'.format(tgt_temp))
		
		while True:
			temps = self.get_temperature_history()
			nozzle_temp = float(temps['ext_temp'][-1])
			
			if print_cnt == PRINT_INTERVAL:
				print_cnt = 1
				self.trace('@{0}sec, Nozzle: {1}C'.format(duration, nozzle_temp) )
			else:
				print_cnt = print_cnt +1
			
			if nozzle_temp >= tgt_temp:
				RETR = 0
				self.trace('Target temperature reached in {0}sec'.format(duration))
				break
			
			time.sleep(1)
			duration = duration +1
			if (timeout - duration) == 0:
				break
		
		self.send('M104 S0')
		
		self.trace('== Nozzle heating finished ==')
		self.stop()
		exit(RETR)

if __name__ == "__main__":
	tc = TestCase()
	tc.run()
