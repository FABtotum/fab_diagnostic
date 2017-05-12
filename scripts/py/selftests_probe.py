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
from threading import Event, Thread, RLock

from fabtotum.fabui.gpusher import GCodePusher
from fabtotum.fabui.notify  import NotifyService

class TestCase(GCodePusher):
	
	def __init__(self):
		super(TestCase, self).__init__()
		
		self.has_opened = False
		self.has_closed = False
		
		# Notification service
		self.ns = NotifyService(config=self.config)
		
		self.error_code = 0
	
	def trace(self, log_msg):
		print log_msg
		self.trace_logger.info(log_msg)
	
	def exit(self, error_code):
		self.stop()		 # need to stop the loop first
		self.error_code = error_code
		exit(self.error_code)
	
	def custom_action_callback(self, action, data):
		if action == "custom":
			if data[0] == 'is_probe_opened':
				self.has_opened = ('Yes' == data[1])
				self.trace('Is probe opened...{0}'.format(data[1]))
				self.trace("Closing probe")
				self.gcs.send('M402')
				data = {
					'id' : 'is_probe_closed',
					'type': 'question',
					'msg': 'Is the probe closed?',
					'buttons' : '[Yes][No]'
				}
				self.ns.notify('selftest', data)
				
			elif data[0] == 'is_probe_closed':
				self.has_closed = ('Yes' == data[1])
				self.trace('Is probe closed...{0}'.format(data[1]))

				if self.has_opened and self.has_closed:
					self.exit(0)
				else:
					self.exit(1)
			else:
				self.exit(1)
		else:
			self.trace('unknown action [{0}]'.format(action))
			self.exit(1)
	
	def run(self):
		self.resetTrace()

		# Preparing
		self.send('M402')

		# Start
		self.trace("=== Starting probe test ===")
		self.trace("Opening probe")
		self.send('M401')

		data = {
			'id' : 'is_probe_opened',
			'type': 'question',
			'msg': 'Is the probe extended?',
			'buttons' : '[Yes][No]'
		}
		self.ns.notify('selftest', data)
		
		self.loop()
		self.trace("=== Probe test finished ===")
		self.exit(self.error_code)
		
if __name__ == "__main__":
	tc = TestCase()
	tc.run()
