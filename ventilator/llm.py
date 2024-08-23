
from abc import ABC, abstractmethod

class LLM(ABC):

    memory = None



    @abstractmethod
    def chat(self, message):
        pass

