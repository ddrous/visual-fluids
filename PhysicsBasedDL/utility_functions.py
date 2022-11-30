import numpy as np
import matplotlib
matplotlib.style.use('seaborn')
import matplotlib.pyplot as plt

## Wrapper function for matplotlib
def plot(*args, axis=None, x_label=None, y_label=None, title=None, **kwargs):
    if axis==None: 
        _, axis = plt.subplots(1, 1, figsize=(6,3))
    if x_label:
        axis.set_xlabel(x_label)
    if y_label:
        axis.set_ylabel(y_label)
    if title:
        axis.set_title(title)
    axis.plot(*args, **kwargs)
    axis.legend()
    return axis

## Data generator
def get_batch_data(X, Y, batch_size):
    size = X.shape[0]
    i = 0
    while i < size:
        inext = i + batch_size
        if inext > size: inext = size
        yield X[i:inext], Y[i:inext]
        i = inext
