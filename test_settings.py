"""
These settings are here to use during tests, because django requires them.

In a real-world use case, apps in this project are installed into other
Django applications, so these settings will not be used.
"""

from os.path import abspath, dirname, join


def root(*args):
    """
    Get the absolute path of the given path relative to the project root.
    """
    return join(abspath(dirname(__file__)), *args)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'default.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'taxonomy'
)

LOCALE_PATHS = [
    root('taxonomy', 'conf', 'locale'),
]

# ROOT_URLCONF = 'taxonomy.urls'

SECRET_KEY = 'insecure-secret-key'


# Settings related to to EMSI client
EMSI_API_ACCESS_TOKEN_URL = 'https://auth.emsicloud.com/connect/token'
EMSI_API_BASE_URL = 'https://emsiservices.com'
EMSI_CLIENT_ID = ''
EMSI_CLIENT_SECRET = ''
