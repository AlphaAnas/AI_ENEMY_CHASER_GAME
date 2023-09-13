import heapq
from pathfinding.core.grid import Grid
from pathfinding.finder.dijkstra import DijkstraFinder

import sys
from heapq import heappush, heappop

def dijsktra(graph,src,dest):
    inf = sys.maxsize
    node_data={}
    for i in graph:
        node_data[i]={'cost':inf,'pred':[]}
    node_data[src]['cost'] = 0
    visited = []
    min_heap = []
    heappush(min_heap,(node_data[src]['cost'],src))
    while min_heap:
        temp = heappop(min_heap)[1]
        if temp not in visited: # TODO: Reassign source
            visited.append(temp)
            for j in graph[temp]:
                if j[0] not in visited:
                    cost = node_data[temp]['cost'] + j[1]
                    if cost < node_data[j[0]]['cost']:
                        node_data[j[0]]['cost'] = cost
                        node_data[j[0]]['pred'] = node_data[temp]['pred'] + [temp]
                    elif cost == node_data[j[0]]['cost']:
                        node_data[j[0]]['cost'] = cost
                        node_data[j[0]]['pred'] = min(node_data[temp]['pred'] + [temp],node_data[j[0]]['pred'], key=lambda i:len(i))
                    heappush(min_heap,(node_data[j[0]]['cost'],j[0]))
        
    # print("Shortest Distance: " + str(node_data[dest]['cost']))
    return list(node_data[dest]['pred'] + [dest])

# def getShortestPath(G,source,destination): #djikstras...
#   queue = [] ; visited = []
#   cost = {} ; route=[] ; temp = []
#   d=destination
#   for node in G:
#     cost[node] = float('inf')
#   cost[source] = 0
#   heapq.heappush(queue,(cost[source],source)) 
#   while queue:
#     p = heapq.heappop(queue) # p[0] is cost ; p[1] is node
#     if p[1] not in visited:
#       visited.append(p[1])
#       for label in G[p[1]]: # label[0] is node ; label[1] is cost
#         if label[0] not in visited:
#           new_cost = cost[p[1]] + label[1]
#           if new_cost < cost[label[0]]:
#             temp.append((p[1],label[0])) # routes, need to 'sort' them later from destination to source.
#             cost[label[0]] = new_cost
#           heapq.heappush(queue,(cost[label[0]],label[0]))
#   for something in temp[::-1]:
#     if something[1]==d:
#       route.append(something)
#       d=something[0]
#   return route[::-1]
# OURS
matrix = [[1,1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,1,1]]

graph={}
matrix_length=len(matrix)
for i in range(matrix_length):
    for j in range(matrix_length):
        neighbours=[]
        if i-1>=0:
            neighbours.append(((i-1,j),matrix[i][j]))
        if i+1 <matrix_length:
            neighbours.append(((i+1,j),matrix[i][j]))
        if j-1>=0:
            neighbours.append(((i,j-1),matrix[i][j]))     
        if j+1 <matrix_length:
            neighbours.append(((i,j+1),matrix[i][j]))
        graph[(i,j)]=neighbours
# MODULE
grid = Grid(matrix = matrix)
finder = DijkstraFinder()
path , runs = finder.find_path(grid.node(1,0),grid.node(0,7), grid)
for i in graph:
    print(i,graph[i])
# print(dijsktra(graph,(1,0),(0,7)))
# print(path)