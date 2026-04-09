#
# Gina G. Healy
# K-d tree demo
#
# |- src/kdtree.py
# |- examples/demo.py
# 

import sys
import os

# 1. Get the directory where your current script is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Go up one level and then into the 'src' folder
src_path = os.path.join(current_dir, '..', 'src')

# 3. Add that calculated path to Python's search list
sys.path.append(os.path.abspath(src_path))

from kdtree import build_kdtree
import random

points = [(random.random(), random.random()) for _ in range(10)]
tree = build_kdtree(points)

print("KD-tree constructed with", len(points), "points")
