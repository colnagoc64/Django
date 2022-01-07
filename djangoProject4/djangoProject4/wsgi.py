"""
WSGI config for djangoProject4 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoProject4.settings')

application = get_wsgi_application()


#웹서버와 장고 같은 프레임워크간에 중간다리 역활 = wsgi
