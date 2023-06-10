import unittest
from tire.created_tires.carrigan_tire import CarriganTire

class TestCarriganTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear_sensor = [0.5, 0.2, 0.8, 1]
        tire = CarriganTire(tire_wear_sensor)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_wear_sensor = [0.5, 0.2, 0.8, 0.1]
        tire = CarriganTire(tire_wear_sensor)
        self.assertFalse(tire.needs_service())