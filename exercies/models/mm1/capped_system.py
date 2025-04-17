"""
M/M/1 Queue with Finite Capacity Model
"""

class MM1CappedSystem:
    """
    Class to represent an M/M/1 queue with finite capacity.
    """

    def __init__(self, lmbda: float, mu: float, M: int):
        """
        Initialize the M/M/1 queue.

        Parameters:
        lmbda (float): Arrival rate (customers per time unit).
        mu (float): Service rate (customers per time unit).
        M (int): Capacity of the system.
        """

        if lmbda >= mu:
            raise ValueError("This system won't stop growing (lambda >= mu).")

        self.lmbda = lmbda
        self.mu = mu
        self.psi = lmbda / mu
        self.M = M

    def system_units_amount_mean(self) -> float:
        """
        Calculate the mean number of units in the system.

        Returns:
        float: Mean number of units in the system.
        """

        sum1 = self.psi / (1 - self.psi)
        sum2 = ((self.M + 1) * (self.psi ** (self.M + 1))) / (1 - (self.psi ** (self.M + 1)))

        return sum1 - sum2
    
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

        return self.queue_units_amount_mean() / (self.lmbda * (self.probability_of_zero_units() + self.probability_of_n_units(1)))
    
    def time_in_system_mean(self) -> float:
        """
        Calculate the mean time spent in the system.
        
        Returns:
        float: Mean time spent in the system.
        """

        sum1 = 1 / (self.mu * (1 - self.psi))
        sum2 = (self.M * (self.psi ** (self.M))) / (self.mu * (1 - (self.psi ** (self.M))))

        return sum1 - sum2
    
    def time_of_service_mean(self) -> float:
        """
        Calculate the mean time spent in service.

        Returns:
        float: Mean time spent in service.
        """

        return 1 / self.mu
    
    def probability_of_zero_units(self) -> float:
        """
        Calculate the probability of having zero units in the system.
        
        Returns:
        float: Probability of having zero units in the system.
        """

        term1 = 1 - self.psi

        return term1 / (term1 **(self.M + 1))
    
    def probability_of_n_units(self, n: int) -> float:
        """
        Calculate the probability of having n units in the system.

        Parameters:
        n (int): Number of units.

        Returns:
        float: Probability of having n units in the system.
        """

        if n > self.M:
            raise ValueError("n must be less than or equal to M.")
        if n == 0:
            return self.probability_of_zero_units()
        if n >= 1:
            return self.probability_of_zero_units() * (self.psi ** n)
        
    def effective_arrival_rate(self) -> float:
        """
        Calculate the effective arrival rate.

        Returns:
        float: Effective arrival rate.
        """

        return self.lmbda * (1 - self.probability_of_n_units(self.M))
