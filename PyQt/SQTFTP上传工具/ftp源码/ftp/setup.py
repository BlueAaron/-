# -*- coding: utf-8 -*-

import sys

from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = "FTP",
    version = "0.1",
    description = "FTP",
    executables = [Executable("ftp.py", base = base, icon = "ftp.ico")]
    )
