# (c) 2008-2009
# Jeff Schroeder <jeffschroeder@computer.org>
# Michael DeHaan <michael.dehaan AT gmail>
#
# License: GPLv2+

import distutils.sysconfig
import sys
import os
import traceback

plib = distutils.sysconfig.get_python_lib()
mod_path="%s/cobbler" % plib
sys.path.insert(0, mod_path)

from utils import _
import sys
import cobbler.templar as templar
from cobbler.cexceptions import CX
import utils

def register():
   # this pure python trigger acts as if it were a legacy shell-trigger, but is much faster.
   # the return of this method indicates the trigger type
   return "/var/lib/cobbler/triggers/add/system/post/*"

def run(api, args, logger):
    # FIXME: make everything use the logger
    api.sync()

    return 0




