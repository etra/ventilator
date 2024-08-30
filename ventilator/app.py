from typing import List
from ventilator.config import Config
from ventilator.memory import get_memory_backend, Memory, MemoryItem
from ventilator.client import get_client_backend, Client
from ventilator.llm import get_llm_backend, LLM
import logging
import sys
import os


class App:
    config: Config = None
    log: logging = None
    _memory: Memory = None
    _llm: LLM = None


    def __init__(self, config: Config, log: logging):
        self.config = config
        self.log = log

    @property
    def is_debug(self):
        return self.config.DEBUG

    @property
    def memory(self):
        self.log.info(f"Getting memory: {self.config.MEMORY_BACKEND}")
        if not self._memory:
            self._memory = get_memory_backend(self.config.MEMORY_BACKEND, self)

        return self._memory

    @property
    def llm(self):
        if not self._llm:
            self._llm = get_llm_backend(self.config.LLM_BACKEND, self)
        return self._llm

    def test(self, **kwargs):
        self.memory.add("test", MemoryItem("system", "You are helpfull bot which job is to write a short story from given random words, you are required to provide funny title and funny short story. If user do not provide random words use function generate_random_words to get random words user may provide number of words it would like it to generate but this is optional"))
        self.memory.add("test", MemoryItem("user", "Hello write me a story"))

        response = self.llm.chat("test")
        self.log.info(response)


        self.memory.delete("test")
    def run(self, **kwargs):
        client = get_client_backend(self.config.CLIENT_BACKEND, self)
        client.run()

        self.log.info(f"Starting the app... in {'debug' if self.is_debug else 'non debug'} mode")

    def _init_conversation(self, conversation_id: str):
        # self.memory.add("test", MemoryItem("system", "You are helpfull bot which job is to write a short story (max 1900 charecters) from given random words, you are required to provide funny title and funny short story. If user do not provide random words use function generate_random_words to get random words user may provide number of words it would like it to generate but this is optional"))
        # self.memory.add(conversation_id, MemoryItem)
        # return 'Hello, I am a bot! I am here to help you with your questions.'
        pass

    def on_message(self, conversation_id: str, messages: str):

        conversation = self.memory.get(conversation_id)

        if not conversation:
            self._init_conversation(conversation_id)

        self.memory.add(conversation_id, MemoryItem.user_message(messages))

        #conversation is full (with newely added message)
        #we do somerhing
        response = self.llm.chat(conversation_id)
        #todo: implement response chunking up to 2000 charecters (split by paragpraphs)

        self.memory.display(conversation_id)
        return response
        #context_from_memory = self.memory.get(message_id)
        #todo: implement check for if memory has no knowlage
        #chatgpt.call(message)
        #
        # return ....
        #todo: implement this
        pass