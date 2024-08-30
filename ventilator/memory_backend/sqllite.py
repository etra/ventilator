#Memory implementation using sqllite
from typing import List, Dict
from ventilator.memory import Memory as MemoryInterface, MemoryItem
import sqlite3
import base64
import json

def encode_base64(message: Dict) -> str:
    """
    Encodes a given string into Base64.

    :param input_string: The string to encode.
    :return: The Base64 encoded string.
    """
    input_string = json.dumps(message)
    # Convert the string to bytes
    input_bytes = input_string.encode('utf-8')
    # Encode the bytes to Base64
    encoded_bytes = base64.b64encode(input_bytes)
    # Convert Base64 bytes back to a string
    encoded_string = encoded_bytes.decode('utf-8')
    return encoded_string

def decode_base64(message: str) -> Dict:
    """
    Decodes a given Base64 encoded string.

    :param encoded_string: The Base64 encoded string to decode.
    :return: The decoded string.
    """
    print(message)
    # Convert the Base64 string to bytes
    encoded_bytes = message.encode('utf-8')
    # Decode the Base64 bytes
    decoded_bytes = base64.b64decode(encoded_bytes)
    # Convert decoded bytes back to a string
    decoded_string = decoded_bytes.decode('utf-8')
    print(decoded_string)
    print(json.loads(decoded_string))
    return json.loads(decoded_string)


class Memory(MemoryInterface):

        def __init__(self, app: "ventilator.app.App"):
            self.conn = sqlite3.connect('data/memory.db')
            self.cursor = self.conn.cursor()
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS memory
                        (conversation_id text, message text)''')
            super(Memory, self).__init__(app=app)

        def get(self, conversation_id) -> List[MemoryItem]:
            self.cursor.execute(f"SELECT * FROM memory WHERE conversation_id = ?", (conversation_id,))
            rows = self.cursor.fetchall()
            return [MemoryItem(decode_base64(row[1])) for row in rows]

        def add(self, conversation_id, value: MemoryItem):
            self.cursor.execute(f"INSERT INTO memory VALUES (?, ?)", (conversation_id, encode_base64(value.message)))
            self.conn.commit()

        def delete(self, conversation_id):
            self.cursor.execute(f"DELETE FROM memory WHERE conversation_id = ?", (conversation_id,))
            self.conn.commit()
