"""
Django settings for csua_backend project.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
import os
from pathlib import Path

from decouple import config
import ldap3

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DJANGO_DEBUG", cast=bool, default=False)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = str(Path(__file__).parent.parent.parent)

PROJECT_HOME = BASE_DIR

FIXTURE_DIRS = [os.path.join(BASE_DIR, "fixtures")]

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

if config("CSUA_BACKEND_USE_MYSQL", cast=bool, default=False):
    DB_PASS = config("DJANGO_DB_PASS")

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": "csua_backend",
            # The following settings are not used with sqlite3:
            "USER": "pnunez",
            "PASSWORD": DB_PASS,
            "HOST": "",  # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
            "PORT": "",  # Set to empty string for default.
            "TEST": {"NAME": "test_csua_backend", "CHARSET": "utf8"},
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(PROJECT_HOME, "csua.sqlite3"),
        }
    }


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALLOWED_HOSTS = [
    "www.csua.berkeley.edu",
    "csua.berkeley.edu",
    "legacy.csua.berkeley.edu",
    "dev.csua.berkeley.edu",
]
if DEBUG:
    ALLOWED_HOSTS.extend(["*"])

SITE_ID = 1

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = "America/Los_Angeles"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.join(PROJECT_HOME, "media_root/")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = "/media/"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(PROJECT_HOME, "static_root/")

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = "/static/"

# Additional locations of static files
STATICFILES_DIRS = [
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_HOME, "static")
]

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
]

# Security
if not DEBUG:
    CSRF_COOKIE_SECURE = True
    CSRF_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SECURE_HSTS_SECONDS = 60
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_Forwarded_Proto", "https")
X_FRAME_OPTIONS = "SAMEORIGIN"

# SECURITY WARNING: keep the secret key used in production secret!
# Make this unique, and don't share it with anybody.
if DEBUG:
    SECRET_KEY = "CSUA)@3zekni&mwis6s031xsru2v&h(y=l89oa4@^&i#lxfoa9p9"
else:
    SECRET_KEY = config("DJANGO_SECRET_KEY")


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        "OPTIONS": {"min_length": 9},
    },
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            # insert your TEMPLATE_DIRS here
            os.path.join(PROJECT_HOME, "templates")
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.contrib.redirects.middleware.RedirectFallbackMiddleware",
    # 'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "apps.csua_backend.urls"

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = "apps.csua_backend.wsgi.application"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Uncomment the next line to enable the admin:
    "django.contrib.admin",
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    "django.contrib.redirects",
    ## Our apps
    "apps.main_page",
    "apps.newuser",
    "apps.db_data",
    "apps.tracker",
    "apps.philbot",
    "apps.outreach",
    ## Third-party
    "markdown_deux",
    "sorl.thumbnail",
    "django_python3_ldap",
]

SESSION_SERIALIZER = "django.contrib.sessions.serializers.JSONSerializer"

ADMINS = (("Robert Quitt", "robertq@csua.berkeley.edu"),)

MANAGERS = ADMINS

DEFAULT_FROM_EMAIL = "django@csua.berkeley.edu"

SERVER_EMAIL = "django-errors@csua.berkeley.edu"

EMAIL_HOST = "mail.csua.berkeley.edu"

EMAIL_PORT = 25

EMAIL_USE_TLS = True

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
            "filters": ["require_debug_false"],
        }
    },
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
        "sorl.thumbnail": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
        }
    },
}

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

## SORL-THUMBNAIL CONFIG ##
THUMBNAIL_DEBUG = DEBUG
THUMBNAIL_BACKEND = "apps.csua_backend.thumbnail_backends.SEOThumbnailBackend"
THUMBNAIL_PREFIX = "thumbnails"
THUMBNAIL_COLORSPACE = None
THUMBNAIL_PRESERVE_FORMAT = True

## SLACK CONFIG ##
SLACK_CLIENT_ID = "3311748471.437459179046"
SLACK_CLIENT_SECRET = config("SLACK_CLIENT_SECRET", default="")
SLACK_BOT_USER_TOKEN = config("SLACK_BOT_USER_TOKEN", default="")
SLACK_SIGNING_SECRET = config("SLACK_SIGNING_SECRET", default="")
SLACK_VERIFICATION_TOKEN = config("SLACK_VERIFICATION_TOKEN", default="")

## LDAP_AUTH CONFIG ##
LDAP_AUTH_URL = "ldaps://ldap.csua.berkeley.edu"
LDAP_AUTH_USE_TLS = True
LDAP_AUTH_SEARCH_BASE = "ou=People,dc=csua,dc=berkeley,dc=edu"
LDAP_AUTH_USER_FIELDS = {"username": "uid", "gecos": "gecos"}
LDAP_AUTH_USER_LOOKUP_FIELDS = ("username",)
LDAP_AUTH_OBJECT_CLASS = "posixAccount"
LDAP_AUTH_CLEAN_USER_DATA = "apps.csua_backend.settings.clean_ldap_user_data"
LDAP_AUTH_CONNECT_TIMEOUT = 1

STAFF_GROUPS = ("excomm", "root")


def clean_ldap_user_data(fields):
    """
    Path to a callable that takes a dict of {model_field_name: value}, returning a dict of clean model data.
    Use this to customize how data loaded from LDAP is saved to the User model.
    See django-python3-ldap docs for more info.
    """
    if "gecos" in fields:
        gecos = fields["gecos"].split(",")
        name = gecos[0].split(" ", 1)
        if len(name) == 1:
            first_name, last_name = name[0], ""
        else:
            first_name, last_name = name
        if len(gecos) > 1:
            email = gecos[1]
        else:
            email = ""
    else:
        first_name, last_name, email = "", "", ""

    with ldap3.Connection("ldaps://ldap.csua.berkeley.edu") as c:
        c.search(
            "ou=Group,dc=csua,dc=berkeley,dc=edu",
            "(memberUid={})".format(fields["username"]),
            attributes="cn",
        )
        groups = [str(group.cn) for group in c.entries]

    is_staff = any(staff_group in groups for staff_group in STAFF_GROUPS)

    return {
        "username": fields["username"],
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "is_staff": is_staff,
        "is_superuser": is_staff,
    }


AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
    "django_python3_ldap.auth.LDAPBackend",
]
