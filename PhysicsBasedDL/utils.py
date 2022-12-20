import numpy as np

# import seaborn as sns
# sns.set(context='poster', style='white',
#         font='sans-serif', font_scale=1, color_codes=True, None)
# sns.despine()

import matplotlib.pyplot as plt
plt.style.use('bmh')

## Wrapper function for matplotlib
def plot(*args, ax=None, figsize=(6,4), x_label=None, y_label=None, title=None, y_scale='log', **kwargs):
    if ax==None: 
        if figsize==None:
            _, ax = plt.subplots(1, 1, figsize=(8,5))
        else:
            _, ax = plt.subplots(1, 1, figsize=figsize)
    if x_label:
        ax.set_xlabel(x_label)
    if y_label:
        ax.set_ylabel(y_label)
    if title:
        ax.set_title(title)
    ax.set_yscale(y_scale)
    ax.plot(*args, **kwargs)
    ax.legend(fontsize=12)
    return ax

## Data generator
def get_batch_data(X, Y, batch_size):
    size = X.shape[0]
    i = 0
    while i < size:
        inext = i + batch_size
        if inext > size: inext = size
        yield X[i:inext], Y[i:inext]
        i = inext

## A function for the Pytorch dataloader that will return data as NumPy arrays
def numpy_collate_fn(batch):
    inputs, labels = zip(*batch)
    ## NB. Make sure each element if numpy tensor first
    ## Make sure channel is moved from first axis to last, if not already
    inputs = np.moveaxis(np.stack(inputs), 1, -1)
    labels = np.moveaxis(np.stack(labels), 1, -1)
    return inputs, labels
