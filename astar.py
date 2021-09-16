import numpy as np

def push(fringe, node, value):
    if node in fringe.keys():
        if value < fringe[node]:
            fringe[node] = value
    else:
        fringe[node] = value
    fringe = dict(sorted(fringe.items(), key=lambda x:x[1]))
    return fringe

def pop(fringe):
    first = list(fringe)[0]
    current = fringe.pop(first)
    return fringe, current

def get_coordinates(node):
    #assuming nodes are of the form "A1", "B3", etc.
    #extracting coordinates to work for a matrix in the form (0, 0), (1, 2), etc.
    x = ord(node[0]) - 65
    y = int(node[1]) - 1
    return x, y
    
def get_heuristic(current, goal):
    #using Manhattan distance to compute the heuristic
    x1, y1 = get_coordinates(current)
    x2, y2 = get_coordinates(goal)
    heuristic = abs(x1-x2) + abs(y1-y2)
    return heuristic
    
def a_star(initial_grid, agent_grid, fringe, heuristic):
    