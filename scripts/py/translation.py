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

# Import standard python module
import os
import gettext
import ConfigParser

# Import external modules

# Import internal modules
from fabtotum.fabui.config  import ConfigService

# Set up message catalog access

tr = gettext.translation('fab_diagnostic', '/mnt/userdata/plugins/fab_diagnostic/locale', fallback=True)
_ = tr.ugettext

def setLanguage(lang, domain='fab_diagnostic', config=None):
    if not config:
        config = ConfigService()

    locale_path = config.get('general', 'locale_path')
    
    tr = gettext.translation('fab_diagnostic', locale_path, fallback=True, languages=[lang])
    _ = tr.ugettext
    
    return _