from a_star import main
from gridworld import get_grid

initial_grid, agent_grid = get_grid(10, 0.2)

grid, astar = main(initial_grid, agent_grid)
print(grid)

try:
    parent = astar(grid, (0,0), (grid.shape[0]-1, grid.shape[1]-1))
    
    path = []
    path.append((grid.shape[0]-1, grid.shape[1]-1))
    value = parent[(grid.shape[0]-1,grid.shape[1]-1)]
    path.append(value)
    while value != (0,0):
        key = value
        value = parent[key]
        path.append(value)
    path.reverse()
    
    print(path)
except:
    print('No grid')