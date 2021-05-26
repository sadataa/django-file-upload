from .base import *

SECRET_KEY = config('SECRET_KEY')
ALLOWED_HOSTS = ['127.0.0.1', '*']

DEBUG = True

# if DEBUG:
#     # EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
#     EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}