from Serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, Engine, Battery):
        self.__engine = Engine
        self.__battery = Battery

    def NeedsService(self):
        return self.__engine.NeedsService() or self.__battery.NeedsService()
