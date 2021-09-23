import math
import numpy as np

def push(old_fringe, node, value):
    fringe = {}
    if node in old_fringe.keys():
        if value < old_fringe[node]:
            fringe[node] = value
    else:
        fringe[node] = value
    fringe.update(old_fringe)
    fringe = dict(sorted(fringe.items(), key=lambda x:x[1]))
    return fringe

def pop(fringe):
    first = list(fringe)[0]
    fringe.pop(first)
    return fringe, first

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
    

def a_star(initial_grid, fringe, start, goal, g=1,  path=[], visited=[], blocked=[]):
    x2, y2 = get_coordinates(goal)
    fringe = push(fringe, start, 0)
    while len(fringe) > 0:
        block_finder = {}
        inf_finder = {}
        fringe, current = pop(fringe)
        path.append(current)
        visited.append(current)
        if current == goal:
            print(path)
            print(visited)
            print(blocked)
            return True
        else:
            x1, y1 = get_coordinates(current)
            if check_bounds(x1-1, y1, initial_grid):
                label = get_label(x1-1, y1)
                h = get_heuristic(label, goal)
                f = g + h
                block_finder[label] = f  
                inf_finder[label] = initial_grid[x1-1][y1]
                if not math.isinf(initial_grid[x1-1][y1]) and label not in visited and label not in blocked:
                    fringe = push(fringe, label, f)
                elif math.isinf(initial_grid[x1-1][y1]):
                    blocked.append(label)
                    
            if check_bounds(x1+1, y1, initial_grid):
                label = get_label(x1+1, y1)
                h = get_heuristic(label, goal)
                f = g + h
                block_finder[label] = f  
                inf_finder[label] = initial_grid[x1+1][y1]
                if not math.isinf(initial_grid[x1+1][y1]) and label not in visited and label not in blocked:
                    fringe = push(fringe, label, f)
                elif math.isinf(initial_grid[x1+1][y1]):
                    blocked.append(label)
                    
            if check_bounds(x1, y1-1, initial_grid):
                label = get_label(x1, y1-1)
                h = get_heuristic(label, goal)
                f = g + h
                block_finder[label] = f  
                inf_finder[label] = initial_grid[x1][y1-1]
                if not math.isinf(initial_grid[x1][y1-1]) and label not in visited and label not in blocked:
                    fringe = push(fringe, label, f)
                elif math.isinf(initial_grid[x1][y1-1]):
                    blocked.append(label)
                    
            if check_bounds(x1, y1+1, initial_grid):
                label = get_label(x1, y1+1)
                h = get_heuristic(label, goal)
                f = g + h
                block_finder[label] = f  
                inf_finder[label] = initial_grid[x1][y1+1]
                if not math.isinf(initial_grid[x1][y1+1]) and label not in visited and label not in blocked:
                    fringe = push(fringe, label, f)
                elif math.isinf(initial_grid[x1][y1+1]):
                    blocked.append(label)
                    
            if current != start:
                if math.isinf(inf_finder[min(block_finder, key=block_finder.get)]):
                    path.pop()
                    return a_star(initial_grid, {}, path.pop(), goal, g-1, path, visited, blocked)
                else:
                    g += 1
        print(fringe)
                
    return False
            

#using a test grid for now            
grid = np.array([[1, 1, 1, 1, 1],
                 [1, 1, math.inf, 1, 1],
                 [1, 1, math.inf, math.inf, 1],
                 [1, 1, math.inf, math.inf, 1],
                 [1, 1, 1, math.inf, 1]])
start = "E3"
goal = "E5"

print(a_star(grid, {}, start, goal))
            