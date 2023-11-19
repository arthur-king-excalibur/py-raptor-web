from os.path import join, exists
from os import getenv, makedirs
from pathlib import Path
from dotenv import load_dotenv

# Define project directories
BASE_DIR: str = Path(__file__).resolve().parent.parent
RAPTORWEB_DIR: str = join(BASE_DIR, 'raptorWeb')
TEMPLATE_DIR: str = join(RAPTORWEB_DIR, "templates")
STATIC_DIR: str = join(RAPTORWEB_DIR, "static")
MEDIA_DIR: str = join(RAPTORWEB_DIR, "media")
LOG_DIR: str = join(BASE_DIR, "logs")

RAPTORMC_TEMPLATE_DIR: str = join(TEMPLATE_DIR, "raptormc")
PANEL_TEMPLATE_DIR: str = join(TEMPLATE_DIR, "panel")
RAPTORBOT_TEMPLATE_DIR: str = join(TEMPLATE_DIR, 'raptorbot')
GAMESERVERS_TEMPLATE_DIR: str = join(TEMPLATE_DIR, 'gameservers')
STAFFAPPS_TEMPLATE_DIR: str = join(TEMPLATE_DIR, 'staffapps')
AUTH_TEMPLATE_DIR: str = join(TEMPLATE_DIR, 'authprofiles')

# Load .env file
load_dotenv(join(BASE_DIR, 'stack.env'))

# Django secret key from .env
SECRET_KEY: str = getenv('DJANGO_SECRET_KEY')

# SECURITY WARNING: Neither of the below two True in production!
DEBUG: bool = True if getenv('DEBUG') == "True" else False
USE_SQLITE: bool = True if getenv('USE_SQLITE') == "True" else False

# Set RUNNING_IN_DOCKER to True if you are running this in a Docker container
RUNNING_IN_DOCKER: bool = True if getenv('RUNNING_IN_DOCKER') == "True" else False

# Configure "DOMAIN_NAME" to match the domain name you will use (no www)
DOMAIN_NAME: str = getenv('DOMAIN_NAME')

# Configure web protocol based on DEBUG status
WEB_PROTO: str = ""
if DEBUG and RUNNING_IN_DOCKER:
    DOMAIN_NAME: str = "localhost"
    WEB_PROTO: str = "https"
if DEBUG and not RUNNING_IN_DOCKER:
    DOMAIN_NAME: str = "127.0.0.1:8000"
    WEB_PROTO: str = "http"
else:
    WEB_PROTO: str = "https"

# Addresses the Django app can be directly accessed from.
ALLOWED_HOSTS: list[str] = ['raptorapp', '127.0.0.1', 'localhost']

# Superuser to create when no users are present. To be changed immediately after creation
ADMINS: tuple[str] = (
    (getenv('DEFAULT_SUPERUSER_USERNAME'), getenv('DEFAULT_SUPERUSER_EMAIL')),
)

# CSRF
SESSION_COOKIE_SECURE: bool = True
CSRF_COOKIE_SECURE: bool = True
CSRF_TRUSTED_ORIGINS: list[str] = [f'{WEB_PROTO}://{DOMAIN_NAME}',
                                   f'{WEB_PROTO}://www.{DOMAIN_NAME}']

# Application/Middleware definitions
INSTALLED_APPS: list[str] = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_bootstrap5',
    'tinymce',
    'captcha',
    'raptorWeb.raptormc',
    'raptorWeb.staffapps',
    'raptorWeb.authprofiles',
    'raptorWeb.gameservers',
    'raptorWeb.raptorbot',
    'raptorWeb.panel'
]

MIDDLEWARE: list[str] = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'raptorWeb.raptorbot.botware.RaptorBotWare',
    'raptorWeb.panel.middleware.PanelMessages'
]

ROOT_URLCONF: str = 'config.urls'

TEMPLATES: list[dict] = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'raptorWeb.raptormc.context_processor.context_process',
                'raptorWeb.authprofiles.context_processor.all_users_to_context',
                'raptorWeb.raptorbot.context_processor.add_discord_guild_data',
                'raptorWeb.gameservers.context_processor.server_settings_to_context',
            ],
        },
    },
]

