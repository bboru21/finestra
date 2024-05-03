from dotenv import load_dotenv
import os

load_dotenv()

from os.path import abspath, basename, dirname, join, normpath
from sys import path


########## PATH CONFIGURATION
# Absolute filesystem path to the scripts project directory:
SCRIPTS_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
APP_ROOT = dirname(SCRIPTS_ROOT)

# Site name:
SITE_NAME = basename(SCRIPTS_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(SCRIPTS_ROOT)
########## END PATH CONFIGURATION


AAI_SETTINGS_API_KEY = os.getenv('AAI_SETTINGS_API_KEY')
VIDEO_FILE_PATH = os.getenv('VIDEO_FILE_PATH')
MOVIES_FILE_PATH = f"{VIDEO_FILE_PATH}/Movies"
