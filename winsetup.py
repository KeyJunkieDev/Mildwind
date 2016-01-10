from distutils.core import setup
import py2exe
import sys

if len(sys.argv) == 1:
    sys.argv.append("py2exe")
    sys.argv.append("-q")

class Target:
    def __init__(self, **kw):
        self.__dict__.update(kw)
        self.version = "1.0.2.0"
        self.company_name = "Keyboard Junkie Devs"
        self.copyright = "Copyright (c) 2016 Keyboard Junkie Devs"
        self.name = "Mildwind"

target = Target(
    description = "A text-based adventure",
    script = "Mildwind.py",
    dest_base = "Mildwind",
	icon_resources = [(1, "icon.ico")])

setup(
    options = {'py2exe': {'bundle_files': 2,
                          'compressed': True}},
    zipfile = None,
    console = [target],
)