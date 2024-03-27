import os, logging, requests, whisper, yaml, json

from fastapi import FastAPI, Request
from datetime import datetime

LOG_DIR = os.path.join('logs', 'asdf.log')
AUDIO_PATH_FOLDER = os.path.join('audio', 'temp')

telegram_api_path = os.path.join("telegram_api.yml")



LOG = logging.getLogger('asdf')
handler = logging.FileHandler(LOG_DIR, mode='a')
log_format = logging.Formatter(
    '%(asctime)s %(levelname)s %(module)s %(funcName)s %(lineno)d %(message)s')
handler.setFormatter(log_format)
LOG.setLevel(logging.DEBUG)
LOG.addHandler(handler)

with open(telegram_api_path) as tg_fp:
    API_TELEGRAM = yaml.safe_load(tg_fp)["API_TELEGRAM"]["aris997testbot"]

MODEL = whisper.load_model('medium')
UNUSEFUL_KEYS = ["chat", "date", "from", "message_id"]