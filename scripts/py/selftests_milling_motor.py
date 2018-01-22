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

from translation import _, setLanguage

class TestCase(GCodePusher):
	
	def __init__(self):
		super(TestCase, self).__init__()
		
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
	
	def __stress_test_thread(self):
		self.trace(_('=== Milling motor stress test started ==='))
		
		self.send('M3 S6000')
		self.trace(_('Waiting to start up...'))
		time.sleep(7)
		
		for rpm in range(7,14):
			rpm *= 1000
			self.send('M3 S{0}'.format(rpm) )
			time.sleep(2)
		
		self.send('M5')
		self.trace(_('Stopping motor'))
		time.sleep(2)
		
		data = {
			'id' : 'is_working_question',
			'type': 'question',
			'msg': _('Did the motor start and was changing speed?'),
			'buttons' : '[Yes][No]'
		}
		self.ns.notify('selftest', data)
	
	def custom_action_callback(self, action, data):
		if action == "custom":
			if data[0] == 'start_motor' and data[1] == 'OK':
				self.stress_test_thread = Thread( target=self.__stress_test_thread )
				self.stress_test_thread.start()
			elif data[0] == 'is_working_question':
				self.trace(_('Is the motor working...{0}').format(data[1]))
				if data[1] == 'Yes':
					self.exit(0)
				self.exit(1)
			else:
				self.exit(1)
		else:
			self.trace(_('unknown action [{0}]').format(action))
			self.exit(1)
	
	def run(self):
		self.resetTrace()

		self.trace(_('=== Preparing test ==='))

		head_info = self.config.get_current_head_info()
		self.trace(_('Installed head: {0}').format(head_info['name']))
		
		if "mill" not in head_info['capabilities']:
			self.trace(_('Head does not support milling.'))
			self.trace(_('Skipping test.'))
			self.stop()
			exit(200)

		data = {
			'id' : 'start_motor',
			'type': 'confirm',
			'msg': _('When ready click OK to start the motor.'),
			'buttons' : '[OK]'
		}
		
		self.ns.notify('selftest', data)
		
		self.loop()
		self.trace(_("=== Milling motor stress test finished ==="))
		self.exit(self.error_code)
		
if __name__ == "__main__":
	tc = TestCase()
	tc.run()
