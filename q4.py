import numpy as np
from gridworld import get_grid
from only_astar import a_star
import matplotlib.pyplot as plt
import seaborn as sns

p = np.linspace(0.01, 0.99)
prob = []
print(p)

for i in p:
    total = 0
    for j in range(30):
        initial_grid, agent_grid = get_grid(101, i)
        flag = a_star(initial_grid, (0, 0), (initial_grid.shape[0]-1, initial_grid.shape[1]-1))
        if len(flag) == 0:
            continue
        else:
            total += 1
    ratio = total / 30
    prob.append(ratio)
    
print(prob)
plt.xlabel('Probability')
plt.ylabel('Solvability')
sns.scatterplot(x=p, y=prob)
sns.lineplot(x=p, y=prob, color='red')
plt.show()

#p0= 0.23