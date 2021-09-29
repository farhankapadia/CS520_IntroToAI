import numpy as np
from gridworld import get_grid
from only_astar import a_star
import matplotlib.pyplot as plt
import seaborn as sns

p = np.arange(0.01, 0.24, 0.01)
print(p)

avg = []

for i in p:
    nodes_m = []
    nodes_e = []
    nodes_c = []
    for j in range(30):
        initial_grid, agent_grid = get_grid(101, i)
        flag, nodes = a_star(initial_grid, (0, 0), (initial_grid.shape[0]-1, initial_grid.shape[1]-1), 1)
        if len(flag) == 0:
            continue
        else:
            nodes_m.append(nodes)
            flag, nodes = a_star(initial_grid, (0, 0), (initial_grid.shape[0]-1, initial_grid.shape[1]-1), 2)
            nodes_e.append(nodes)
            flag, nodes = a_star(initial_grid, (0, 0), (initial_grid.shape[0]-1, initial_grid.shape[1]-1), 3)
            nodes_c.append(nodes)
            
    avg.append(sum(nodes_m)/len(nodes_m))
    avg.append(sum(nodes_e)/len(nodes_e))
    avg.append(sum(nodes_c)/len(nodes_c))
            

    
labels = [["Manhattan", "Euclidean", "Chebyshev"]*len(p)]
labels = labels[0]

p = np.repeat(p, 3)
p = [str(i) for i in p]

raw_data = {'x':p, 'y':avg, 'category':labels}

plt.xlabel('Distances')
plt.xticks(rotation=90)
plt.ylabel('No. of nodes processed')

sns.barplot(x='x', y='y', hue='category', data=raw_data)
plt.show()

