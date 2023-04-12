from battery import NubbinBattery
from battery import SpindlerBattery

from engine import CapuletEngine
from engine import SternmanEngine
from engine import WilloughbyEngine

from car import Car

class CarFactory:

    @staticmethod
    def CreateCalliope(CurrentDate, LastServiceDate, CurrentMileage, LastServiceMileage):
        engine = CapuletEngine(CurrentMileage, LastServiceMileage)
        battery = SpindlerBattery(LastServiceDate, CurrentDate)
        return Car(engine, battery)

    @staticmethod
    def CreateGlissade(CurrentDate, LastServiceDate, CurrentMileage, LastServiceMileage):
        engine = WilloughbyEngine(CurrentMileage, LastServiceMileage)
        battery = SpindlerBattery(LastServiceDate, CurrentDate)
        return Car(engine, battery)
    
    @staticmethod
    def CreatePalindrome(CurrentDate, LastServiceDate, WarningLightOn):
        engine = SternmanEngine(WarningLightOn)
        battery = SpindlerBattery(LastServiceDate, CurrentDate)
        return Car(engine, battery)
    
    @staticmethod
    def CreateRorschach(CurrentDate, LastServiceDate, CurrentMileage, LastServiceMileage):
        engine = WilloughbyEngine(CurrentMileage, LastServiceMileage)
        battery = NubbinBattery(LastServiceDate, CurrentDate)
        return Car(engine, battery)
    
    @staticmethod
    def CreateThovex(CurrentDate, LastServiceDate, CurrentMileage, LastServiceMileage):
        engine = CapuletEngine(CurrentMileage, LastServiceMileage)
        battery = NubbinBattery(LastServiceDate, CurrentDate)
        return Car(engine, battery)
    