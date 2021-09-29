import numpy as np
from gridworld import get_grid
from only_astar import a_star
from a_star import main
import matplotlib.pyplot as plt
import seaborn as sns

p = np.arange(0.0, 0.24, 0.01)
print(p)

avg1 = []
avg2 = []
avg3 = []
t_nodes = []

for i in p:
    total_path = 0
    total_d_path = 0
    total_s_path = 0
    for j in range(30):
        initial_grid, agent_grid = get_grid(101, i)
        grid, astar, nodes_processed, path = main(initial_grid, agent_grid)
        if len(path) == 0:
            j -= 1
        else:
            parent = astar(grid, (0,0), (grid.shape[0]-1, grid.shape[1]-1))
            parent_2, nodes = a_star(initial_grid, (0, 0), (grid.shape[0]-1, grid.shape[1]-1), 1)
            d_path = []
            d_path.append((grid.shape[0]-1, grid.shape[1]-1))
            value = parent[(grid.shape[0]-1,grid.shape[1]-1)]
            d_path.append(value)
            while value != (0,0):
                key = value
                value = parent[key]
                d_path.append(value)
            d_path.reverse()
            
            s_path = []
            s_path.append((grid.shape[0]-1, grid.shape[1]-1))
            value = parent[(grid.shape[0]-1,grid.shape[1]-1)]
            s_path.append(value)
            while value != (0,0):
                key = value
                value = parent[key]
                s_path.append(value)
            s_path.reverse()
            
            total_path += len(path)
            total_d_path += len(d_path)
            total_s_path += len(s_path)
            
    avg_t_path = total_path / 30
    avg_d_path = total_d_path / 30
    avg_s_path = total_s_path / 30 
    
    avg1.append(avg_t_path)
    avg2.append(avg_d_path)
    avg3.append(avg_s_path)
    t_nodes.append(nodes_processed)
    