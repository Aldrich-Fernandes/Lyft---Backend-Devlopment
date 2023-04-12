import unittest
from datetime import datetime

from engine.model.calliope import Calliope
from engine.model.glissade import Glissade
from engine.model.palindrome import Palindrome
from engine.model.rorschach import Rorschach
from engine.model.thovex import Thovex


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        CurrentMileage = 0
        lastServiceMileage = 0

        car = Calliope(last_service_date, CurrentMileage, lastServiceMileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        CurrentMileage = 0
        lastServiceMileage = 0

        car = Calliope(last_service_date, CurrentMileage, lastServiceMileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        CurrentMileage = 30001
        lastServiceMileage = 0

        car = Calliope(last_service_date, CurrentMileage, lastServiceMileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        CurrentMileage = 30000
        lastServiceMileage = 0

        car = Calliope(last_service_date, CurrentMileage, lastServiceMileage)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        CurrentMileage = 0
        lastServiceMileage = 0

        car = Glissade(last_service_date, CurrentMileage, lastServiceMileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        CurrentMileage = 0
        lastServiceMileage = 0

        car = Glissade(last_service_date, CurrentMileage, lastServiceMileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        CurrentMileage = 60001
        lastServiceMileage = 0

        car = Glissade(last_service_date, CurrentMileage, lastServiceMileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        CurrentMileage = 60000
        lastServiceMileage = 0

        car = Glissade(last_service_date, CurrentMileage, lastServiceMileage)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        WarningLightIsOn = False

        car = Palindrome(last_service_date, WarningLightIsOn)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        WarningLightIsOn = False

        car = Palindrome(last_service_date, WarningLightIsOn)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        WarningLightIsOn = True

        car = Palindrome(last_service_date, WarningLightIsOn)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        WarningLightIsOn = False

        car = Palindrome(last_service_date, WarningLightIsOn)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        CurrentMileage = 0
        lastServiceMileage = 0

        car = Rorschach(last_service_date, CurrentMileage, lastServiceMileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        CurrentMileage = 0
        lastServiceMileage = 0

        car = Rorschach(last_service_date, CurrentMileage, lastServiceMileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        CurrentMileage = 60001
        lastServiceMileage = 0

        car = Rorschach(last_service_date, CurrentMileage, lastServiceMileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        CurrentMileage = 60000
        lastServiceMileage = 0

        car = Rorschach(last_service_date, CurrentMileage, lastServiceMileage)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        CurrentMileage = 0
        lastServiceMileage = 0

        car = Thovex(last_service_date, CurrentMileage, lastServiceMileage)
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        CurrentMileage = 0
        lastServiceMileage = 0

        car = Thovex(last_service_date, CurrentMileage, lastServiceMileage)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        last_service_date = datetime.today().date()
        CurrentMileage = 30001
        lastServiceMileage = 0

        car = Thovex(last_service_date, CurrentMileage, lastServiceMileage)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_date = datetime.today().date()
        CurrentMileage = 30000
        lastServiceMileage = 0

        car = Thovex(last_service_date, CurrentMileage, lastServiceMileage)
        self.assertFalse(car.needs_service())


if __name__ == '__main__':
    unittest.main()
