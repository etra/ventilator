#using dict as storage so that we can store the data in memory
from abc import ABC, abstractmethod
from typing import List


class MemoryItem:
    role: str
    content: str

    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content

    def to_dict(self):
        return {
            "role": self.role,
            "content": self.content
        }

    @staticmethod
    def from_dict(data: dict):
        return MemoryItem(data["role"], data["content"])


class Memory(ABC):

    def __init__(self, app: "ventilator.app.App"):
        self.app = app

    @abstractmethod
    def get(self, conversation_id) -> List[MemoryItem]:
        pass

    @abstractmethod
    def add(self, conversation_id, value: MemoryItem):
        pass

    def delete(self, conversation_id):
        pass

    def display(self, conversation_id):
        has_conversation = False
        for conversation in self.get(conversation_id=conversation_id):
            has_conversation = True
            self.app.log.info(conversation.role + ": " + conversation.content)

        if not has_conversation:
            self.app.log.info("No conversation found for conversation_id: " + conversation_id)

def get_memory_backend(backend: str, app: "ventilator.app.App"):
    if backend == "memory":
        from ventilator.memory_backend.memory import Memory
    elif backend == "sqlite":
        from ventilator.memory_backend.sqllite import Memory
    else:
        raise Exception("Invalid memory backend")
    return Memory(app)