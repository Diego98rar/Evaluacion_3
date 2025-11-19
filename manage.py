#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    
    # --- INICIO CONFIGURACIÓN ORACLEDB ---
    try:
        import oracledb
        # Hacemos que oracledb se comporte como cx_Oracle para Django
        oracledb.version = "8.3.0"
        sys.modules["cx_Oracle"] = oracledb
    except ImportError:
        pass
    # --- FIN CONFIGURACIÓN ORACLEDB ---

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()