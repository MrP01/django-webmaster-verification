#!/usr/bin/env python
import os
import sys
from django.core.management import execute_from_command_line

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_project.settings")
    sys.path.insert(0, os.path.abspath('%s/..' % os.getcwd()))
    execute_from_command_line(sys.argv)
