import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from scipy.stats import norm
import os

def GaussianPlot(output_plot_path, t_points, v_lvls):

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

    # Current as Y-axis
    colors = cm.viridis(np.linspace(0, 1, len(v_lvls)))
    for i, v in enumerate(v_lvls):
        ax1.plot([0, 1], [v, v], color=colors[i], linewidth=0.25)
    ax1.axes.get_xaxis().set_visible(False)
    ax1.set_ylabel('Current Level')

    # Crrent as X-axis
    ax2.hist(v_lvls, bins=50, color='black', alpha=0.25, density=True)
    ax2.set_xlabel('Current Level')
    ax2.axes.get_yaxis().set_visible(False)

    mean, std = norm.fit(v_lvls)
    xmin, xmax = ax2.get_xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mean, std)
    ax2.plot(x, p, 'r', linewidth=1)

    plt.tight_layout()
    plot_path = os.path.join(output_plot_path, 'gaussian_current.png')
    plt.savefig(plot_path, dpi=500)