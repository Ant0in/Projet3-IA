

from src.grid import *
import random


if __name__ == "__main__":

    gems: list = random.sample([[x, y] for x in range(10) for y in range(10)], 2)
    grid = Grid(10, [(5, 2), (0, 7), (8, 8)])
    coups = ["D", "R", "R", "R", "R", "D", "R", "D", "D"]
    grid.plot_moves(coups)
