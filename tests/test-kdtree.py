"""
KD-Tree Test
-----------------------------------------------
This module contains a test case for comparison 
rsive implementation of a K-Dimensional Tree.
Construction Complexity: O(n log^2 n) due to sorting at each level.
Used to compare spatial query performance against brute-force methods.
"""
import sys
from pathlib import Path

# --- Environment Setup ---
# Dynamically add the project root to sys.path so we can import from /src 
# even if we run this script from inside the /tests or /benchmarks folder.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))

from src.kdtree import build_kdtree, nearest_neighbor, brute_force_nearest


def test_nearest_neighbor_matches_brute_force():
    """
    Integration test to verify that the KD-Tree search returns the same 
    result as Brute Force search.
    """

    # Sample 2D spatial data
    points = [
        (0.1, 0.2),
        (0.4, 0.4),
        (0.9, 0.8),
        (0.5, 0.5),
        (0.2, 0.1),
    ]

    target = (0.45, 0.45)

    # Build the tree (using .copy() to ensure the original list isn't mutated)
    tree = build_kdtree(points.copy())

    # Perform the search using both methods
    kd_result = nearest_neighbor(tree, target)
    brute_result = brute_force_nearest(points, target)


    # Verification: If the KD-Tree logic is correct, it must find the same 
    # nearest point as the exhaustive brute force search.
    assert kd_result == brute_result, f"Mismatch! KD: {kd_result}, Brute: {brute_result}"

if __name__ == "__main__":
    test_nearest_neighbor_matches_brute_force()
    print("Test passed!")
