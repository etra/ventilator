#using dict as storage so that we can store the data in memory
from typing import List
from ventilator.memory import Memory as MemoryInterface, MemoryItem


class Memory(MemoryInterface):

    def __init__(self, app: "ventilator.app.App"):
        self.memory = {}
        super(Memory, self).__init__(app=app)

    def get(self, conversation_id) -> List[MemoryItem]:
        return self.memory.get(conversation_id)

    def add(self, conversation_id, value: MemoryItem):
        if conversation_id in self.memory:
            self.memory[conversation_id].extend([value])
        else:
            self.memory[conversation_id] = [value]

    def delete(self, conversation_id):
        del self.memory[conversation_id]