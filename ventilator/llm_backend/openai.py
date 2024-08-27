#openai llm implementation class
from ventilator.memory import MemoryItem
from ventilator.llm import LLM as LLMInterface
from openai import OpenAI


class LLM(LLMInterface):

    _client: OpenAI = None

    @property
    def client(self):
        if not self._client:
            self._client = OpenAI(api_key=self.app.config.OPENAI_API_KEY)
        return self._client

    def chat(self, conversation_id):
        #todo: convers messages json building to to_dict method
        response = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": memory_item.role, "content": memory_item.content}
                for memory_item in self.app.memory.get(conversation_id)
            ]
        )
        self.app.log.info(response.choices[0].message)
        self.app.memory.add(conversation_id, MemoryItem(response.choices[0].message.role, response.choices[0].message.content))
        return response.choices[0].message.content
