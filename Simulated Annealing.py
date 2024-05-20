import math
import random


class SimulatedAnnealing:
    """
    Class representing a simulated annealing algorithm.
    """

    def __init__(self, points):
        self.points = points
        self.energy_function = self._default_energy_function

    def _default_energy_function(self, value):
        # Replace with your actual energy function logic
        return value

    def set_energy_function(self, energy_function):
        """
        Sets the energy function to be used.
        """
        self.energy_function = energy_function

    def next_neighbor(self):
        """
        Selects a random neighbor from the available points.
        """
        return random.choice(self.points)

    def simulate(self, Tmax, Tmin, Cinit):
        """
        Performs the simulated annealing algorithm.
        """
        C = Cinit
        for T in range(Tmin, Tmax + 1):
            EC = self.energy_function(C)
            N = self.next_neighbor()
            EN = self.energy_function(N)
            delta_E = EN - EC
            if delta_E > 0:
                C = N
            else:
                if math.exp(delta_E / T) > random.uniform(0, 1):
                    C = N
        return C


if __name__ == "__main__":
    points = [i for i in range(21)]
    sa = SimulatedAnnealing(points)

    # Override the default energy function if needed
    # sa.set_energy_function(your_custom_energy_function)

    Tmax = 100
    Tmin = 1
    Cinit = 5

    result = sa.simulate(Tmax, Tmin, Cinit)
    print("Final point:", result)
