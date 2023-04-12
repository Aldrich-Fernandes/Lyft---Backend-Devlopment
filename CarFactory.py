from battery.NubbinBattery import NubbinBattery
from battery.SpindlerBattery import SpindlerBattery

from engine.CapuletEngine import CapuletEngine
from engine.SternmanEngine import SternmanEngine
from engine.WilloughbyEngine import WilloughbyEngine

from tyre.CarriganTyre import CarriganTyre
from tyre.OctoprimeTyre import OctoprimeTyre

from car import Car

class CarFactory:

    @staticmethod
    def CreateCalliope(CurrentDate, LastServiceDate, CurrentMileage, LastServiceMileage, SensorData):
        engine = CapuletEngine(CurrentMileage, LastServiceMileage)
        battery = SpindlerBattery(LastServiceDate, CurrentDate)
        tyre = CarriganTyre(SensorData)
        return Car(engine, battery, tyre)

    @staticmethod
    def CreateGlissade(CurrentDate, LastServiceDate, CurrentMileage, LastServiceMileage, SensorData):
        engine = WilloughbyEngine(CurrentMileage, LastServiceMileage)
        battery = SpindlerBattery(LastServiceDate, CurrentDate)
        tyre = CarriganTyre(SensorData)
        return Car(engine, battery, tyre)
    
    @staticmethod
    def CreatePalindrome(CurrentDate, LastServiceDate, WarningLightOn, SensorData):
        engine = SternmanEngine(WarningLightOn)
        battery = SpindlerBattery(LastServiceDate, CurrentDate)
        tyre = OctoprimeTyre(SensorData)
        return Car(engine, battery, tyre)
    
    @staticmethod
    def CreateRorschach(CurrentDate, LastServiceDate, CurrentMileage, LastServiceMileage, SensorData):
        engine = WilloughbyEngine(CurrentMileage, LastServiceMileage)
        battery = NubbinBattery(LastServiceDate, CurrentDate)
        tyre = OctoprimeTyre(SensorData)
        return Car(engine, battery, tyre)
    
    @staticmethod
    def CreateThovex(CurrentDate, LastServiceDate, CurrentMileage, LastServiceMileage, SensorData):
        engine = CapuletEngine(CurrentMileage, LastServiceMileage)
        battery = NubbinBattery(LastServiceDate, CurrentDate)
        tyre = CarriganTyre(SensorData)
        return Car(engine, battery, tyre)
    