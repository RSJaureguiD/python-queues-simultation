"""
M/M/1 Queue Model with Infinite Capacity and Population
"""


import numpy as np

class MM1Uncapped:
    """
    Class to represent an M/M/1 queue with infinite capacity and population.
    """

    def __init__(self, lmbda: float, mu: float):
        """
        Initialize the M/M/1 queue.

        Parameters:
        lmbda (float): Arrival rate (customers per time unit).
        mu (float): Service rate (customers per time unit).
        """

        if lmbda >= mu:
            raise ValueError("This system won't stop growing (lambda >= mu).")

        self.lmbda = lmbda
        self.mu = mu
        self.psi = lmbda / mu

    def system_units_amount_mean(self) -> float:
        """
        Calculate the mean number of units in the system.

        Returns:
        float: Mean number of units in the system.
        """
        
        return self.psi / (1 - self.psi)
    
    def queue_units_amount_mean(self) -> float:
        """
        Calculate the mean number of units in the queue. This are units
        in the system but not being served.

        Returns:
        float: Mean number of units in the queue.
        """
        
        return (self.psi ** 2) / (1 - self.psi)
    
    def unoccupied_servers_mean(self) -> float:
        """
        Calculate the mean number of unoccupied servers.

        Returns:
        float: Mean number of unoccupied servers.
        """
        
        return 1 - self.psi
    
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

        return self.psi * np.exp(self.mu * t * (self.psi - 1))
    
    def probability_of_zero_units(self) -> float:
        """
        Calculate the probability of having zero units in the system.

        Returns:
        float: Probability of having zero units in the system.
        """
        
        return 1 - self.psi
    
    def probability_of_n_units(self, n: int) -> float:
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
        if n >= 1:
            return (self.psi ** n) * (1 - self.psi)
