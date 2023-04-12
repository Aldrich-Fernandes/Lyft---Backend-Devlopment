from Tyre import Tyre

class OctoprimeTyre(Tyre):
    def __init__(self, SensorData):
        self.__SensorData = list(SensorData)

    def NeedsService(self):
        if sum(self.__SensorData) >= 3.0:
            return True
        else:
            return False