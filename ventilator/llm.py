
from abc import ABC, abstractmethod

class LLM(ABC):
    def __init__(self, app: "ventilator.app.App"):
        self.app = app

    @abstractmethod
    def chat(self, conversation_id):
        pass


def get_llm_backend(backend: str, app: "ventilator.app.App"):
    if backend == "openai":
        from ventilator.llm_backend.openai import LLM
    else:
        raise Exception("Invalid memory backend")
    return LLM(app)

[
    {"role": "system", "content": "...."},
    {"role": "user", "content": "...."},
    {"role": "system", "content": "...."},
]

