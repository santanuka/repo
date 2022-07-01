#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['wez', 'gabor_bernat'])
    for line in edit_file('PKGBUILD'):
        if "pkgname=" in line:
            print("options=(!lto)")
        print(line)
