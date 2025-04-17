"""
M/M/s Queue Model with Infinite Capacity and Population
"""

import numpy as np
from math import factorial as fact

class MMSUncapped:
    """
    Class to represent an M/M/s queue with infinite capacity and population.
    """

    def __init__(self, lmbda: float, mu: float, s: int):
        """
        Initialize the M/M/s queue.

        Parameters:
        lmbda (float): Arrival rate (customers per time unit).
        mu (float): Service rate (customers per time unit).
        s (int): Number of servers.
        """

        if lmbda >= s * mu:
            raise ValueError("This system won't stop growing (lambda >= s * mu).")

        self.lmbda = lmbda
        self.mu = mu
        self.s = s
        self.psi = lmbda / mu

    def system_units_amount_mean(self) -> float:
        """
        Calculate the mean number of units in the system.

        Returns:
        float: Mean number of units in the system.
        """

        div1 = self.psi**(self.s + 1)
        div2 = (self.s * fact(self.s) * ((1 - (self.psi/self.s))**2))
        

        return (div1/div2) * self.probability_of_zero_units() + self.psi
    
    def queue_units_amount_mean(self) -> float:
        """
        Calculate the mean number of units in the queue. This are units
        in the system but not being served.

        Returns:
        float: Mean number of units in the queue.
        """

        return 1 * (self.psi ** (self.s+1)) / (self.s*fact(self.s)*((1-(self.psi/self.s))**2)*self.mu)
    
    def unoccupied_servers_mean(self) -> float:
        """
        Calculate the mean number of unoccupied servers.

        Returns:
        float: Mean number of unoccupied servers.
        """

        return self.s - self.psi
    
    def time_in_queue_mean(self) -> float:
        """
        Calculate the mean time spent in the queue.

        Returns:
        float: Mean time spent in the queue.
        """

        return self.queue_units_amount_mean() / self.lmbda
    
    def time_in_system_mean(self) -> float:
        """
        Calculate the mean time spent in the system.

        Returns:
        float: Mean time spent in the system.
        """

        return self.system_units_amount_mean() / self.lmbda
    
    def time_of_service_mean(self) -> float:
        """
        Calculate the mean time spent in the system.

        Returns:
        float: Mean time spent in the system.
        """

        return 1 / self.mu
    
    def probability_of_waiting_over(self, t: float) -> float:
        """
        Calculate the probability of waiting over a certain time.

        Parameters:
        t (float): Time threshold.

        Returns:
        float: Probability of waiting over the time threshold.
        """

        return self.probability_of_units_in_system_geq_servers_amount() * np.exp(self.mu * t * ((self.psi/self.s)-1))
    
    def probability_of_zero_units(self) -> float:
        """
        Calculate the probability of having zero units in the system.

        Returns:
        float: Probability of having zero units in the system.
        """
        
        sum1 = sum(map(lambda x: ((self.psi**self.s)/fact(x)), range(self.s)))
        sum2 = (self.psi**self.s)/(fact(self.s)* (1-((self.psi/self.s)**2)))


        return (sum1 + sum2) ** -1
    
    def probability_of_n_units(self, n: int) -> float:
        """
        Calculate the probability of having n units in the system.

        Parameters:
        n (int): Number of units.

        Returns:
        float: Probability of having n units in the system.
        """

        if n < self.s:
            return ((self.psi**n) / fact(n)) * self.probability_of_zero_units()
        else:
            return ((self.psi**n) / (fact(self.s) * (self.s**(n-self.s)))) * self.probability_of_zero_units()
        
    def probability_of_units_in_system_geq_servers_amount(self) -> float:
        """
        Calculate the probability of having an amount of units in the system greater than or equal to the number of servers.

        Parameters:
        n (int): Number of units.

        Returns:
        float: Probability of having an amount of units in the system greater than or equal to the number of servers.
        """

        return self.probability_of_zero_units() * (self.psi**self.s) / (fact(self.s) * (1 - (self.psi/self.s)))
    
    def effective_service_rate(self, n: int) -> float:
        """
        Calculate the effective service rate for a given number of units in the system.

        Parameters:
        n (int): Number of units.
        
        Returns:
        float: Effective service rate.
        """

        if n < 0:
            raise ValueError("Number of units must be non-negative.")
        if n < self.s:
            return self.mu * n
        else:
            return self.mu * self.s
