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
		
		# Notification service
		self.ns = NotifyService(config=self.config)
	
	def trace(self, log_msg):
		print log_msg
		self.trace_logger.info(log_msg)
	
	def exit(self, error_code):
		self.stop()		 # need to stop the loop first
		exit(error_code)
	
	def __stress_test_thread(self):
		self.trace('Starting stress test')
		
		self.send('M3 S6000')
		self.trace('Speed: 6000RPM')
		time.sleep(7)
		
		for rpm in range(7,14):
			rpm *= 1000
			self.send('M3 S{0}'.format(rpm) )
			self.trace('Speed: {0}RPM'.format(rpm) )
			time.sleep(2)
		
		self.send('M5')
		self.trace('Stopping motor...')
		time.sleep(2)
		
		data = {
			'id' : 'is_working_question',
			'type': 'question',
			'msg': 'Did the motor start and was changing speed?',
			'buttons' : '[Yes][No]'
		}
		self.ns.notify('selftest', data)
		
		self.trace('Starting stress finished')
	
	def custom_action_callback(self, action, data):
		self.trace("Custom handler {0}, {1}".format(action, data))
		if action == "custom":
			self.trace('Action == custom')
			if data[0] == 'start_motor' and data[1] == 'OK':
				self.stress_test_thread = Thread( target=self.__stress_test_thread )
				self.stress_test_thread.start()
			elif data[0] == 'is_working_question':
				if data[1] == 'Yes':
					self.exit(0)
				self.exit(1)
			else:
				self.exit(1)
		else:
			self.trace('unknown action [{0}]'.format(action))
			self.exit(1)
	
	def run(self):
		self.resetTrace()

		data = {
			'id' : 'start_motor',
			'type': 'confirm',
			'msg': 'When ready click OK to start the motor.',
			'buttons' : '[OK]'
		}
		
		self.trace("Notification sending...")
		self.ns.notify('selftest', data)
		self.trace("Notification sent")
		
		self.loop()
		
if __name__ == "__main__":
	tc = TestCase()
	tc.run()
