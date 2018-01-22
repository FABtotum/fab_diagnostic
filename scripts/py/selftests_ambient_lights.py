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
from translation import _, setLanguage

from fabtotum.fabui.gpusher import GCodePusher
from fabtotum.fabui.notify  import NotifyService

class TestCase(GCodePusher):
	
	def __init__(self):
		super(TestCase, self).__init__()
		
		self.red = False
		self.green = False
		self.blue = False
		
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
			if data[0] == 'is_red_working':
				self.red = (data[1] == 'Yes')
				
				self.trace(_('Is RED working...{0}').format(data[1]))
				
				self.trace(_('Setting GREEN color'))
				self.send('M701 S0')
				self.send('M702 S255')
				self.send('M703 S0')
				
				data = {
					'id' : 'is_green_working',
					'type': 'question',
					'msg': _('Are the GREEN ambient lights glowing?'),
					'buttons' : '[Yes][No]'
				}
				self.ns.notify('selftest', data)
				
			elif data[0] == 'is_green_working':
				self.green = (data[1] == 'Yes')
				
				self.trace(_('Is GREEN working...{0}').format(data[1]))
				
				self.trace(_('Setting BLUE color'))
				self.send('M701 S0')
				self.send('M702 S0')
				self.send('M703 S255')
				
				data = {
					'id' : 'is_blue_working',
					'type': 'question',
					'msg': _('Are the BLUE ambient lights glowing?'),
					'buttons' : '[Yes][No]'
				}
				self.ns.notify('selftest', data)
				
			elif data[0] == 'is_blue_working':
				self.blue = (data[1] == 'Yes')
				
				self.trace(_('Is BLUE working...{0}').format(data[1]))
				
				self.trace(_('Setting WHITE color'))
				self.send('M701 S255')
				self.send('M702 S255')
				self.send('M703 S255')
				
				if self.red and self.green and self.blue:
					self.trace(_('All lights are working'))
					self.exit(0)
				else:
					self.trace(_('Some lights are not working'))
					self.exit(1)
				
			else:
				self.exit(1)
		else:
			self.trace(_('unknown action [{0}]').format(action))
			self.exit(1)
	
	def run(self):
		self.resetTrace()

		self.trace(_("=== Starting ambient light test ==="))

		self.trace(_('Setting RED color'))
		self.send('M701 S255')
		self.send('M702 S0')
		self.send('M703 S0')

		data = {
			'id' : 'is_red_working',
			'type': 'question',
			'msg': _('Are the RED ambient lights glowing?'),
			'buttons' : '[Yes][No]'
		}
		self.ns.notify('selftest', data)
		
		self.loop()
		
		self.trace(_("=== Ambient light test finished ==="))
		self.exit(self.error_code)
		
if __name__ == "__main__":
	tc = TestCase()
	tc.run()
