DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'example',
        'USER': 'example',
        'PASSWORD': 'example',
        'HOST': 'example',
        'PORT': '5432',
    }
}

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'example@gmail.com'
EMAIL_HOST_PASSWORD = 'example'
try:
    from sms.settings_local import *
except ImportError:
    print('settings_local module not found!')