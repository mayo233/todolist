from pathlib import Path
import os

#settings.pyからそのままコピー
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'f-sl%rtf4!c6&q(@*l$nxilr9rqnk!*!%tspft42q$so)_phst'

#settings.pyからそのままコピー
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = True #ローカルでDebugできるようになります