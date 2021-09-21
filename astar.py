import math
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

def get_label(x, y):
    node = chr(x+65) + str(y+1)
    return node
    
def check_bounds(x, y, initial_grid):
    if x>=0 and y>=0 and x<=initial_grid.shape[0]-1 and y<=initial_grid.shape[1]-1:
        return True
    return False

def get_heuristic(current, goal, heu=1):
    #using Manhattan distance to compute the heuristic
    x1, y1 = get_coordinates(current)
    x2, y2 = get_coordinates(goal)
    #computing heuristic 
    if heu==1:
        heuristic = abs(x1-x2) + abs(y1-y2)
    elif heu==2:
        heuristic = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    else:
        heuristic = max(abs(x1-x2), abs(y1-y2))
    return heuristic
    
def a_star(initial_grid, agent_grid, fringe, heuristic, start, goal):
    path = []
    x2, y2 = get_coordinates(goal)
    fringe = push(fringe, start, 0)
    path.append(start)
    while len(fringe) > 0:
        fringe, current = pop()
        if current == goal:
            pass #add code here later
        else:
            x1, y1 = get_coordinates(current)
            if check_bounds(x1-1, y):
                agent_grid[][]
    
    