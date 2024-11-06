import numpy as np
import matplotlib.pyplot as plt
from src.bayesian_network import *


class Grid:

    def __init__(self, grid_size, gems):
        
        self.grid_size = grid_size
        self.gems = gems
        self.network = BayesianNetwork(self.grid_size, len(self.gems))
        self.current_position = [0, 0]
        self.network.infer(self.current_position, [distance(self.current_position, i) for i in self.gems])

    def move(self, direction):
        """Updates the agent position, and performs the inference in the Bayesian network"""
        if direction == "L": self.current_position[1] -= 1
        elif direction == "R": self.current_position[1] += 1
        elif direction == "U": self.current_position[0] -= 1
        elif direction == "D": self.current_position[0] += 1
        self.network.infer(self.current_position, [distance(self.current_position, i) for i in self.gems])
    
    def plot(self):
        """Plots the current value of G"""
        for g in self.gems:
            plt.plot(g[0], g[1], marker='v', color="white") 
        plt.plot(self.current_position[0], self.current_position[1], marker='o', color="red") 
        plt.imshow(self.network.get_belief_distribution().T)
        plt.show()

    def plot_moves(self, moves):
        """Plots the evolution of G given a series of moves"""
        fig, ax = plt.subplots(1, len(moves), figsize=(5*len(moves), 5))
        for m, move in enumerate(moves):
            self.move(move)
            for g in self.gems:
                plt.plot(g[0], g[1], marker='v', color="white") 
            ax[m].plot(self.current_position[0], self.current_position[1], marker='o', color="red") 
            ax[m].axis('off')
            ax[m].imshow(self.network.get_belief_distribution().T)
        plt.tight_layout()
        plt.show()
