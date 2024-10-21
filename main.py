

from grid import *
import random


if __name__ == "__main__":

    gems: list = random.sample([[x, y] for x in range(10) for y in range(10)], 3)
    grid = Grid(10, gems)
    coups = ["D", "R", "R", "R", "R", "D", "R", "D", "D"]
    grid.plot_moves(coups)
