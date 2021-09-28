import numpy as np
import math
import random

def get_grid():
    dim = int(input("Enter dimensions of the grid: "))
    p = float(input('Enter probability of blocked cells: '))
    
    agent_grid = np.ones((dim,dim))
    k = int(dim * dim * p)
    
    initial_grid = np.ones((dim,dim))
    population = []
    
    for i in range(dim):
        for j in range(dim):
            if (i==0 and j==0) or (i==dim-1 and j==dim-1):
                continue
            else:
                population.append((i, j))
                
    sample = random.sample(population, k)
    
    for i in sample:
        initial_grid[i[0]][i[1]] = math.inf
        
    return initial_grid, agent_grid
    
