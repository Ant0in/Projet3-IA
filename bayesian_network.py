import numpy as np
import itertools

def distance(cell, gem_position):
    """Calculate Euclidean distance between the current cell and the gem position."""
    pass # TO DO

class BayesianNetwork:
    def __init__(self, grid_size, n_gems):
        self.grid_size = grid_size
        self.n_gems = n_gems
        self.G = # TO DO
    
    def likelihood(self, current_cell, distances, gem_positions):
        """Compute likelihood of observing given distances, given gem positions."""
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
