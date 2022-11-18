import unittest
from modules.Car import Car
from modules.Engine import Engine
from modules.Gearbox import GearBox

class TestCar(unittest.TestCase):
    def setUp(self):
        engine = Engine(3)
        gearbox = GearBox(6)
        self.car = Car("red", "Ford", engine, gearbox)
  

    def test_car_has_colour(self):
        self.assertEqual("red", self.car.colour)

    def test_volume(self):
        self.assertEqual( 3, self.car.engine.volume)

    def test_engine(self):
        self.assertEqual("Engine started", self.car.engine.ignite())

    def test_change_car_colour(self):
        self.car = "black"
        self.assertEqual("black", self.car)

    def test_change_engine_volume(self):
        self.car.engine.volume = 5
        self.assertEqual(5, self.car.engine.volume)
        