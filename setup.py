import os
import shutil
import sys
from cx_Freeze import setup, Executable

os.environ['TCL_LIBRARY'] = r'C:\Users\pthaiduy\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\pthaiduy\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'

__version__ = '1.0.0'
base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

include_files = ['facts.txt','rules.txt']
includes = ['tkinter']
excludes = []
packages = ['Equation']

setup(
    name='KBS',
    description='KBS',
    version=__version__,
    executables=[Executable('run.py', base=base)],
    options = {'build_exe': {
        'packages': packages,
        'includes': includes,
        'include_files': include_files,
        'include_msvcr': True,
        'excludes': excludes,
    }},
)

path = os.path.abspath(os.path.join(os.path.realpath(__file__), os.pardir))
build_path = os.path.join(path, 'build', 'exe.win32-3.6')
shutil.copy(r'C:\Users\pthaiduy\AppData\Local\Programs\Python\Python36-32\DLLs\tcl86t.dll', build_path)
shutil.copy(r'C:\Users\pthaiduy\AppData\Local\Programs\Python\Python36-32\DLLs\tk86t.dll', build_path)