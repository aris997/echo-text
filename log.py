import os
import logging
import logging.handlers

import utils
from datetime import datetime

# logger
LOG_DIR = os.path.join("logs")
utils.create_folder(LOG_DIR)

#max size of log file:
MAX_BYTES = 20*1024*1024   #20 MBytes
MAX_BACKUPS_LOGS = 5
LOG_FNAME = os.path.join(LOG_DIR, f"echobot_{utils.now()[:7]}.log")

# # If you want to read months in your language
# import locale
# locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')

class CustomFormatter(logging.Formatter):

    grey = "\x1b[38;20m"
    blue = "\x1b[34;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[41;1m"
    reset = "\x1b[0m"

    format_ = "%(levelname)s:"
    messager = "%(asctime)s \033[94mf=%(funcName)s \033[95m%(filename)s:%(lineno)d \033[0m= %(message)s"

    FORMATS = {
        logging.DEBUG: blue + "   " + format_ + reset + messager,
        logging.INFO: grey + "    " + format_ + reset + messager,
        logging.WARNING: yellow + " " + format_ + reset + messager,
        logging.ERROR: red + "   " + format_ + reset + messager,
        logging.CRITICAL: bold_red  + format_ + reset + messager
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        # self.formatTime(record, datefmt_)
        return formatter.format(record)
    
    def formatTime(self, record: logging.LogRecord, datefmt: str | None = None) -> str:
        datefmt_ = "%d %B %Y %H:%M:%S"
        return super().formatTime(record, datefmt_)

# formatter = logging.Formatter('%(levelname)s:    %(asctime)s \033[94mf=%(funcName)s \033[95m%(filename)s:%(lineno)d\033[0m %(message)s', datefmt="%d %B %Y %H:%M:%S")
console_handler = logging.StreamHandler()
console_handler.setFormatter(CustomFormatter())
file_handler = logging.handlers.RotatingFileHandler(LOG_FNAME, mode='a', maxBytes = MAX_BYTES, backupCount = MAX_BACKUPS_LOGS, encoding="utf-8", delay=False)
formatter = logging.Formatter('%(levelname)s: %(asctime)s f=%(funcName)s %(filename)s:%(lineno)d = %(message)s', datefmt="%Y-%m-%d %H-%M-%S")
file_handler.setFormatter(formatter)
logger = logging.getLogger("echobot")
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# level set should be in global as a global var
logger.setLevel(logging.DEBUG)
