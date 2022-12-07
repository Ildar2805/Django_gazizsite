# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/i/ildar2805/ildar2805.beget.tech/gazizsite')
sys.path.insert(1, '/home/i/ildar2805/ildar2805.beget.tech/venv_django/lib/python3.10/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'gazizsite.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()