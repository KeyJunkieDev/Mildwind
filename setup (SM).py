from distutils.core import setup
import py2exe
import sys

if len(sys.argv) == 1:
    sys.argv.append("py2exe")
    sys.argv.append("-q")

class Target:
    def __init__(self, **kw):
        self.__dict__.update(kw)
        self.version = "0.1.0"
        self.company_name = "Keyboard Junkie Devs"
        self.copyright = "Copyright (c) 2015 Keyboard Junkie Devs"
        self.name = "Mildwind Save Manager"

target = Target(
    description = "Save manager utility",
    script = "MildwindSaveManager.py",
    dest_base = "Save Manager",)

setup(
    options = {'py2exe': {'bundle_files': 2,
                          'compressed': True}},
    zipfile = None,
    console = [target],
)