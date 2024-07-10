import os
import yaml
import json
import whisper
import requests

from datetime import datetime
# from openai import OpenAI
from fastapi import FastAPI, Request

# My modules
import utils
import telegram_endpoint
from log import *

logger.critical("start logging...")

# Change this link to set the hook for telegram
NGROK = "https://abf3-185-98-164-25.ngrok-free.app"

# Folders for debug
# TODO: wrap them in a debug block
AUDIO_PATH_FOLDER = os.path.join('audio', 'temp')
TEMP_PATH = os.path.join("samples", "temp")
utils.create_folder(AUDIO_PATH_FOLDER)
utils.create_folder(TEMP_PATH)

# choose here the size of ur model
MODEL = whisper.load_model('small')
logger.debug("model was loaded")

# TODO: check existence of this file
telegram_api_path = "api-keys.yml"
with open(telegram_api_path) as tg_fp:
    file_api = yaml.safe_load(tg_fp)
    API_TELEGRAM = file_api["TELEGRAM_BOT"]
    OPENAI_API_KEY = file_api["OPENAI_API_KEY"]
    COHERE_API_KEY = file_api["COHERE_API_KEY"]

logger.info(telegram_endpoint.set(API_TELEGRAM, NGROK))

# TODO: refact this as a dict maybe
TELEGRAM_SEND_MESSAGE = f"https://api.telegram.org/bot{API_TELEGRAM}/SendMessage"
TELEGRAM_GET_PATH = f"https://api.telegram.org/bot{API_TELEGRAM}/getFile"
TELEGRAM_DOWNLOAD = f"https://api.telegram.org/file/bot{API_TELEGRAM}/"

UNUSEFUL_KEYS = ["chat", "date", "from", "message_id"]