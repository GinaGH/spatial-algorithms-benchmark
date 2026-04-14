# Spatial Algorithms Benchmark

This project explores spatial data structures and their performance characteristics for nearest-neighbor and range queries. It focuses on comparing KD-tree-based search with brute-force methods on large datasets.

## Motivation

Efficient spatial search is fundamental in computational geometry, simulation, machine learning, and scientific computing. This project investigates how algorithmic design impacts performance as data scales. 
## Features

- KD-tree construction (balanced)
- Nearest-neighbor search
- k-nearest neighbors (planned)
- Range queries (planned)
- Performance comparison with brute-force search
- Scaling experiments (small → large datasets)
- Add visualization (2D) (planned)

## Algorithms

### KD-tree
A binary space-partitioning structure that recursively splits points along alternating axes.

- Build time: O(n log^2 n)
- Query time:
  - Average-case: O(log n) (low dimensions)
  - Worst-case: O(n)

### Brute-force
Linear scan across all points.

- Preprocessing time: O(1) (no indexing structure)
- Query time: O(n)

## Current Status

Implemented:
- KD-tree construction (median-split, balanced)
- nearest-neighbor search
- brute-force nearest-neighbor baseline
- initial benchmarking
- basic correctness test
  
## Planned Work
- [ ] Add k-nearest neighbors
- [ ] Add range queries
- [ ] Add visualization (2D)

## Tech

- Python (initial implementation)
- Matplotlib (for visualization)

## Future Work

- C++ implementation for performance comparison
- Higher-dimensional data
- Parallelization experiments
