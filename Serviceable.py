# interface
from abc import ABC

class Serviceable(ABC):

    @staticmethod
    def needs_service():
        pass