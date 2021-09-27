import math
import queue

q = queue.PriorityQueue(maxsize=0)

def check_bounds(coords, initial_grid):
    x = coords[0]
    y = coords[1]
    if x>=0 and y>=0 and x<=initial_grid.shape[0]-1 and y<=initial_grid.shape[1]-1:
        return True
    return False

def get_heuristic(current, goal, heu=1):
    x1 = current[0]
    y1 = current[1]
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

def a_star(initial_grid, agent_grid, start, goal):
    pass

