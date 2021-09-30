from weighted_astart import main
from gridworld import get_grid
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

initial_grid, agent_grid = get_grid(101, 0.23)
weights = np.arange(1, 3, 0.2)

path_m = []
path_e = []
path_c = []
time_m = []
time_e = []
time_c = []
for i in range(len(weights)):
    grid, astar, nodes, path, time = main(initial_grid, agent_grid, weights[i], 1)
    grid1, astar1, nodes1, path1, time1 = main(initial_grid, agent_grid, weights[i], 2)
    grid2, astar2, nodes2, path2, time2 = main(initial_grid, agent_grid, weights[i], 3)
    if len(path) == 0 or len(path1) == 0 or len(path2) == 0:
        i -= 1
    else:
        path_m.append(len(path))
        path_e.append(len(path1))
        path_c.append(len(path2))
        time_m.append(time)
        time_e.append(time1)
        time_c.append(time2)
        
dict = {'path_m': path_m, 'path_e': path_e , 'path_c': path_c, 'time_m':time_m, 'time_e':time_e, 'time_c':time_c,
        'weights':weights}  
       
df = pd.DataFrame(dict) 
    
# saving the dataframe 
df.to_csv('q9.csv') 

plt.title('Manhattan Distance')
plt.xlabel('Weights')
plt.xticks(rotation=90)
plt.ylabel('Length of path')
sns.scatterplot(x=weights, y=path_m)
sns.lineplot(x=weights, y=path_m, color='red')
plt.show()

plt.title('Euclidean Distance')
plt.xlabel('Weights')
plt.xticks(rotation=90)
plt.ylabel('Length of path')
sns.scatterplot(x=weights, y=path_e)
sns.lineplot(x=weights, y=path_e, color='red')
plt.show()

plt.title('Chebyshev Distance')
plt.xlabel('Weights')
plt.xticks(rotation=90)
plt.ylabel('Length of path')
sns.scatterplot(x=weights, y=path_c)
sns.lineplot(x=weights, y=path_m, color='red')
plt.show()

plt.title('Manhattan Distance')
plt.xlabel('Weights')
plt.xticks(rotation=90)
plt.ylabel('Time')
sns.scatterplot(x=weights, y=time_m)
sns.lineplot(x=weights, y=time_m, color='red')
plt.show()

plt.title('Euclidean Distance')
plt.xlabel('Weights')
plt.xticks(rotation=90)
plt.ylabel('Time')
sns.scatterplot(x=weights, y=time_e)
sns.lineplot(x=weights, y=time_e, color='red')
plt.show()

plt.title('Chebyshev Distance')
plt.xlabel('Weights')
plt.xticks(rotation=90)
plt.ylabel('Time')
sns.scatterplot(x=weights, y=time_c)
sns.lineplot(x=weights, y=time_c, color='red')
plt.show()