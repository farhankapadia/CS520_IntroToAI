import math
import queue

def check_bounds(x, y, initial_grid):
    if x>=0 and y>=0 and x<=initial_grid.shape[0]-1 and y<=initial_grid.shape[1]-1:
        return True
    return False


def get_coordinates(node):
    x = node[0]
    y = node[1]
    return x, y

def bfs(agent_grid, start, goal, heu):
    q = queue.PriorityQueue(maxsize=0)
    nodes_processed = 0
    parent = {}
    visited = []
    x1, y1 = get_coordinates(start)
    q.put(start)
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
                q.put((x1+1, y1))
                
            if check_bounds(x1, y1+1, agent_grid) and not math.isinf(agent_grid[x1][y1+1]) and (x1, y1+1) not in visited:
                parent[(x1, y1+1)] = current
                visited.append((x1, y1+1))
                q.put((x1, y1+1))
                
            if check_bounds(x1-1, y1, agent_grid) and not math.isinf(agent_grid[x1-1][y1]) and (x1-1, y1) not in visited:
                parent[(x1-1, y1)] = current
                visited.append((x1-1, y1))
                q.put((x1-1, y1))
                
            if check_bounds(x1, y1-1, agent_grid) and not math.isinf(agent_grid[x1][y1-1]) and (x1, y1-1) not in visited:
                parent[(x1, y1-1)] = current
                visited.append((x1, y1-1))
                q.put((x1, y1-1))
            
    return {}, nodes_processed