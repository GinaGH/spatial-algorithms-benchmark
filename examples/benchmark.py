#
# Gina G. Healy
# KD tree benchmark 
#
# |- src/kdtree.py
# |- examples/benchmark.py
# 
# Benchmark:
#   generates random points
#   builds the KD-tree
#   queries nearest neighbor with the KD-tree
#   queries nearest neighbor with brute force
#   checks for correctness and prints whether the answers match

import sys
import os
import random
import time


# 1. Get the directory where your current script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Go up one level and then into the 'src' folder
src_path = os.path.join(current_dir, '..', 'src')

# 3. Add that calculated path to Python's search list
sys.path.append(os.path.abspath(src_path))

from kdtree import build_kdtree, nearest_neighbor, brute_force_nearest 


def generate_points(n, dim=2):
    ''' Generates random points.'''
    return [tuple(random.random() for _ in range(dim)) for _ in range(n)]


def benchmark(n, dim=2):
    ''' Benchmark: call to generate points, 
    pick a random target, 
    compare brute-force vs KD-tree time and results.'''
    points = generate_points(n, dim)
    target = tuple(random.random() for _ in range(dim))

    # KD-tree build
    start = time.perf_counter()
    tree = build_kdtree(points.copy())
    build_time = time.perf_counter() - start

    # KD-tree query
    start = time.perf_counter()
    kd_result = nearest_neighbor(tree, target)
    kd_query_time = time.perf_counter() - start

    # Brute-force query
    start = time.perf_counter()
    brute_result = brute_force_nearest(points, target)
    brute_query_time = time.perf_counter() - start

    print(f"\nNumber of points: {n}")
    print(f"KD-tree build time:      {build_time:.6f} seconds")
    print(f"KD-tree query time:      {kd_query_time:.6f} seconds")
    print(f"Brute-force query time:  {brute_query_time:.6f} seconds")
    print(f"KD-tree result:          {kd_result}")
    print(f"Brute-force result:      {brute_result}")
    print(f"Match:                   {kd_result == brute_result}")


if __name__ == "__main__":
    for n in [100, 1000, 5000, 10000]:
        benchmark(n)
