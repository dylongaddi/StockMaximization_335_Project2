## Contact Information
- Robert Olivares
- Email: robertolivares@csu.fullerton.edu

- Dylon Gaddi
- Email: dylongaddi@csu.fullerton.edu

# Stock Purchase Maximization Project

## Overview
This project implements two algorithms to solve the Stock Purchase Maximization Problem: Exhaustive Search and Dynamic Programming. The goal is to maximize the number of stocks an investor can purchase with a limited amount of financial resources.

## Files Description
- `ExhaustiveSearchStockMaximization.py`: Implements the exhaustive search algorithm through recursion.
- `DPStockMaximization.py`: Implements the dynamic programming approach.
- `main.py`: Executes both algorithms using input from `input.txt` and outputs the results to `output.txt`.
- `input.txt`: Contains input cases for the stock purchase problem.
- `output.txt`: Stores the output results from both algorithms.

## Setup and Execution
Ensure that Python 3.x is installed on your system. Place all the Python scripts (`ExhaustiveSearchStockMaximization.py`, `DPStockMaximization.py`, `main.py`) and the `input.txt` file in the same directory.

1. To execute the program, navigate to the directory containing the scripts.
2. Run `python main.py` in the command line or terminal.
3. The program will read the input from `input.txt`, process it using both algorithms, and write the results to `output.txt`.

## Input File Format
The `input.txt` file must follow this format:
- Each case consists of 4 lines.
- Line 1: The number of companies (N).
- Line 2: A list of lists where each inner list contains two integers - the number of stocks and their corresponding value for each company.
- Line 3: The total amount of money available for investment.
- Line 4: A blank line separating each case.

Example:
_______________________________
4  
[[1,2],[4,3],[3,6],[6,7]]  
12  
  
4  
[[3,2],[4,3],[5,3],[6,7]]  
10
  
_______________________________

## Output File Format
The `output.txt` file contains the results in the following format:
- Each case will have two sections of output with each line labeled.
- Section 1: The result from the Exhaustive Search algorithm.
- Section 2: The result from the Dynamic Programming algorithm.