WSGI_APPLICATION: str = 'config.wsgi.application'
ASGI_APPLICATION: str = 'config.asgi.application'

# Email
USE_CONSOLE_EMAIL: bool = True if getenv('USE_CONSOLE_EMAIL') == "True" else False
EMAIL_BACKEND: str = 'django.core.mail.backends.smtp.EmailBackend'
if USE_CONSOLE_EMAIL:
    EMAIL_BACKEND: str = 'django.core.mail.backends.console.EmailBackend'

EMAIL_USE_TLS: bool = True
EMAIL_HOST: str = str(getenv('EMAIL_HOST'))
EMAIL_PORT: int = int(getenv('EMAIL_PORT'))
EMAIL_HOST_USER: str = str(getenv('EMAIL_HOST_USER'))
EMAIL_HOST_PASSWORD: str = str(getenv('EMAIL_HOST_PASSWORD'))

# Database
DATABASES: dict = {}

if USE_SQLITE:

    DATABASES: dict = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

else:

    DATABASES: dict = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': getenv('MYSQL_DATABASE'),
            'USER': getenv('MYSQL_USER'),
            'PASSWORD': getenv('MYSQL_PASSWORD'),
            'HOST': 'mariadb',
            'PORT': '3306',
        }
    }

# Password validation
AUTH_PASSWORD_VALIDATORS: list[dict] = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 10,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Hashing algorithms
PASSWORD_HASHERS: list[str] = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

# Django Authentication
AUTHENTICATION_BACKENDS: list[str] = [
    'raptorWeb.authprofiles.auth.DiscordAuthBackend',
    'django.contrib.auth.backends.ModelBackend'
]

# Logging configuration

# Create log directory if it does not exist
if not exists(LOG_DIR):
    makedirs(LOG_DIR)

