import math
import queue
#from gridworld import get_grid

def main(initial_grid, agent_grid):
    #initial_grid, agent_grid = get_grid()
    print(initial_grid)
    
    def check_bounds(x, y, initial_grid):
        if x>=0 and y>=0 and x<=initial_grid.shape[0]-1 and y<=initial_grid.shape[1]-1:
            return True
        return False
    
    def get_coordinates(node):
        x = node[0]
        y = node[1]
        return x, y
    
    global nodes_processed
    nodes_processed = 0
    
    def bfs(agent_grid, start, goal):
        q = queue.Queue(maxsize=0)
        global nodes_processed
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
                return parent
            
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
                
        return {}
    
    def execution(initial_grid, agent_grid, start, goal, path=[]):
        parent = bfs(agent_grid, start, goal) 
        global nodes_processed
        new_path = []
        if len(parent) == 0:
            print('No path')
            return [], [], 0
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
        return agent_grid, path, nodes_processed
         
    
        
    new_agent_grid, path, nodes_processed = execution(initial_grid, agent_grid, (0,0), (initial_grid.shape[0]-1, initial_grid.shape[1]-1))
    return new_agent_grid, bfs, nodes_processed, path

#grid, astar = main()
