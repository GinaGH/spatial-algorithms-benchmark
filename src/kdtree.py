"""
KD-Tree Implementation for Spatial Benchmarking
-----------------------------------------------
This module contains a recursive implementation of a K-Dimensional Tree.
Construction Complexity: O(n log^2 n) due to sorting at each level.
Used to compare spatial query performance against brute-force methods.
"""
import math

class KDNode:
    """Represents a single node in a K-Dimensional tree."""
    def __init__(self, point, axis, left=None, right=None):
        self.point = point  # The actual data point (e.g., [x, y])
        self.axis = axis    # The dimension used to split at this level
        self.left = left    # Subtree with values < median
        self.right = right  # Subtree with values >= median


def build_kdtree(points, depth=0):
    """
    Recursively builds a KD-tree from a list of points.
    
    Args:
        points: List of coordinates (e.g., [[2, 3], [5, 4]])
        depth: Current recursion depth used to determine the split axis
    """
    if not points:
        return None

    # Determine split axis (x, y, z, etc.) based on current depth
    k = len(points[0])  # dimension
    axis = depth % k

    # Sort points to find the median; this ensures a balanced tree
    # Note: Sorting at every level makes construction O(n log^2 n)
    points.sort(key=lambda x: x[axis])
    median = len(points) // 2

    # Create node and recursively build the left and right subtrees
    return KDNode(
        point=points[median],
        axis=axis,
        left=build_kdtree(points[:median], depth + 1),
        right=build_kdtree(points[median + 1:], depth + 1)
    )


def distance(p1, p2):
    """
    Computes the Euclidean distance (L2 norm) between two multi-dimensional points.
    
    Formula: sqrt(sum((pi - qi)^2))
    """
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))


def squared_distance(p1, p2):
    """
    Computes the squared Euclidean distance between two points.
    
    Optimization: Skipping the square root (sqrt) is significantly faster 
    for benchmarks. Since distance comparisons (dist_a < dist_b) remain 
    consistent without the sqrt, this is preferred for nearest-neighbor searches.
    """
    return sum((a - b) ** 2 for a, b in zip(p1, p2))


def nearest_neighbor(root, target, best=None):
    """
    Finds the point in the tree closest to the target using recursive pruning
    Note: uses squared distances for performance
    """
    if root is None:
        return best

    # 1. Update the 'best' point found so far
    # Note: For the optimized version, using squared_distance here
    if best is None or squared_distance(target, root.point)< squared_distance(target, best):
        best = root.point


    # if you must - here is the traditional method
    # (note: using the square-root is not optimal for speed)
    # if best is None or distance(target, root.point) < distance(target, best):
    #    best = root.point


    axis = root.axis

    # 2. Decide the "preferred" direction to explore first
    # We head toward the branch where the target would logically live
    if target[axis] < root.point[axis]:
        next_branch = root.left
        opposite_branch = root.right
    else:
        next_branch = root.right
        opposite_branch = root.left

    # 3. Recursively search the "likely" side first
    best = nearest_neighbor(next_branch, target, best)

    # 4. Optimized Pruning Check
    # Check if we need to explore the other side
    # Does the hyper-plane (splitting line) cross the circle formed by 
    # our current best distance? If yes, the "other" side might have a closer point.
    # if abs(target[axis] - root.point[axis]) < distance(target, best):
    if (target[axis] - root.point[axis])**2 < squared_distance(target, best):
        best = nearest_neighbor(opposite_branch, target, best)

    return best


def brute_force_nearest(points, target):
    ''' Brute force nearest search. Used as a baseline method to compare against the KD-tree'''
    if not points:
        return None

    best = points[0]
    best_dist = distance(target, best)

    for point in points[1:]:
        d = distance(target, point)
        if d < best_dist:
            best = point
            best_dist = d

    return best
