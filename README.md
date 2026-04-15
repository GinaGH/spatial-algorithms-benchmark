# Spatial Algorithms Benchmark

This project explores spatial data structures and their performance characteristics for nearest-neighbor search. It focuses on comparing KD-tree-based search with brute-force methods across varying datasets and dimensions.


## Motivation

Efficient spatial search is fundamental in computational geometry, simulation, and machine learning. This project investigates how algorithmic design impacts performance as data scales, specifically focusing on the trade-offs between construction overhead and query speed.


# Project Structure
- src/: Core KD-Tree and Brute Force logic.
- benchmarks/: Performance testing scripts for scaling analysis.
- tests/: Correctness tests using Python's `assert` statements.
- examples/: Simple demonstrations and 2D visualizations.

  
## Features

- KD-tree construction: Balanced tree using median-splitting.
- Nearest-neighbor search: Recursive search with branch pruning.
- Performance Benchmarking: High-precision timing comparing Tree vs. Brute Force.
- Visualization: 2D plotting of search results using Matplotlib.


## Complexity Analysis

### KD-Tree
A binary space-partitioning structure that recursively splits points along alternating axes.

- Build time: $O(n \log^2 n)$ (due to $O(n \log n)$ sorting at each level)
- Query time:
  - Average-case: $O(\log n)$ 
  - Worst-case: $O(n)$

### Brute-Force
Linear scan across all points.
- Build time: O(1) (no indexing structure)
- Query time: $O(n)$ (linear scan)


## Getting Started
- Install Dependencies: Run pip install -r requirements.txt to set up the necessary libraries.
- Run the Benchmark: Run python benchmarks/benchmark_kdtree.py to compare performance across different dataset sizes.
- View the Visualization: Run python examples/visualize_2D.py to see the algorithm in action in 2D. 

  
## Planned Work
- [ ] Implement k-Nearest Neighbors (k-NN)
- [ ] Optimize construction to O(n log n) using a median-finding algorithm
