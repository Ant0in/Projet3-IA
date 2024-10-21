import numpy as np
import itertools
import math



def distance(cell: list[int, int], gem_position: list[int, int]) -> float:
    # Calculate Euclidean distance between the current cell and the gem position.
    assert len(cell) == len(gem_position) == 2, f'[E] Cell and gem_position must be in 2dimensions.'
    distance: float = math.sqrt(((gem_position[0] - cell[0]) ** 2) + ((gem_position[1] - cell[1]) ** 2))
    sigma: float = 0.5
    noise: float = np.random.normal(0, sigma)
    return distance + noise


# à chaque fois, on reçoit les distances du sonar vers les gemmes (position exacte, le sonar sent ou elles sont).
# 1. On génère toutes les permutations des positions de n gemmes possibles, et on va estimer à quel point c'est probable que
# ça soit ça, compte tenu de nos observations.
# 2. Pour chacune de ces possibilités, on vérifie la valeur de d, l'écart entre la distance mesurée via le sonar pour la vraie position
# et la distance mesurée via le sonar pour la position qu'on teste. Si on est très proche, alors d très petit.
# 3. Puisqu'on a une fonction 2^-d, plus d est petit (bon guess), plus likelyhood auguemente.
# 4. On veut mettre à jour nos croyances stockées dans la matrice dans BayesNetwork.G. Pour ce-faire, on va initialiser
# une matrice de zéros, à laquelle on va ajouter les vraisemblances pour chacune des positions possibles des gemmes. On se retrouve
# avec une carte indiquant les probabilités que les gemmes se trouvent en i, j. On additionne cette matrice à la matrice de croyances.
# 5. On obtient alors la matrice avec des zones "chaudes" là ou les vraisamblances sont souvent correctes et des zones froides
# là ou elles sont très mauvaises.


class BayesianNetwork:

    def __init__(self, grid_size: int, n_gems: int) -> None:
        
        self.grid_size: int = grid_size
        self.n_gems: int = n_gems
        self.G: np.ndarray = np.ones((self.grid_size, self.grid_size)) / self.grid_size ** 2
    
    def likelihood(self, current_cell: list[int, int], distances: list[float], gem_positions: list[list[int, int]]) -> float:
        # Compute likelihood of observing given distances, given gem positions.
        likelihood: float = 1.0
        for i, gem_position in enumerate(gem_positions):
            
            # gem_positions contient les noeuds G(m) des positions que peuvent prendre les gemmes.
            # On calcule les vecteurs observation vers ces G(m) afin de mettre à jour nos croyances.
            inf_distance: float = distance(current_cell, gem_position)
            sonar_distance: float = distances[i]
            d: float = abs(inf_distance - sonar_distance)  # Distance entre l'observation et la croyance.
            likelihood *= (2 ** (-d))

        return likelihood
    
    def infer(self, cell: list[int, int], distances: list[float]) -> None:
        # Update beliefs using inference by enumeration over all possible gem positions.

        # Init la matrice de croyance des positions ainsi que la liste des positions possibles dans la matrice.
        posterior: np.ndarray = np.zeros((self.grid_size, self.grid_size))
        all_positions: list[list[int, int]] = [[x, y] for x in range(self.grid_size) for y in range(self.grid_size)]

        # Pour chacune des config possibles des n gemmes;
        for gem_positions in itertools.permutations(all_positions, self.n_gems):
    
            likelihood: float = self.likelihood(current_cell=cell, distances=distances, gem_positions=gem_positions)
            
            # Pour chacune des gemmes, on met à jour le tableau de la vraisemblance 
            for gc in gem_positions:
                posterior[gc[0]][gc[1]] += likelihood


        posterior *= self.get_belief_distribution()
        self.G = posterior

        
    
    def get_belief_distribution(self) -> np.ndarray:
        # Return current belief distribution (posterior).
        G_sum: float = self.G.sum()
        if G_sum > 0: self.G /= G_sum
        return self.G


