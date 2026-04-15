#
# KD-Tree Visualization (2D)
# --------------------------
# Uses Matplotlib to plot a cloud of points, a target, and the identified 
# nearest neighbor to visually verify the search algorithm's accuracy
# 

import random
import matplotlib.pyplot as plt
import sys
import random

from pathlib import Path

# --- Environment Setup ---
# Dynamically add project root to path for cross-directory imports
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))


from src.kdtree import build_kdtree, nearest_neighbor

def generate_points(n):
    '''Generates N random 2D points within the range [0.0, 1.0)'''
    return [(random.random(), random.random()) for _ in range(n)]


def main():
    # Initialize data and perform search
    points = generate_points(50)
    
    # Construct KD-Tree
    tree = build_kdtree(points.copy())

    # Find the Nearest Neighbor of the Target
    target = (0.5, 0.5)
    nn = nearest_neighbor(tree, target)

    # Prepare data for plotting
    # Separate list of tuples into distinct x and y coordinate lists
    x_vals = [p[0] for p in points]
    y_vals = [p[1] for p in points]

    # Create the Visualization
    plt.figure(figsize=(8, 8))

    # Plot the full dataset
    plt.scatter(x_vals, y_vals, label="Points")

    # Highlight the Target point with an 'X'
    plt.scatter(target[0], target[1], marker="x", s=100, label="Target")

    # Highlight the found Nearest Neighbor
    plt.scatter(nn[0], nn[1], s=100, label="Nearest Neighbor")

    # Draw a dashed line between Target and Nearest Neighbor to show the distance
    plt.plot(
        [target[0], nn[0]],
        [target[1], nn[1]],
        color='blue',
        linestyle="--",
        linewidth=1,
        label="Distance Path"
    )

    # Customize the Plot
    plt.title("KD-Tree Nearest Neighbor Search (2D Visualization)")
    plt.xlabel("X-Axis")
    plt.ylabel("Y-Axis")
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.show()


if __name__ == "__main__":
    main()
