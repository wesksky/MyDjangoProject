import sys
import os
from django.conf import settings
from django.core.management import execute_from_command_line
from django.conf.urls import url
from django.http import HttpResponse
from django.core.wsgi import get_wsgi_application

DEBUG = os.environ.get('DEBUG', 'on') == 'on'

print(DEBUG)

SECRET_KEY = os.environ.get('SECRET_KEY', os.urandom(32))

print(SECRET_KEY)

settings.configure(
    DEBUG = DEBUG,
    SECRET_KEY = SECRET_KEY,
    ROOT_URLCONF  = __name__,
    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)

def index(request):
    return HttpResponse('Hello World')

urlpatterns = (
    url(r'^$', placeholder, name='homepage'),
)

application = get_wsgi_application()

if __name__ == '__main__':

    execute_from_command_line(sys.argv)
