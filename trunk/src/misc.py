#
# poldeg
# misc.py
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
import gettext

if os.path.isdir('../po'):
    poldeg_podir = '../po'
try:
    txt = gettext.translation('poldeg', poldeg_podir)
    _ = txt.gettext
except:
    def _(str):
        return str
    
def poldegError(str):
    '''Print error messages to console'''
    print str
    sys.exit(1)
    
if os.path.isdir('../glade'):
    poldeg_gladedir = '../glade'
else:
    poldegError(_('Couldn\'t find glade directory.'))