LOGGING: dict = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'debug': {
            'format': '[{levelname}] [{asctime}] {module} {process:d} {thread:d} {message}',
            'datefmt': '%Y:%m:%d-%H:%M:%S',
            'style': '{',
        },
        'simple_time': {
            'format': '[{levelname}] [{asctime}] {message}',
            'datefmt': '%H:%M',
            'style': '{',
        },
        'simple': {
            'format': '[{levelname}] {message}',
            'datefmt': '%H:%M',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'debug'
        },
        'django_log_file': {
            'class': 'logging.FileHandler',
            'formatter': 'debug',
            'filename': join(LOG_DIR, 'django.log'),
        },
        'log_file': {
            'class': 'logging.FileHandler',
            'formatter': 'debug',
            'filename': join(LOG_DIR, 'raptorWeb.log'),
        },
        'bot_log_file': {
            'class': 'logging.FileHandler',
            'formatter': 'debug',
            'filename': join(LOG_DIR, 'raptorBot.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'django_log_file'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.request': {
            'handlers': ['console', 'django_log_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'raptormc.views': {
            'handlers': ['console', 'log_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'raptormc.models': {
            'handlers': ['console', 'log_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'raptormc.urlStrip': {
            'handlers': ['console', 'log_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'raptormc.routes': {
            'handlers': ['console', 'log_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'panel.routes': {
            'handlers': ['console', 'log_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'panel.models': {
            'handlers': ['console', 'log_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'panel.views': {
            'handlers': ['console', 'log_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'staffapps.views': {
            'handlers': ['console', 'log_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'authprofiles.auth': {
            'handlers': ['console', 'log_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'authprofiles.views': {
            'handlers': ['console', 'log_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'authprofiles.models': {
            'handlers': ['console', 'log_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'authprofiles.authTags': {
            'handlers': ['console', 'log_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'gameservers.views': {
            'handlers': ['console', 'log_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'gameservers.models': {
            'handlers': ['console', 'log_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'gameservers.serverTags': {
            'handlers': ['console', 'log_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'raptorbot.botware': {
            'handlers': ['console', 'bot_log_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'raptorbot.discordbot.bot': {
            'handlers': ['console', 'bot_log_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'raptorbot.discordbot.util.presence': {
            'handlers': ['console', 'bot_log_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'raptorbot.discordbot.util.announcements': {
            'handlers': ['console', 'bot_log_file'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'raptorbot.discordbot.util.task_check': {
            'handlers': ['console', 'bot_log_file'],
            'level': 'DEBUG',
            'propagate': False,
        }
    }
}

# Internationalization
LANGUAGE_CODE: str = getenv('LANGUAGE_CODE')
TIME_ZONE: str = getenv('TIME_ZONE')
USE_I18N: bool = True
USE_L10N: bool = True
USE_TZ: bool = True

# Static files (CSS, JavaScript, Images)
STATIC_URL: str = '/static/'
STATIC_ROOT: str = join(join(BASE_DIR, 'docker'), join('static'))

# THIS MUST BE NAMED `STATICFILES_DIRS`
STATICFILES_DIRS: list[str] = [
    STATIC_DIR,
]

# Media files (User submitted content)
MEDIA_URL: str = '/media/'
MEDIA_ROOT: str = MEDIA_DIR
DEFAULT_MEDIA: str = f'{WEB_PROTO}://{DOMAIN_NAME}/media/'

# Default primary key field type
DEFAULT_AUTO_FIELD: str = 'django.db.models.BigAutoField'

BACKGROUND_TASK_RUN_ASYNC: bool = True

# ** Settings for "raptormc" app **
ADMIN_BRAND_NAME = "Default" if getenv('ADMIN_BRAND_NAME') == '' else getenv('ADMIN_BRAND_NAME')

# ** Settings for "gameservers" app **
SERVER_PAGINATION_COUNT: int = int(getenv('SERVER_PAGINATION_COUNT'))

# Path to json file to import servers from
IMPORT_JSON_LOCATION: str = join(BASE_DIR, 'server_data_full.json')

# ** Settings for "authprofiles" app **
AUTH_USER_MODEL: str = 'authprofiles.RaptorUser'
LOGIN_URL: str = '/login/'
BASE_USER_URL: str = 'user'
USER_RESET_URL: str = 'reset'
DISCORD_APP_ID: str = getenv('DISCORD_OAUTH_APP_ID')
DISCORD_APP_SECRET: str = getenv('DISCORD_OAUTH_APP_SECRET')
DISCORD_REDIRECT_URL: str = f"{WEB_PROTO}://{DOMAIN_NAME}/api/user/oauth2/login/redirect"
DISCORD_AUTH_URL: str = ("https://discord.com/api/oauth2/authorize?"
                        f"client_id={DISCORD_APP_ID}"
                        f"&redirect_uri={DISCORD_REDIRECT_URL}&response_type=code&scope=identify%20email")

# ** Settings for "raptorbot" app **
DISCORD_BOT_TOKEN: str = getenv('DISCORD_BOT_TOKEN')
DISCORD_BOT_DESCRIPTION: str = getenv('DISCORD_BOT_DESCRIPTION')

# ** Settings for "django-jazzmin" app **
JAZZMIN_SETTINGS = {

    "site_title": f"Admin {ADMIN_BRAND_NAME}",
    "site_header": f"{ADMIN_BRAND_NAME}",
    "site_brand": f"{ADMIN_BRAND_NAME}",
    "site_logo_classes": "img-circle",
    "welcome_sign": f"Welcome to {ADMIN_BRAND_NAME}",
    "topmenu_links": [
        {"name": "Return to Site", "url": "/", "new_window": False},
        {"name": "Admin", "url": "/admin/", "new_window": False},
        {"name": "Control Panel", "url": "/panel/", "new_window": False},
        {"name": "Discord Bot", "url": "/panel/discordbot/", "new_window": False},
        {"name": "Server Actions", "url": "/panel/serveractions/", "new_window": False},
        {"name": "Reporting", "url": "/panel/reporting/", "new_window": False},
        {"app": "raptormc"},
        {"app": "gameservers"},
        {"app": "raptorbot"},
        {"app": "staffapps"},
        {"app": "authprofiles"},
        {"name": "Settings", "url": "/panel/settings/", "new_window": False},
    ],
    "usermenu_links": [
        {"model": "auth.user"},
        {"name": "Return to Site", "url": "/", "new_window": False},
        {"name": "Admin", "url": "/admin/", "new_window": False},
        {"name": "Control Panel", "url": "/panel/", "new_window": False},
        {"name": "Discord Bot", "url": "/panel/discordbot/", "new_window": False},
        {"name": "Server Actions", "url": "/panel/serveractions/", "new_window": False},
        {"name": "Reporting", "url": "/panel/reporting/", "new_window": False},
        {"name": "Settings", "url": "/panel/settings/", "new_window": False},
    ],

    # Sidebar
    "show_sidebar": True,
    "navigation_expanded": False,
    "order_with_respect_to": ["raptormc", "gameservers", "raptorbot", "staffapps", "authprofiles"],
    "custom_links": {
        "raptorbot": [{
            "name": "Discord Bot Control Panel", 
            "url": "/panel/discordbot/", 
            "icon": "fas fa-terminal",
            "permissions": ["raptorbot.view_discordguild"]
        }],
         "gameservers": [{
            "name": "Server Actions", 
            "url": "/panel/serveractions/", 
            "icon": "fas fa-terminal",
            "permissions": ["gameservers.view_server"]
        }]
    },
    "icons": {
        "raptormc": "fas fa-book",
        "raptormc.InformativeText": "fas fa-scroll",
        "raptormc.NavbarLink": "fas fa-map-marker",
        "raptormc.NavbarDropdown": "fas fa-map-marker",
        "raptormc.NavWidget": "fas fa-map-pin",
        "raptormc.NavWidgetBar": "fas fa-map-pin",
        "raptormc.NotificationToast": "fas fa-envelope-square",
        "raptormc.Page": "fas fa-file",
        "gameservers": "fas fa-gamepad",
        "gameservers.Player": "fas fa-headset",
        "gameservers.Server": "fas fa-server",
        "raptorbot": "fas fa-robot",
        "raptorbot.GlobalAnnouncement": "fas fa-bullhorn",
        "raptorbot.ServerAnnouncement": "fas fa-bullhorn",
        "staffapps": "fas fa-book-reader",
        "staffapps.ModeratorApplication": "fas fa-book-open",
        "staffapps.AdminApplication": "fas fa-book-open",
        "authprofiles": "fas fa-users",
        "authprofiles.RaptorUser": "fas fa-user",
        "authprofiles.UserProfileInfo": "fas fa-user-tag",
        "authprofiles.DiscordUserInfo": "fas fa-user-tag",
        
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",
    "related_modal_active": True,
    "use_google_fonts_cdn": True,
    "show_ui_builder": False,
    "related_modal_active": True

}

JAZZMIN_UI_TWEAKS = {

    "navbar_small_text": True,
    "footer_small_text": True,
    "body_small_text": False,
    "brand_small_text": False,
    "brand_colour": False,
    "accent": "accent-lightblue",
    "navbar": "navbar-gray-dark navbar-dark",
    "no_navbar_border": False,
    "navbar_fixed": True,
    "layout_boxed": False,
    "footer_fixed": False,
    "sidebar_disable_expand": True,
    "theme": "cyborg",
    "actions_sticky_top": False,
    "sidebar_nav_child_indent": True,
    "related_modal_active": True

}

# ** Settings for "django_bootstrap5" app **
BOOTSTRAP5: dict = {

    # Set placeholder attributes to label if no placeholder is provided.
    'set_placeholder': False,

}

# ** Settings for "django-tinymce" app **
TINYMCE_DEFAULT_CONFIG: dict = {
        "theme": "silver",
        "height": 500,
        "menubar": True,
        "plugins": "advlist,autolink,lists,link,image,charmap,print,preview,anchor,"
        "searchreplace,visualblocks,code,fullscreen,insertdatetime,media,table,paste,"
        "code,help,wordcount",
        "toolbar": "undo redo | formatselect | "
        "bold italic forecolor backcolor | alignleft aligncenter "
        "alignright alignjustify | bullist numlist outdent indent | "
        "removeformat | help",
    }

