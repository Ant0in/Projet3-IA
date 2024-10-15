from grid import *

if __name__ == "__main__":
    grid = Grid(10, [(5, 2), (0, 7), (8, 8)])
    coups = ["D", "R", "R", "R", "R", "D", "R", "D", "D"]
    grid.plot_moves(coups)
