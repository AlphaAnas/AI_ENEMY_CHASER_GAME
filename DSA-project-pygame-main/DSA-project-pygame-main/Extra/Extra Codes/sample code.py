import heapq

# Constants for colors and grid size
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GRID_SIZE = 20
GRID_WIDTH = 10
GRID_HEIGHT = 5

# Create a grid to represent the game map
grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# # Set blocked cells in the grid
grid[2][3] = 1
grid[3][3] = 1
grid[4][3] = 1
print(grid)

# # Create a node class to represent each cell in the grid
# class Node:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.parent = None
#         self.distance = float('inf')

#     def __lt__(self, other):
#         return self.distance < other.distance

# # Dijkstra's algorithm to find the path from enemy to player
# def dijkstras(di, source):
#     pq=[]
#     heapq.heapify(pq)
#     cost={}
#     preele=None
    
#     for i in di.keys():
#         cost[i]=[99999999, preele]
#     cost[source]=[0,None]
#     heapq.heappush(pq, (cost[source][0],source))
#     while pq:
#         ele=heapq.heappop(pq)
#         label=ele[1]
#         weight=[0]
#         for e in di[label]:
#             eleLabel=e[0]
#             elecost=e[1]
#             if elecost+weight<cost[eleLabel][0]:
#                 cost[eleLabel][0]= elecost+weight
#                 preele=label
#                 cost[label][1]=preele
#                 heapq.heappush(pq,(cost[label][0],label))


# print(cost)

# current='G'
# outlst=[]
# while current!='A':

#   tupl=(cost[current][1],current)
#   outlst.append(tupl)
#   current=cost[current][1]
  
# outlst.reverse()
# print(outlst,'ans')
# # def dijkstra(enemy, player, grid):
# #     open_list = []
# #     heapq.heappush(open_list, enemy)
# #     came_from = {}
# #     enemy.distance = 0

# #     while open_list:
# #         current = heapq.heappop(open_list)

# #         x, y = current.x, current.y
# #         directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # Up, down, left, right
# #         for dx, dy in directions:
# #             new_x, new_y = x + dx, y + dy
# #             if new_x >= 0 and new_x < GRID_WIDTH and new_y >= 0 and new_y < GRID_HEIGHT and not grid[new_y][new_x]:
# #                 neighbor = Node(new_x, new_y)
# #                 tentative_distance = current.distance + 1
# #                 if tentative_distance < neighbor.distance:
# #                     came_from[neighbor] = current
# #                     neighbor.distance = tentative_distance
# #                     heapq.heappush(open_list, neighbor)

# # print(open)

# # Helper function to reconstruct the path from came_from dictionary
# def reconstruct_path(came_from, current):
#     path = []
#     while current is not None:
#         path.append((current.x, current.y))
#         current = came_from.get(current)
#     path.reverse()
#     return path

# # Example usage
# enemy = Node(0, 0)
# player = Node(9, 4)

# path = dijkstra(enemy, player, grid)
# if path:
#     print("Found path:", path)
# else:
#     print("No path found.")
