import seaborn as sns
sns.set(context='talk', style='white',
        font='sans-serif', font_scale=1, color_codes=True)
sns.despine()

import matplotlib.pyplot as plt
# plt.style.use('bmh')

## Wrapper function for matplotlib
def plot(*args, ax=None, x_label=None, y_label=None, title=None, **kwargs):
    if ax==None: 
        _, ax = plt.subplots(1, 1, figsize=(8,5))
    if x_label:
        ax.set_xlabel(x_label)
    if y_label:
        ax.set_ylabel(y_label)
    if title:
        ax.set_title(title)
    ax.plot(*args, **kwargs)
    ax.legend(fontsize=12)
    plt.tight_layout()
    return ax