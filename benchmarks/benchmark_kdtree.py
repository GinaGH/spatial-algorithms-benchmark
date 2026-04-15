#
# KD tree benchmark 
#

import os
import sys
import random
import time

from pathlib import Path

# --- Environment Setup ---
# Add project root to Python's import path
# This ensures the 'src' directory is visible to this script regardless of execution context
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from src.kdtree import build_kdtree, nearest_neighbor, brute_force_nearest


def generate_points(n, dim=2):
    '''
    Creates a list of N random points within a unit hypercube (0.0 to 1.0).
    Returns a list of tuples, e.g., [(0.12, 0.45), (0.98, 0.01), ...]
    '''
    return [tuple(random.random() for _ in range(dim)) for _ in range(n)]


def benchmark(n, dim=2):
    ''' 
    Conducts a performance comparison between KD-Tree and Brute Force.
    Measures: Build time, Query time, and Result accuracy.
    '''
    points = generate_points(n, dim)
    target = tuple(random.random() for _ in range(dim))


    # Phase 1: Measure KD-Tree Construction
    # Uses time.perf_counter() for high-precision timing
    start = time.perf_counter()
    tree = build_kdtree(points.copy())
    build_time = time.perf_counter() - start


    # Phase 2: Measure KD-Tree Query Speed
    # This should stay fast even as N grows (O(log n))
    start = time.perf_counter()
    kd_result = nearest_neighbor(tree, target)
    kd_query_time = time.perf_counter() - start


    # Phase 3: Measure Brute-Force Query Speed
    # This will scale linearly (O(n)), becoming the bottleneck for large N
    start = time.perf_counter()
    brute_result = brute_force_nearest(points, target)
    brute_query_time = time.perf_counter() - start

    # Output results
    print(f"\nNumber of points: {n}")
    print(f"KD-tree build time:      {build_time:.6f} seconds")
    print(f"KD-tree query time:      {kd_query_time:.6f} seconds")
    print(f"Brute-force query time:  {brute_query_time:.6f} seconds")
    print(f"KD-tree result:          {kd_result}")
    print(f"Brute-force result:      {brute_result}")
    print(f"Match:                   {'Results match!' if kd_result == brute_result else 'Results do not match.'}")


if __name__ == "__main__":
    # Test multiple scales to observe the algorithmic complexity in action.
    for n in [100, 1000, 5000, 10000, 100000]:
        benchmark(n)
