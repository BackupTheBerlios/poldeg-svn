#!/usr/bin/env python
#
# poldeg
# poldeg.py
#
# Copyright 2007 Lukasz Kies
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; only version 2 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#

import sys
from misc import *

try:
    import poldek
except:
    poldegError(_('Couldn\'t import poldek module.'))
try:
    import pygtk
    pygtk.require('2.0')
    import gtk
    import gtk.glade
except:
    poldegError(_('Couldn\'t import GTK modules.'))
    sys.exit(1)

class Cpoldeg:
    def __init__(self):
        poldek.lib_init()
        self.ctx = poldek.poldek_ctx()
        self.ctx.load_config()
        try:
            self.ctx.setup()
        except:
            poldegError(_('poldek setup error.'))

if __name__ == '__main__':
    poldeg_main = Cpoldeg()
