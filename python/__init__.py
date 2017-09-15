import os
import sys

# import tkinter only if Netgen was configured with USE_GUI=ON
if @IMPORT_TKINTER@:
    import tkinter

_netgen_bin_dir=os.path.realpath(os.path.join(os.path.dirname(__file__),'..','@NETGEN_PYTHON_RPATH_BIN@'))
_netgen_lib_dir=os.path.realpath(os.path.join(os.path.dirname(__file__),'..','@NETGEN_PYTHON_RPATH@'))

# from . import libngpy
# del path

# del sys
# del os

from . import libngpy
