import numpy as np
import itertools
import math



def distance(cell: list[int, int], gem_position: list[int, int], noise: bool = True) -> float:
    # Calculate Euclidean distance between the current cell and the gem position.
    assert len(cell) == len(gem_position) == 2, f'[E] Cell and gem_position must be in 2dimensions.'
    distance: float = math.sqrt(((gem_position[0] - cell[0]) ** 2) + ((gem_position[1] - cell[1]) ** 2))
    return (distance + np.random.normal(0, 0.5)) if noise else distance



class BayesianNetwork:

    def __init__(self, grid_size: int, n_gems: int) -> None:
        
        self.grid_size: int = grid_size
        self.every_coordinates: list[list[int, int]] = [(x, y) for x in range(self.grid_size) for y in range(self.grid_size)]
        self.n_gems: int = n_gems
        self.G: np.ndarray = np.ones((self.grid_size, self.grid_size)) / self.grid_size ** 2
        

    def likelihood(self, current_cell: list[int, int], distances: list[float], gem_positions: list[list[int, int]]) -> float:
        
        # Compute likelihood of observing given distances, given gem positions.
        likelihood: float = 1.0
        BASE: float = 2.0
        # gem_positions contient les noeuds G(m) des positions que peuvent prendre les gemmes.
        # On calcule les vecteurs observation vers ces G(m) afin de mettre à jour nos croyances.
        observation: list[float] = sorted([distance(current_cell, gp) for gp in gem_positions])

        for i, ob in enumerate(observation):
            d: float = abs(ob - distances[i])  # Distance entre l'observation et la croyance.
            likelihood *= (BASE ** (-d))

        return likelihood
    
    def infer(self, cell: list[int, int], distances: list[float]) -> None:
        # Update beliefs using inference by enumeration over all possible gem positions.

        # Init la matrice de croyance des positions ainsi que la liste des positions possibles dans la matrice.
        posterior: np.ndarray = np.zeros((self.grid_size, self.grid_size))

        distances.sort()  # On sort les distances pour se permettre d'utiliser les combi au lieu des perms

        # Pour chacune des config possibles des n gemmes;
        for gem_positions in itertools.combinations(self.every_coordinates, self.n_gems):
    
            likelihood: float = self.likelihood(current_cell=cell, distances=distances, gem_positions=gem_positions)
            
            # Pour chacune des gemmes, on met à jour le tableau de la vraisemblance 
            for gc in gem_positions:
                posterior[gc[0]][gc[1]] += likelihood

        self.normalize(mat=posterior)
        self.G *= posterior

        
    def get_belief_distribution(self, move: str | None = None) -> np.ndarray:
        # Return current belief distribution (posterior).
        if move: print(f'[i] Done processing move : {move}.')
        return self.G
    
    @staticmethod
    def normalize(mat: np.ndarray) -> None:
        # normalise matrix 'mat' in place
        mat_sum: float = mat.sum()
        if mat_sum > 0: mat /= mat_sum


