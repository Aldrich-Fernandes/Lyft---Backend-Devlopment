import unittest

from tyre.CarriganTyre import CarriganTyre # replace if any tyreWare >= 0.9
from tyre.OctoprimeTyre import OctoprimeTyre # replace if total ware >= 3

class TestCarriganTyre(unittest.TestCase):
    def ShouldBeServiced(self):
        SensorData = [0.9, 0.3, 0.6, 0.4]
        tyre = CarriganTyre(SensorData)
        self.assertTrue(tyre.NeedsService())

    def ShouldNotBeServiced(self):
        SensorData = [0.5, 0.3, 0.6, 0.4]
        tyre = CarriganTyre(SensorData)
        self.assertFalse(tyre.NeedsService())

class TestOctoprimeTyre(unittest.TestCase):
    def ShouldBeServiced(self):
        SensorData = [0.9, 0.9, 0.9, 0.4]
        tyre = OctoprimeTyre(SensorData)
        self.assertTrue(tyre.NeedsService())

    def ShouldNotBeServiced(self):
        SensorData = [0.5, 0.3, 0.6, 0.4]
        tyre = OctoprimeTyre(SensorData)
        self.assertFalse(tyre.NeedsService())