#!/usr/bin/env python
#
# poldeg - main module
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

class _poldeg:
    
    def __init__(self):
        poldek.lib_init()
        self.pckgs = pckgs._packages()
        self.win_main = gui._gui_main()
        dict = {'s_win_main_destroy': self.poldeg_quit}
        self.win_main.add_signals(dict)
        
    def poldeg_quit(self, widget, event):
        result = gui.qmessage(widget, _('Quit poldeg?'))
        if result:
            gtk.main_quit()
            return False
        else:
            return True

if __name__ == '__main__':
    import misc
    misc.init_poldeg()
    import poldek
    import gui
    import pckgs
    poldeg_main = _poldeg()
    import gtk
    gtk.main()
