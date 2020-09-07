"""
Django settings for portfolio project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
# Nos sirve para que las rutas que generemos en nuestro proyecto sean relativas, es decir que se generen a partir de esta url base.
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#print(os.path.abspath(__file__))
#print(BASE_DIR)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Nos sirve para usar un modo seguro al subir nuestra app online
SECRET_KEY = 'pm%)yvs5i9shzzj#_vps&u$70d1a%st(fk5-r5y9k&1%!m9l6d'

# SECURITY WARNING: don't run with debug turned on in production!
# Si esta variable se encuentra en 'True' permite que se muestren los errores que se produzcan al ejecutar la aplicacion
DEBUG = True

# En esta variable podemos configurar de que servidores vamos a recibir peticiones.
ALLOWED_HOSTS = []


# Application definition
# Como en Django todos los componentes se manejan como si fueran apps
# Entonces esta variable indica que aplicaciones componen nuestro proyecto que ya vienen por defecto instaladas
# Cada aplicacion es un modulo que funciona de manera independiente
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Middleware definition
# Es un sub framework que permite modificaciones al sistema de procesamiento de request/response de Django. 
# Es un sistema de plugins liviano y de bajo nivel que permite alterar globalmente las entradas y salidas de Django.
# Cada componente middleware es responsable de hacer alguna función específica.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Esta variable contiene el detalle de la url del archivo url.py que es el que permite generar las rutas de cada elemento
# Al igual que la configuracion de settings se genera automaticamente colocando un valor por defecto
ROOT_URLCONF = 'portfolio.urls'

# Templates definition
# En esta variable se definen las plantillas que utilizara mi proyecto
# En 'DIRS' voy a tener que definir donde se alojan todos mis templates
DIR_TEMPLATE = os.path.join(os.path.dirname(BASE_DIR), 'templates')
print(DIR_TEMPLATE)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [DIR_TEMPLATE],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Define desde donde se va a ejecutar mi aplicacion Django
# Cualquier servidor que configure debe saber dónde está el archivo WSGI. 
# Si está utilizando un servidor externo, se verá en su propia configuración. 
# Si está utilizando el servidor de desarrollo de Django, comprobará la configuración de Django. 
# La aplicación Django se puede iniciar de varias maneras diferentes.
WSGI_APPLICATION = 'portfolio.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
# Configuracion de la base de datos que utilizaremos en nuestro proyecto
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(os.path.dirname(BASE_DIR), 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators
# Esta variable contiene los validadores de contraseña que ya trae Django por defecto

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

# Define la configuracion de idioma que utilizaremos
LANGUAGE_CODE = 'es-ar'

# Define la zona horaria que utilizaremos
TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
# Define la ruta de los archivos estaticos que utiliza la aplicacion (html-css-js-img-video)
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(os.path.dirname(BASE_DIR), 'static')),
# Define la ruta de archivos que son generados dinamicamente, o sea a traves de la aplicacion.
MEDIA_URL = '/media/'
MEDIA_ROOT=os.path.join(os.path.dirname(BASE_DIR), 'media')