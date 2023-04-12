from Serviceable import Serviceable

class Car(Serviceable):
    def __init__(self, Engine, Battery, Tyre):
        self.__engine = Engine
        self.__battery = Battery
        self.__tyre = Tyre

    def NeedsService(self):
        return self.__engine.NeedsService() or self.__battery.NeedsService() or self.__tyre.NeedsService()
