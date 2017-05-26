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
	
	# Pyro GCodeService wrapper
	gcs = GCodeServiceClient()
	
	# Failure
	RETR=1
	
	print ">> G0"
	reply = gcs.send('G0', timeout=5)
	if reply:
		print "<<", " ".join(reply)
		if reply[0] == 'ok':
			# Success
			print "Totumduino link is working."
			RETR=0
	else:
		print ">> no response"
		print "Totumduino link is not working."
	
	# Result
	exit(RETR)

if __name__ == "__main__":
	test_case()
