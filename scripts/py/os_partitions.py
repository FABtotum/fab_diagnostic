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

def test_case(args):
	current_table_tmp = args[1].split()
	planned_table_tmp = args[2].split()
	current_table = {}
	planned_table = {}
	RETR=0
	
	for pt in current_table_tmp:
		tmp = pt.split(':')
		current_table[tmp[0]] = tmp[1][:-1]
		
	for pt in planned_table_tmp:
		tmp = pt.split(':')
		meta = {}
		meta['fs'] = tmp[1]
		meta['size'] = tmp[2]
		planned_table[ '/dev/mmcblk0p'+str(tmp[0]) ] = meta

	for pt in planned_table:
		if pt in current_table:
			if planned_table[pt]['size'] != '-':
				tg_size = int(planned_table[pt]['size'])
				size = int(current_table[pt])
				if size < (tg_size - 5) or size > (tg_size + 5):
					print "Partition",pt,"has the wrong size. Expected ",tg_size,"MB but has",size,"MB"
					RETR=1
				else:
					print "Partition",pt,"size is correct"
		else:
			print "Partition",pt,"does not exist"
			RETR=1
	
	# Result
	exit(RETR)

if __name__ == "__main__":
	import sys
	test_case(sys.argv)
