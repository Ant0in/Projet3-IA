
import argparse
import random
import time
from src.grid import Grid



class Argparser:

    @staticmethod
    def parse_tuple_list(s: str) -> list[tuple[int, int]]:
        try: return [tuple(map(int, coord.strip("()").split(','))) for coord in s.split()]
        except ValueError: raise argparse.ArgumentTypeError("Gem positions must be of the form : '(x1,y1) (x2,y2)'.")

    @staticmethod
    def parse_args() -> argparse.Namespace:

        parser = argparse.ArgumentParser(description="Projet3-IA : Sonar and Bayes Net")

        parser.add_argument("--grid_size", type=int, default=10, help="Size of the grid.")
        parser.add_argument("--n_gems", type=int, default=3, help="Number of gems on the grid.")
        parser.add_argument("--moves", nargs="+", type=str, required=True, help="List of moves, e.g., 'D R R D'.")
        parser.add_argument("--verbose", action="store_true", help="Enable verbose output.")
        parser.add_argument("--gems_positions", type=Argparser.parse_tuple_list, default=None, help="Positions of gems as a list of tuples, e.g., '(1,2) (3,4)'.")

        return parser.parse_args()


def time_wrapper(func: callable) -> any:
    # Time wrapper pour décorer des fonctions style main.
    def wrapper(*args, **kwargs) -> any:
        t1: float = time.time()
        ret: any = func(*args, **kwargs)
        t2: float = time.time()
        delta_t: float = t2 - t1
        print(f"[i] Execution time for {func.__name__}: {delta_t:.4f}s.")
        return ret
    return wrapper

@time_wrapper
def main(grid_size: int, n_gems: int, moves: list[str], gems_positions: list[tuple] | None = None, verbose: bool = False) -> None:

    if not gems_positions:
        gems_positions: list[tuple] = random.sample([[x, y] for x in range(grid_size) for y in range(grid_size)], n_gems)

    grid: Grid = Grid(grid_size=grid_size, gems=gems_positions)
    grid.plot_moves(moves)



if __name__ == "__main__":
    
    # ex : python .\main.py --grid_size 10 --n_gems 3 --moves D R R R R D R D D --gems_positions "(5,2) (0,7) (8,8)"
    args: argparse.Namespace = Argparser.parse_args()
    main(grid_size=args.grid_size, n_gems=args.n_gems, moves=args.moves, gems_positions=args.gems_positions, verbose=args.verbose,)

