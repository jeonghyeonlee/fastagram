import raven

from .partials import *


DEBUG = False

ALLOWED_HOSTS = [
    "*",
]


INSTALLED_APPS += [
    'raven.contrib.django.raven_compat',
]


RAVEN_CONFIG = {
    'dsn': 'https://e456beea56bc47489828c0c37a8e5be0:0bb0394775b14f419953e9ecb670a6a7@app.getsentry.com/72478',
}
