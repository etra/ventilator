#using dict as storage so that we can store the data in memory
from typing import List
from ventilator.app import App
from ventilator.memory import Memory as MemoryInterface


class Memory(MemoryInterface):

    def __init__(self, app: App):
        self.memory = {}
        super(Memory, self).__init__(app=app)

    def get(self, conversation_id) -> List:
        return self.memory.get(conversation_id)

    def add(self, conversation_id, value: List):
        if conversation_id in self.memory:
            self.memory[conversation_id].extend(value)
        else:
            self.memory[conversation_id] = value

    def delete(self, conversation_id):
        del self.memory[conversation_id]

    def display(self, conversation_id):
        if conversation_id in self.memory:
            for message in self.memory[conversation_id]:
                self.app.log.info(message)
        else:
            self.app.log.info("No conversation found")