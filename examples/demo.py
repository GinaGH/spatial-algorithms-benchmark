#
# KD tree demo
#

import sys
import random

from pathlib import Path

# --- Environment Setup ---
# Locate the project root so we can import the 'src' folder
# This allows the demo to run from anywhere within the repository
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

# Import core KD-Tree functionality
from src.kdtree import build_kdtree, nearest_neighbor

# 1. Setup Sample Data
# Generate a small set of 20 random 2D points for demonstration
points = [(random.random(), random.random()) for _ in range(20)]

# 2. Build the Tree
# The build_kdtree function organizes points for efficient spatial querying
tree = build_kdtree(points)
print("KD-Tree constructed with", len(points), "points")

# 3. Perform a Search 
# Find the nearest neighbor to the target point
# defined at the center of the unit square
target = (0.5, 0.5)
nn = nearest_neighbor(tree, target)

# 4. Display Results
print("-" * 30)
print(f"    Target Point:   {target}")
print(f"Nearest Neighbor:   {nn}")
print("-" * 30)
