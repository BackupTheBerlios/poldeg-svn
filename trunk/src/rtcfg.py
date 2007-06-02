#
# rtcfg.py
#
# Copyright (c) 2007 Lukasz Kies
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published
# by the Free Software Foundation; version 2 only.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#

import gettext, os, sys

class Crtcfg:
    def __init__(self):
	if os.path.isdir('../po'):
	    self.po_dir = '../po'
	try:
	    txt = gettext.translation('poldeg', self.po_dir)
	    _ = txt.gettext
        except:
	    def _(str):
		return str
	if os.path.isdir('../glade'):
	    self.glade_dir = '../glade'
	else:
	    print _('Couldn\'t find glade directory.')
    	    sys.exit(1)

rtcfg = Crtcfg()
