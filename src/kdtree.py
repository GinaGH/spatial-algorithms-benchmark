#
# Gina G. Healy
# KD tree 
#
# |- src/kdtree.py
# |- examples/demo.py
# 

import math

class KDNode:
    def __init__(self, point, axis, left=None, right=None):
        self.point = point
        self.axis = axis
        self.left = left
        self.right = right


def distance(p1, p2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(p1, p2)))


def nearest_neighbor(root, target, best=None):
    if root is None:
        return best

    # Current point
    point = root.point

    # Update best if needed
    if best is None or distance(target, point) < distance(target, best):
        best = point

    axis = root.axis

    # Choose which side to explore first
    if target[axis] < point[axis]:
        next_branch = root.left
        opposite_branch = root.right
    else:
        next_branch = root.right
        opposite_branch = root.left

    # Explore the likely side
    best = nearest_neighbor(next_branch, target, best)

    # Check if we need to explore the other side
    if abs(target[axis] - point[axis]) < distance(target, best):
        best = nearest_neighbor(opposite_branch, target, best)

    return best

def build_kdtree(points, depth=0):
    if not points:
        return None

    k = len(points[0])  # dimension
    axis = depth % k

    points.sort(key=lambda x: x[axis])
    median = len(points) // 2

    return KDNode(
        point=points[median],
        axis=axis,
        left=build_kdtree(points[:median], depth + 1),
        right=build_kdtree(points[median + 1:], depth + 1)
    )
