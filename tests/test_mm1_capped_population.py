import unittest
from exercies.models.mm1 import MM1CappedPopulation

class TestMM1Uncapped(unittest.TestCase):
    def setUp(self):
        self.lmbda = 1.0/4.0
        self.mu = 3.0/2.0
        self.m = 6
        self.queue = MM1CappedPopulation(self.lmbda, self.mu, self.m)

    def test_probability_of_zero_units(self):
        a1 = self.queue.probability_of_zero_units()
        a2 = 0.26492
        self.assertAlmostEqual(a1, a2, delta=1e-2)

    def test_time_in_queue_mean(self):
        a1 = self.queue.time_in_queue_mean()
        a2 = 0.77494
        self.assertAlmostEqual(a1, a2, delta=1e-2)

    def test_units_outside_system_mean(self):
        a1 = self.queue.units_outside_system_mean()
        a2 = 4.41057
        self.assertAlmostEqual(a1, a2, delta=1e-2)