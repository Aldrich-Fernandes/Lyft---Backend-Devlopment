from Engine import Engine

class SternmanEngine(Engine):
    def __init__(self, WarningLightIsOn):
        self.__WarningLightIsOn = WarningLightIsOn

    def NeedsService(self):
        if self.__WarningLightIsOn:
            return True
        else:
            return False
