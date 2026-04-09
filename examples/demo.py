#
# Gina G. Healy
# KD tree demo
#
# |- src/kdtree.py
# |- examples/demo.py
# 

import sys
import os
from kdtree import build_kdtree, nearest_neighbor
import random

# 1. Get the directory where your current script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Go up one level and then into the 'src' folder
src_path = os.path.join(current_dir, '..', 'src')

# 3. Add that calculated path to Python's search list
sys.path.append(os.path.abspath(src_path))

# Construct a k-d tree 
points = [(random.random(), random.random()) for _ in range(20)]
tree = build_kdtree(points)
print("KD-tree constructed with", len(points), "points")

# find the nearest neighbor to the target point
target = (0.5, 0.5)
nn = nearest_neighbor(tree, target)

print("Target:", target)
print("Nearest neighbor:", nn)
