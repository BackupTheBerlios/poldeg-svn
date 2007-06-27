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
from misc import _

try:
    import poldek
except:
    poldegError(_('Couldn\'t import poldek module.'))

try:
    import pygtk
    pygtk.require('2.2')
except:
    pass

try:
    import gtk, gtk.glade
except:
    poldegError(_('Couldn\'t import PyGTK modules.'))

import pckgs, gui

class Cpoldeg:
    def __init__(self):
        poldek.lib_init()
        self.win_main = gui.Cwin_main()
        self.pckgs = pckgs.Cpackages()
        self.sdic = {'s_win_main_destroy' : self.win_main.poldeg_quit,
's_win_main_show': self.loading}
        self.win_main.signals(self.sdic)
        win = self.win_main.widgets.get_widget('win_main')
        win.present()

    def loading(self, widget):
        self.pckgs.load()

if __name__ == '__main__':
    poldeg_main = Cpoldeg()
    gtk.main()
