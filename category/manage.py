#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

from django.db import connection

def my_custom_sql():
    with connection.cursor() as cursor:
        sqlQuery = "SELECT model, price FROM PC;"
        cursor.execute(sqlQuery)
        row = cursor.fetchall()
    return row

def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "category.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    print(my_custom_sql())
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()

# TODO Please refer ppt page 30