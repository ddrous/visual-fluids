import numpy as np

import matplotlib.pyplot as plt
# plt.style.use('bmh')

import seaborn as sns
sns.set(context='notebook', style='ticks',
        font='sans-serif', font_scale=1, color_codes=True, rc={"lines.linewidth": 2})

## Wrapper function for matplotlib
def plot(*args, ax=None, figsize=(6,3.5), x_label=None, y_label=None, title=None, y_scale='linear', **kwargs):
    if ax==None: 
        _, ax = plt.subplots(1, 1, figsize=figsize)
    # sns.despine(ax=ax)
    if x_label:
        ax.set_xlabel(x_label)
    if y_label:
        ax.set_ylabel(y_label)
    if title:
        ax.set_title(title)
    ax.plot(*args, **kwargs)
    ax.set_yscale(y_scale)
    ax.legend()
    plt.tight_layout()
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
