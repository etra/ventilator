from ventilator.app import App
from ventilator.config import config
from ventilator.log import log

import ssl

# Disable certificate verification globally
ssl._create_default_https_context = ssl._create_unverified_context

from logging import basicConfig, Handler
from dotenv import load_dotenv
load_dotenv()
import os
import sys



if __name__ == '__main__':
    app = App(config=config, log=log)
    app.run()
