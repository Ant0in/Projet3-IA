# Bayesian Net - 2024

## Description

This project implements a **Bayesian Network** with a focus on **inference by enumeration** to accurately estimate gem positions within a grid. A noisy sonar sensor provides positional data, which the network uses to make these estimations. For more details, please refer to `./pdf/consignes.pdf`.

<p align="center">
  <img src="./rapport/src/intro.png" alt="intro problem" width="700"/>
  <br/>
  <strong>Instance of the Bayesian Network figuring the gem positions withing a 10x10 grid.</strong>
</p>

## Features

- **Bayesian Network Implementation**: Solves the problem using a graph-based structure called a "Bayesian Network."
- **Visualization**: Provides a visual demonstration of the inference-by-enumeration algorithm, showing how the agent estimates gem positions based on Bayesian Network predictions.



## Usage

Make sure you have `Python >= 3.11` installed.


### Running the Project

1. Clone the repository:

   ```bash
   git clone https://github.com/Ant0in/Projet3-IA.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Projet3-IA/
   ```

3. Install dependencies:
   
   ```bash
   pip install -r "requirements.txt"
   ```

4. Run the project:

   ```bash
   python ".\main.py" --grid_size 10 --n_gems 3 --moves D R R R R D R D D --gems_positions "(5,2) (0,7) (8,8)"
   ```

## License

This project is licensed under the **MIT License**. You are free to use, modify, and distribute this software.

## Acknowledgements

This project was developed for the Artificial Intelligence course `INFO-F311`. Special thanks to `Tom Lenaerts & Pascal Tribel (ULB)` for their guidance and support.

