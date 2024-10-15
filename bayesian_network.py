import numpy as np
import itertools
import math



def distance(cell: list[int, int], gem_position: list[int, int]) -> float:
    # Calculate Euclidean distance between the current cell and the gem position, in nth dimension.
    cell_dimension: int = len(cell)
    gem_dimension: int = len(cell)
    assert cell_dimension == gem_dimension, f'[E] Cell and gem_position are not in the same dimension. \
        [{cell}, dim={cell_dimension} & {gem_position}, dim={gem_dimension}]'
    return math.sqrt(sum([((gem_position[n] - cell[n]) ** 2) for n in range(cell_dimension)]))  # arbitrarily using cell_dimension.




class BayesianNetwork:

    def __init__(self, grid_size: int, n_gems: int):
        
        self.grid_size: int = grid_size
        self.n_gems: int = n_gems
        self.G: list[int] = [None for _ in range(self.n_gems)]
    
    def likelihood(self, current_cell, distances, gem_positions):
        # Compute likelihood of observing given distances, given gem positions.
        pass # TO DO
    
    def infer(self, cell, distances):
        """Update beliefs using inference by enumeration over all possible gem positions."""
        posterior = np.zeros((self.grid_size, self.grid_size))
        
        # ...
        # TO DO
        
        self.G = posterior
    
    def get_belief_distribution(self):
        """Return current belief distribution (posterior)."""
        return self.G
