#
# poldeg
# pckgs.py
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

import poldek, misc
from misc import _

class Cpackages:
    def __init__(self):
        '''Prepare poldek config and repositories'''
        self.ctx = poldek.poldek_ctx()
        self.cctx = poldek.poclidek_ctx(self.ctx)
        self.ctx.load_config()
        try:
            self.ctx.setup()
        except:
            misc.poldegError(_('poldek setup error.'))
    
    def load(self):
        '''Loading packages from repositories'''
        self.avail = self.ctx.get_avail_packages()
        self.cctx.load_packages(self.cctx.LOAD_ALL)    
