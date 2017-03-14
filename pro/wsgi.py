"""
WSGI config for pro project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
try:
	import pymysql
	pymysql.install_as_MySQLdb()
except ImportError:
	pass

from django.core.wsgi import get_wsgi_applications

os.environ.setdefault("DJANGO_SETTINGS_MODULE","pro.settings")

aplication=get_wsgi_application()