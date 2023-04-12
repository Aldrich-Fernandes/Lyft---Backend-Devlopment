import unittest
from datetime import datetime

from battery import NubbinBattery
from battery import SpindlerBattery

class TestNubbinBattery(unittest.TestCase): # replaced very 4 years
    def ShouldBeServiced(self):
        Today = datetime.today().date()
        LastServiceDate = Today.replace(year=Today.year-5)
        battery = NubbinBattery(LastServiceDate, Today)
        self.assertTrue(battery.NeedsService())

    def ShouldNotBeServiced(self):
        Today = datetime.today().date()
        LastServiceDate = Today.replace(year=Today.year-3)
        battery = NubbinBattery(LastServiceDate, Today)
        self.assertFalse(battery.NeedsService())

class TestSpindlerBattery(unittest.TestCase): # replaced very 2 years
    def ShouldBeServiced(self):
        Today = datetime.today().date()
        LastServiceDate = Today.replace(year=Today.year-4)
        battery = SpindlerBattery(LastServiceDate, Today)
        self.assertTrue(battery.NeedsService())

    def ShouldNotBeServiced(self):
        Today = datetime.today().date()
        LastServiceDate = Today.replace(year=Today.year-1)
        battery = SpindlerBattery(LastServiceDate, Today)
        self.assertFalse(battery.NeedsService())