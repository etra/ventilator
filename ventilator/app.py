from ventilator.config import Config
from ventilator.memory import get_memory_backend, Memory
from ventilator.client import get_client_backend, Client
import logging
import sys
import os


class App:
    config: Config = None
    log: logging = None
    _memory: Memory = None


    def __init__(self, config: Config, log: logging):
        self.config = config
        self.log = log

    @property
    def is_debug(self):
        return self.config.DEBUG

    @property
    def memory(self):
        if not self._memory:
            self._memory = get_memory_backend(self.config.MEMORY_BACKEND, self)

        return self._memory

    def run(self, **kwargs):
        client = get_client_backend(self.config.CLIENT_BACKEND, self)
        client.run()

        self.log.info(f"Starting the app... in {'debug' if self.is_debug else 'non debug'} mode")

    def on_message(self, message_id, message):

        return "Hello, I'm a bot! I'm here to help you with your questions."
        #context_from_memory = self.memory.get(message_id)
        #todo: implement check for if memory has no knowlage
        #chatgpt.call(message)
        #
        # return ....
        #todo: implement this
        pass