import os
from pathlib import Path

os.environ.setdefault('DJANGO_ENVIROMENT_SETTINGS', 'local_dev')
ENV = os.environ['DJANGO_ENVIROMENT_SETTINGS']

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent.parent

if ENV == 'local_dev':
    # Только в случае локальных настроек, загружаем .env-файл напрямую
    # В случае настроек для docker (docker-dev или docker-prod),
    # за подгрузку переменных окружения отвечает docker-compose
    import envvars
    envvars.load(os.path.join(BASE_DIR, 'env', '.env.dev'))
    from .enviroment.local_settings import *
elif ENV == 'DEV':
    from .enviroment.dev_settings import *