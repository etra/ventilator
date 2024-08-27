#Memory implementation using sqllite
from typing import List
from ventilator.memory import Memory as MemoryInterface, MemoryItem
import sqlite3

class Memory(MemoryInterface):

        def __init__(self, app: "ventilator.app.App"):
            self.conn = sqlite3.connect('data/memory.db')
            self.cursor = self.conn.cursor()
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS memory
                        (conversation_id text, role text, content text)''')
            super(Memory, self).__init__(app=app)

        def get(self, conversation_id) -> List[MemoryItem]:
            self.cursor.execute(f"SELECT * FROM memory WHERE conversation_id = ?", (conversation_id,))
            rows = self.cursor.fetchall()
            return [MemoryItem(row[1], row[2]) for row in rows]

        def add(self, conversation_id, value: MemoryItem):
            self.cursor.execute(f"INSERT INTO memory VALUES (?, ?, ?)", (conversation_id, value.role, value.content))
            self.conn.commit()

        def delete(self, conversation_id):
            self.cursor.execute(f"DELETE FROM memory WHERE conversation_id = ?", (conversation_id,))
            self.conn.commit()
