#
# poldeg - misc module
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
import os

def init_gettext():
    '''Init gettext support'''

    import __builtin__
    import gettext
    try:
        txt = gettext.translation('poldeg')
        _ = txt.gettext
    except:
        _ =  lambda s: s
    __builtin__.__dict__['_'] = _

def init_gtk():
    '''Init GTK+ and PyGTK modules'''

    try:
        import pygtk
        pygtk.require('2.2')
    except:
        pass
    try:
        import gtk
        import gtk.glade
    except:
        sys.exit(_('Couldn\'t init GTK+ and PyGTK modules.'))

def init_poldeg():
    '''Basic poldeg initialization'''

    init_gettext()
    try:
        import poldek
    except:
        sys.exit(_('Couldn\'t import poldek\'s python module.'))
    init_gtk()
