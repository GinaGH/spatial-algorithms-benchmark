#
# Gina G. Healy
# KD-tree test 
#
# |- src/kdtree.py
# |- tests/test_kdtree.py
# 
# 
#   test case 
#   builds the KD-tree
#   queries nearest neighbor with the KD-tree
#   queries nearest neighbor with brute force
#   checks for correctness 

import sys
import os

# 1. Get the directory where your current script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Go up one level and then into the 'src' folder
src_path = os.path.join(current_dir, '..', 'src')

# 3. Add that calculated path to Python's search list
sys.path.append(os.path.abspath(src_path))

from kdtree import build_kdtree, nearest_neighbor, brute_force_nearest 


def test_nearest_neighbor_matches_brute_force():
    points = [
        (0.1, 0.2),
        (0.4, 0.4),
        (0.9, 0.8),
        (0.5, 0.5),
        (0.2, 0.1),
    ]
    target = (0.45, 0.45)

    tree = build_kdtree(points.copy())
    kd_result = nearest_neighbor(tree, target)
    brute_result = brute_force_nearest(points, target)

    assert kd_result == brute_result
