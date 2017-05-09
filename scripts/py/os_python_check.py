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

def testModule (name):
	try:
		mod = __import__(name)
		print "Module",name,": OK"
		return mod
	except ImportError:
		print "Module",name,": Not found"
		return None

def test_case():
	import sys
	
	RETR=0
	
	try:
		version = sys.version_info
		if (version[0] == 2 and version[1] == 7):
			print "Checking Python version: OK ", sys.version
		else:
			print "Checking Python version: ERROR "+sys.version
			RETR=1
	except Exception:
		print "Checking Python version: ERROR (< 2.0)"
		RETR=1
		
		
	if not testModule("RPi.GPIO"):
		RETR=1
		
	if not testModule("picamera"):
		RETR=1
		
	if not testModule("six"):
		RETR=1
		
	if not testModule("serpent"):
		RETR=1
		
	if not testModule("pycurl"):
		RETR=1
		
	if not testModule("yaml"):
		RETR=1
		
	if not testModule("selectors34"):
		RETR=1
		
	if testModule("serial"):
		import serial
		print "Checking pyserial version...",
		try:
			serialVersion = serial.VERSION
			print serialVersion
		except AttributeError:
			print "< 2.3: ERROR"
			RETR=1
		parts = serialVersion.split(".", 1)
		if parts[0] != "3":
			RETR=1
	else:
		RETR=1
		
	if not testModule("pathtools"):
		RETR=1
		
	if not testModule("watchdog"):
		RETR=1
		
	if not testModule("ws4py"):
		RETR=1
	
	have_numpy=False
	have_opencv=False
	
	if testModule("numpy"):
		have_numpy=True
	else:
		RETR=1
		
	if testModule("cv"):
		have_opencv=True
	else:
		RETR=1
		
	if testModule("cv2"):
		if have_numpy and have_opencv:
			import numpy
			import cv, cv2
			
			image = numpy.zeros((16,16,3),numpy.uint8)
			print "Checking OpenCV JPEG support...",
			try:
				cv2.imwrite('/tmp/cv2_test.jpg',image)
				print "OK"
			except Exception:
				print "ERROR"
				RETR=1
				
			print "Checking OpenCV PNG support...",
			try:
				cv2.imwrite('/tmp/cv2_test.png',image)
				print "OK"
			except Exception:
				print "ERROR"
				RETR=1
	else:
		RETR=1
		
	if not testModule("Pyro4"):
		RETR=1
		
	if not testModule("requests"):
		RETR=1
		
	# Result
	exit(RETR)

if __name__ == "__main__":
	test_case()
