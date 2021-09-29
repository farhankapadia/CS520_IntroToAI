import math
import queue

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

def a_star(agent_grid, start, goal, heu):
    q = queue.PriorityQueue(maxsize=0)
    nodes_processed = 0
    parent = {}
    visited = []
    g = {}
    x1, y1 = get_coordinates(start)
    h = get_heuristic(goal, x1, y1, heu)
    g[start] = 0
    f = g[start] + h
    q.put((f, start))
    visited.append(start)
    while not q.empty():
        current = q.get()[1]
        nodes_processed += 1
        x1, y1 = get_coordinates(current)
        
        if current == goal:
            return parent, nodes_processed
        
        else:
            if check_bounds(x1+1, y1, agent_grid) and not math.isinf(agent_grid[x1+1][y1]) and (x1+1, y1) not in visited:
                parent[(x1+1, y1)] = current
                visited.append((x1+1, y1))
                g[(x1+1, y1)] = g[current] + 1
                h = get_heuristic(goal, x1+1, y1, heu)
                f = g[(x1+1, y1)] + h
                q.put((f, (x1+1, y1)))
                
            if check_bounds(x1, y1+1, agent_grid) and not math.isinf(agent_grid[x1][y1+1]) and (x1, y1+1) not in visited:
                parent[(x1, y1+1)] = current
                visited.append((x1, y1+1))
                g[(x1, y1+1)] = g[current] + 1
                h = get_heuristic(goal, x1, y1+1, heu)
                f = g[(x1, y1+1)] + h
                q.put((f, (x1, y1+1)))
                
            if check_bounds(x1-1, y1, agent_grid) and not math.isinf(agent_grid[x1-1][y1]) and (x1-1, y1) not in visited:
                parent[(x1-1, y1)] = current
                visited.append((x1-1, y1))
                g[(x1-1, y1)] = g[current] + 1
                h = get_heuristic(goal, x1-1, y1, heu)
                f = g[(x1-1, y1)] + h
                q.put((f, (x1-1, y1)))
                
            if check_bounds(x1, y1-1, agent_grid) and not math.isinf(agent_grid[x1][y1-1]) and (x1, y1-1) not in visited:
                parent[(x1, y1-1)] = current
                visited.append((x1, y1-1))
                g[(x1, y1-1)] = g[current] + 1
                h = get_heuristic(goal, x1, y1-1, heu)
                f = g[(x1, y1-1)] + h
                q.put((f, (x1, y1-1)))
            
    return {}, nodes_processed