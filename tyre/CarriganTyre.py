from Tyre import Tyre

class CarriganTyre(Tyre):
    def __init__(self, SensorData):
        self.__SensorData = list(SensorData)

    def NeedsService(self):
        for x in range(4):
            if self.__SensorData[x] >= 0.9:
                return True
            else:
                return False
    