@ -10,18 +10,23 @@ For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""


from pathlib import Path
import environ
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


env = environ.Env()
environ.Env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '066^n&1n5q+gdm-sgqy_q4_8cbnf0&iavx$ecz#s1v+j_qf0o4'
SECRET_KEY = env('SECRET_KEY')
# SECRET_KEY = '066^n&1n5q+gdm-sgqy_q4_8cbnf0&iavx$ecz#s1v+j_qf0o4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
@ -84,7 +89,7 @@ DATABASES = {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'goods',
        'USER': 'postgres',
        'PASSWORD': os.environ.get('default_pass'),
        'PASSWORD': env('POSTGRES_PASS'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
@ -136,7 +141,7 @@ STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STRIPE_SECRET_KEY = os.environ.get('secret_api_key')
STRIPE_SECRET_KEY = env('SECREY_API_KEY')

STRIPE_ENDPOINT_SECRET = 'whsec_8e5828109b068641bbefa160ec1a45c268e5039276053ca805694b5f4ae734a2'
#add env variable
