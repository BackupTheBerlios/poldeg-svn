#
# poldeg - gui module - init
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

import gtk

class _gui_main:

    def __init__(self):
        self.widgets = gtk.glade.XML('glade/poldeg.glade')

    def add_signals(self, dict):
        self.widgets.signal_autoconnect(dict)

def qmessage(widget, text):
        msg = gtk.MessageDialog(widget, 0, gtk.MESSAGE_QUESTION,
                                gtk.BUTTONS_YES_NO, text)
        result = msg.run()
        msg.destroy()
        if result == gtk.RESPONSE_YES:
            return True
        else:
            return False
