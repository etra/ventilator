#using dict as storage so that we can store the data in memory
from abc import ABC, abstractmethod
from typing import List


class Memory(ABC):

    def __init__(self, app: "ventilator.app.App"):
        self.app = app

    @abstractmethod
    def get(self, conversation_id) -> List:
        pass

    @abstractmethod
    def add(self, conversation_id, value: List):
        pass

    def delete(self, conversation_id):
        pass

    def display(self, conversation_id):
        pass


def get_memory_backend(backend: str, app: "ventilator.app.App"):
    if backend == "memory":
        from ventilator.memory_backend.memory import Memory
    elif backend == "sqllite":
        from ventilator.memory_backend.sqllite import Memory
    else:
        raise Exception("Invalid memory backend")
    return Memory(app)