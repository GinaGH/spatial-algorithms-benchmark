# Spatial Algorithms Benchmark

This project explores spatial data structures and their performance characteristics for nearest-neighbor and range queries. It focuses on comparing KD-tree-based search with brute-force methods on large datasets.

## Motivation

Efficient spatial search is fundamental in computational geometry, simulation, machine learning, and scientific computing. This project investigates how algorithmic design impacts performance as data scales.

## Features

- KD-tree construction (balanced)
- Nearest-neighbor search
- k-nearest neighbors
- Range queries
- Performance comparison with brute-force search
- Scaling experiments (small → large datasets)

## Algorithms

### KD-tree
A binary space-partitioning structure that recursively splits points along alternating axes.

- Build time: O(n log n)
- Query time: average-case sublinear

### Brute-force
Linear scan across all points.

- Build time: O(1)
- Query time: O(n)

## Planned Work

- [ ] Implement KD-tree construction
- [ ] Add nearest-neighbor search
- [ ] Add k-nearest neighbors
- [ ] Add range queries
- [ ] Benchmark vs brute force
- [ ] Add visualization (2D)

## Tech

- Python (initial implementation)
- NumPy (optional)
- Matplotlib (for visualization)

## Future Work

- C++ implementation for performance comparison
- Higher-dimensional data
- Parallelization experiments
