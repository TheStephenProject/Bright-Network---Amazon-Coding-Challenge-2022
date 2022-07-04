# importing relevant modules
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from random import randint
matrix = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


# creating grid
grid = Grid(matrix = matrix)

# start and end point
start = grid.node(0,0)
end = grid.node(9,9)

# uncomment from line 29 to line 39 to access phase 2
# adding 20 random obstacles
# r=0
# while r < 20: #generate 20 obstacles randomly
#     index = randint(0,9)
#     index2 = randint(0,9)
#     if index == 0 and index2 == 0:
#         matrix[index][index2] == 0
#     elif index == 9 and index2 == 9:
#         matrix[index][index2] == 0
#     elif matrix[index][index2] == 0:
#         matrix[index][index2] = 1
#         r = r + 1

# finder
finder = AStarFinder(diagonal_movement = DiagonalMovement.always)

# using the finder to find the path
path,runs = finder.find_path(start,end,grid)

# print results
print(path)
print(runs) # tells us how many times it ran through the matrix to find the shortest path
