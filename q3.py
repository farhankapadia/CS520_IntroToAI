from a_star import main


grid, astar = main()
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