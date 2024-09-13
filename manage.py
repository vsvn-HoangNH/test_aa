#!/usr/bin/env python
import os
import sys
import time

def main():
    "this is main function"
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rag.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ValueError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def aaa():
    pass

if __name__ == '__main__':
    main()
