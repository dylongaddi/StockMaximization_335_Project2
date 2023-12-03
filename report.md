# Report: Stock Purchase Maximization Project

## Group Information
- **Members:** Dylon Gaddi, Robert Olivares
- **Emails:** dylongaddi@csu.fullerton.edu, robertolivares@csu.fullerton.edu


## Introduction
This report details the implementation and analysis of two algorithms - Exhaustive Search and Dynamic Programming - to solve the Stock Purchase Maximization Problem. This problem focuses on maximizing the number of stocks an investor can buy given a limited budget, without considering the future values of these stocks.

## Algorithm Implementations
### Exhaustive Search (Part A)
- **Description:** This algorithm examines all possible combinations of stock purchases and selects the one that maximizes the number of stocks within the budget limit.
- **Implementation:** The approach recursively generates all subsets of stock combinations, checks their total cost, and retains the combination with the highest stock count that is within the budget.
- **Code File:** `ExhaustiveSearchStockMaximization.py`

### Dynamic Programming (Part B)
- **Description:** The Dynamic Programming approach breaks the problem into smaller subproblems and stores their solutions to avoid redundant calculations.
- **Implementation:** It uses a two-dimensional array to store the results of subproblems, considering both the remaining budget and the current company index.
- **Code File:** `DPStockMaximization.py`

## Analysis and Observations
### Time Complexity
- **Exhaustive Search:** The time complexity is O(2^N) due to the generation of all subsets for N companies.
- **Dynamic Programming:** The time complexity is O(N*M), where N is the number of companies and M is the total investment amount, due to the iterative computation over these two dimensions.

### Performance Comparison
- The Exhaustive Search algorithm, while straightforward, is significantly slower for larger inputs due to its exponential time complexity: O(2^N)
- The Dynamic Programming approach is more efficient, especially for larger datasets, as it avoids recalculating the results of overlapping subproblems: O(N*M)
- As the number of comapnies/inputs increases, the exhaustive search algorithm will take up significantly more time than the dynamic programming approach as it does not have to generate every possible combination.

## Conclusion
Both algorithms successfully solve the Stock Purchase Maximization Problem, but the Dynamic Programming approach is superior in terms of efficiency and scalability. It is more suited for practical applications where the number of companies and investment amounts can be large.

## GitHub Repository
- https://github.com/dylongaddi/StockMaximization_335_Project2
