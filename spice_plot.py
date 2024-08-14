import matplotlib.pyplot as plt
import os

def SpicePlot(output_plot_path, x, y_n, y_sc, y_g, y_rp, y_3v, y_lvl, y_i, s):

    fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5, 1, figsize=(10, 8))
    x_max = max([x.get_wave(step).max() for step in range(len(s))])

    for step in range(len(s)):
        # normal
        ax1.plot(x.get_wave(step), y_n.get_wave(step), color='blue', linewidth=0.5)
        # superconducting
        ax1.plot(x.get_wave(step), y_sc.get_wave(step), color='green', linewidth=0.5)
        # result pulse
        ax1.plot(x.get_wave(step), y_g.get_wave(step), color='red', linewidth=0.5)
    ax1.grid(False)
    ax1.set_xlim(left=0, right=x_max)
    ax1.set_ylabel('Current')  # Set y-axis title

    for step in range(len(s)):
        ax2.plot(x.get_wave(step), y_rp.get_wave(step), color='black', linewidth=0.25)
    ax2.grid(False)
    ax2.set_xlim(left=0, right=x_max)
    ax2.set_ylabel('Voltage')

    for step in range(len(s)):
        ax3.plot(x.get_wave(step), y_3v.get_wave(step), color='black', linewidth=0.25)
    ax3.grid(False)
    ax3.set_xlim(left=0, right=x_max)
    ax3.set_ylabel('Voltage')

    for step in range(len(s)):
        ax4.plot(x.get_wave(step), y_lvl.get_wave(step), color='black', linewidth=0.5)
    ax4.grid(False)
    ax4.set_xlim(left=0, right=x_max)
    ax4.set_ylabel('Voltage')

    for step in range(len(s)):
        ax5.plot(x.get_wave(step), y_i.get_wave(step), color='black', linewidth=0.5)
    ax5.grid(False)
    ax5.set_xlim(left=0, right=x_max)
    ax5.set_ylabel('Current')

    plt.tight_layout()
    plot_path = os.path.join(output_plot_path, 'spice_plot.png')
    plt.savefig(plot_path, dpi=500)