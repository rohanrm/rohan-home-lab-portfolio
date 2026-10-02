#!/usr/bin/env python3
"""Compatibility entry point; V4 checks are canonical."""
import runpy
from pathlib import Path
runpy.run_path(str(Path(__file__).with_name('audit-v4.py')), run_name='__main__')
