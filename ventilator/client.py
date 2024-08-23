from abc import ABC, abstractmethod


class Client(ABC):

    def __init__(self, app: "ventilator.app.App"):
        self.app = app




def get_client_backend(backend: str, app: "ventilator.app.App"):
    if backend == "discord":
        from ventilator.client_backend.discord import Client
    else:
        raise Exception("Invalid memory backend")
    return Client(app)