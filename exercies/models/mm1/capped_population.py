"""
M/M/1 Queue with Finite Population Model
"""

import numpy as np
from math import factorial as fact
from enum import Enum

class MM1CappedPopulation:
    """
    Class to represent an M/M/1 FIFO queue with a finite population.
    """

    def __init__(self, lmbda: float, mu: float, m: int):
        """
        Initialize the M/M/1 queue.

        Parameters:
        lmbda (float): Arrival rate (customers per time unit).
        mu (float): Service rate (customers per time unit).
        m (int): Population size.
        """

        if lmbda >= mu:
            raise ValueError("This system won't stop growing (lambda >= mu).")

        self.lmbda = lmbda
        self.mu = mu
        self.psi = lmbda / mu
        self.m = m

    def system_units_amount_mean(self) -> float:
        """
        Calculate the mean number of units in the system.

        Returns:
        float: Mean number of units in the system.
        """

        return self.m - (1/self.psi)*(1 - self.probability_of_zero_units())
    
    def queue_units_amount_mean(self) -> float:
        """
        Calculate the mean number of units in the queue. This are units
        in the system but not being served.

        Returns:
        float: Mean number of units in the queue.
        """

        return self.m - ((1 + self.psi)/self.psi) * (1 - self.probability_of_zero_units())

    def unoccupied_servers_mean(self) -> float:
        """
        Calculate the mean number of unoccupied servers.

        Returns:
        float: Mean number of unoccupied servers.
        """
        
        return sum((1 - n) * self.probability_of_n_units(n) for n in range(2))
    
    def time_in_queue_mean(self) -> float:
        """
        Calculate the mean time spent in the queue.

        Returns:
        float: Mean time spent in the queue.
        """
        
        return self.queue_units_amount_mean() / (self.lmbda * self.units_outside_system_mean())
    
    def time_in_system_mean(self) -> float:
        """
        Calculate the mean time spent in the system.

        Returns:
        float: Mean time spent in the system.
        """

        return (1/self.mu)*((self.m/(1 - self.probability_of_zero_units())) - (1/self.psi))
    
    def time_of_service_mean(self) -> float:
        """
        Calculate the mean time spent in service.

        Returns:
        float: Mean time spent in service.
        """
        
        return 1 / self.mu
    
    def probability_of_waiting_over(self, t: float) -> float:
        """
        Calculate the probability of waiting more than t time units.

        Parameters:
        t (float): Time threshold.

        Returns:
        float: Probability of waiting more than t time units.
        """
        
        if t < 0:
            raise ValueError("Time must be non-negative.")
        if t == 0:
            return self.probability_of_waiting()
        
        return self.psi * np.exp(self.mu * t * (self.psi - 1))
    
    def probability_of_zero_units(self) -> float:
        """
        Calculate the probability of having zero units in the system.

        Returns:
        float: Probability of having zero units in the system.
        """

        return  (1 + sum(((fact(self.m)*(self.psi**k)) / (fact(self.m - k))) for k in range(1, self.m + 1)))**(-1)

    def _p_n_recursive(self, n: int):
        """
        Recursive function to calculate P_0.
        """

        if n == 1:
            return (self.m - n + 1) * self.psi * self.probability_of_zero_units()
        else:
            return (self.m - n + 1) * self.psi * self._p_n_recursive(n - 1)
        
    def _p_n_default(self, n: int):
        """
        Default function to calculate P_0.
        """
        return self.probability_of_zero_units() * fact(self.m)*(self.psi**n) / (fact(self.m - n))

    class PnStrategies(Enum):
        """
        Enumeration of strategies for calculating $P_0$.
        """
        DEFAULT = 0
        RECURSIVE = 1

    _p_n_strategies = {
        PnStrategies.DEFAULT: _p_n_default,
        PnStrategies.RECURSIVE: _p_n_recursive
    }
    
    def probability_of_n_units(self, n: int, strategy: PnStrategies = PnStrategies.DEFAULT) -> float:
        """
        Calculate the probability of having n units in the system.
        
        Parameters:
        n (int): Number of units.

        Returns:
        float: Probability of having n units in the system.
        """

        if n < 0:
            raise ValueError("Number of units must be non-negative.")
        if n == 0:
            return self.probability_of_zero_units()
        if n > self.m:
            raise ValueError("Number of units must be less than or equal to the population size.")

        return self._p_n_strategies[strategy](self, n)

    def units_outside_system_mean(self) -> float:
        """
        Calculate the mean number of units outside the system.

        Returns:
        float: Mean number of units outside the system.
        """

        return (1 / self.psi) * (1 - self.probability_of_zero_units())
    
    def arrival_rate_mean(self) -> float:
        """
        Calculate the mean arrival rate.

        Returns:
        float: Mean arrival rate.
        """

        return self.lmbda * self.units_outside_system_mean()
    
    def probability_of_waiting(self) -> float:
        """
        Calculate the probability of waiting at all.

        Returns:
        float: Probability of waiting.
        """

        return 1 - self.probability_of_zero_units()





