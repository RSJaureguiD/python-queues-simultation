import unittest
from exercies.models.mms import MMSUncapped

class TestMMSUncapped(unittest.TestCase):
    def setUp(self):
        self.lmbda = 80.0
        self.mu = 50.0
        self.s = 2
        self.queue = MMSUncapped(self.lmbda, self.mu, self.s)

    def test_probability_of_zero_units(self):
        a1 = self.queue.probability_of_zero_units()
        a2 = 0.1111
        self.assertAlmostEqual(a1, a2, delta=1e-2)

    def test_time_in_system_mean(self):
        a1 = self.queue.time_in_system_mean()
        a2 = 4.444444/80.0
        self.assertAlmostEqual(a1, a2, delta=1e-2)