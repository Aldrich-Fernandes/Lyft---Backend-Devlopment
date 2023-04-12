# This will create the Engines interface
from abc import ABC

class Engine(ABC):

    @staticmethod
    def needsService():
        pass