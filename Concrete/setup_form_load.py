# A simple setup script to create an executable using PyQt4. This also
# demonstrates the method for creating a Windows executable that does not have
# an associated console.
#
# PyQt4app.py is a very simple type of PyQt4 application
#
# Run the build process by running the command 'python setup.py build'
#
# If everything works well you should find a subdirectory in the build
# subdirectory that contains the files needed to run the application

import sys

from cx_Freeze import setup, Executable
import matplotlib
import  mpl_toolkits.mplot3d

import importlib
importlib.import_module('mpl_toolkits').__path__

base = None
if sys.platform == "win32":
    base = "Win32GUI"

build_exe_options = {"includes":["matplotlib.backends.backend_qt4agg", "mpl_toolkits.mplot3d", "matplotlibwidget","atexit" ,'numpy','scipy.sparse.csgraph._validation'],
                     "include_files":[(matplotlib.get_data_path(), "mpl-data")],
                     "excludes":[],
                     }
setup(
        name = "ClipBoardStatika",
        version = "0.3",
        options = {"build_exe": build_exe_options},
        executables = [Executable("D:\\python_my\\concrete\\form_load.py", base = base)])

