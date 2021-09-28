import math
import queue
import numpy as np
from gridworld import get_grid

initial_grid, agent_grid = get_grid()
print(initial_grid)

def check_bounds(x, y, initial_grid):
    if x>=0 and y>=0 and x<=initial_grid.shape[0]-1 and y<=initial_grid.shape[1]-1:
        return True
    return False

def get_heuristic(goal, x1, y1, heu=1):
    x2 = goal[0]
    y2 = goal[1]
    
    #Manhattan Distance
    if heu==1:
        heuristic = abs(x1-x2) + abs(y1-y2)
    #Euclidean Distance
    elif heu==2:
        heuristic = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    #Chebyshev Distance
    elif heu==3:
        heuristic = max(abs(x1-x2), abs(y1-y2))
        
    return heuristic

def get_coordinates(node):
    x = node[0]
    y = node[1]
    return x, y

def a_star(initial_grid, agent_grid, start, goal):
    q = queue.PriorityQueue(maxsize=0)
    parent = {}
    visited = []
    g = {}
    x1, y1 = get_coordinates(start)
    h = get_heuristic(goal, x1, y1)
    g[start] = 0
    f = g[start] + h
    q.put((f, start))
    visited.append(start)
    while not q.empty():
        current = q.get()[1]
        x1, y1 = get_coordinates(current)
        
        if current == goal:
            return parent
        
        else:
            if check_bounds(x1+1, y1, initial_grid) and not math.isinf(agent_grid[x1+1][y1]) and (x1+1, y1) not in visited:
                parent[(x1+1, y1)] = current
                visited.append((x1+1, y1))
                g[(x1+1, y1)] = g[current] + 1
                h = get_heuristic(goal, x1+1, y1)
                f = g[(x1+1, y1)] + h
                q.put((f, (x1+1, y1)))
                
            if check_bounds(x1, y1+1, initial_grid) and not math.isinf(agent_grid[x1][y1+1]) and (x1, y1+1) not in visited:
                parent[(x1, y1+1)] = current
                visited.append((x1, y1+1))
                g[(x1, y1+1)] = g[current] + 1
                h = get_heuristic(goal, x1, y1+1)
                f = g[(x1, y1+1)] + h
                q.put((f, (x1, y1+1)))
                
            if check_bounds(x1-1, y1, initial_grid) and not math.isinf(agent_grid[x1-1][y1]) and (x1-1, y1) not in visited:
                parent[(x1-1, y1)] = current
                visited.append((x1-1, y1))
                g[(x1-1, y1)] = g[current] + 1
                h = get_heuristic(goal, x1-1, y1)
                f = g[(x1-1, y1)] + h
                q.put((f, (x1-1, y1)))
                
            if check_bounds(x1, y1-1, initial_grid) and not math.isinf(agent_grid[x1][y1-1]) and (x1, y1-1) not in visited:
                parent[(x1, y1-1)] = current
                visited.append((x1, y1-1))
                g[(x1, y1-1)] = g[current] + 1
                h = get_heuristic(goal, x1, y1-1)
                f = g[(x1, y1-1)] + h
                q.put((f, (x1, y1-1)))
            
    return {}

def execution(initial_grid, agent_grid, start, goal, path=[]):
    parent = a_star(initial_grid, agent_grid, start, goal) 
    new_path = []
    if len(parent) == 0:
        print('No path')
        return
    else:
        new_path.append(goal)
        value = parent[goal]
        new_path.append(value)
        while value != start:
            key = value
            value = parent[key]
            new_path.append(value)
        new_path.reverse()
        for i in new_path:
            path.append(i)
        for j, i in enumerate(path):
            x, y = get_coordinates(i)
            if not math.isinf(initial_grid[x][y]):
                if check_bounds(x+1, y, initial_grid) and math.isinf(initial_grid[x+1][y]):
                    agent_grid[x+1][y] = math.inf
                if check_bounds(x, y+1, initial_grid) and math.isinf(initial_grid[x][y+1]):
                    agent_grid[x][y+1] = math.inf
                if check_bounds(x-1, y, initial_grid) and math.isinf(initial_grid[x-1][y]):
                    agent_grid[x-1][y] = math.inf
                if check_bounds(x, y-1, initial_grid) and math.isinf(initial_grid[x][y-1]):
                    agent_grid[x][y-1] = math.inf
            else:
                agent_grid[x][y] = math.inf
                for k in range(j, len(path)):
                    path.pop()
                    
                return execution(initial_grid, agent_grid, path[j-1], goal, path=path)
    print(path)
     

    
execution(initial_grid, agent_grid, (0,0), (initial_grid.shape[0]-1, initial_grid.shape[1]-1))
