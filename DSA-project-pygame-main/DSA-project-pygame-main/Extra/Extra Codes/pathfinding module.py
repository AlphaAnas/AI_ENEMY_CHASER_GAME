# https://www.youtube.com/watch?v=8SigT_jhz4I

# example_grid = [
#     [1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 0, 1, 1, 1, 1],
# ]

# pathfinding module

from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from pathfinding.finder.dijkstra import DijkstraFinder
from pathfinding.core.diagonal_movement import DiagonalMovement

matrix = [
    [1, 1, 5, 1, 1, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1],
]

# Grid
grid = Grid(matrix = matrix)

# Start & End Cell
start = grid.node(0,0)
end = grid.node(5,2)

# creating finder
finder = DijkstraFinder(diagonal_movement = DiagonalMovement.always) # enable diagonal moving as well.

# find the path using Finder
path , runs = finder.find_path(start, end, grid)

# print the result
print(path)
print(runs)
