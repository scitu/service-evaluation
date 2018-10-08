#!/usr/bin/env python
import os
import sys


_DEV_STATE = 'dev'
_PRODUCTION_STATE = 'production'


if __name__ == '__main__':
    state = os.environ.get('STATE', _DEV_STATE)
    if state == _DEV_STATE:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", 
            "service_evaluation.settings.dev")
    elif state == _PRODUCTION_STATE:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE",
            "service_evaluation.settings.production")

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
