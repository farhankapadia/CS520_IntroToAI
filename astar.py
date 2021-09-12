import numpy as np

def push(fringe, node, value):
    if node in fringe.keys():
        if value < fringe[node]:
            fringe[node] = value
    else:
        fringe[node] = value
    fringe = dict(sorted(fringe.items(), key=lambda x:x[1]))
    return fringe
def pop(fringe):
    first = list(fringe)[0]
    current = fringe.pop(first)
    return fringe, current

