import unittest
from exercies.models.mm1 import MM1Uncapped

class TestMM1Uncapped(unittest.TestCase):
    def setUp(self):
        self.lmbda = 10.0
        self.mu = 15.0
        self.queue = MM1Uncapped(self.lmbda, self.mu)

    def test_probability_of_zero_units(self):
        a1 = self.queue.probability_of_zero_units()
        a2 = 1/3
        self.assertAlmostEqual(a1, a2, delta=1e-2)

    def test_queue_units_amount_mean(self):
        a1 = self.queue.queue_units_amount_mean()
        a2 = 4/3
        self.assertAlmostEqual(a1, a2, delta=1e-2)

    def test_time_in_queue_mean(self):
        a1 = self.queue.time_in_queue_mean()
        a2 = (4.0/3.0)/10.0
        self.assertAlmostEqual(a1, a2, delta=1e-2)

    def test_probability_of_waiting_over(self):
        a1 = self.queue.probability_of_waiting_over(7/60)
        a2 = 0.372
        self.assertAlmostEqual(a1, a2, delta=1e-2)