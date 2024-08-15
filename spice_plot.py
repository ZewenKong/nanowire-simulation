import matplotlib.pyplot as plt
import numpy as np
import os

def SpicePlot(output_plot_path, nanowire_1, nanowire_2):

    plt.rc('font', size=6)

    x, y_n_1, y_sc_1, y_g_1, y_rp_1, y_3v_1, y_lvl_1, y_v_1, y_i_1, s = nanowire_1
    x, y_n_2, y_sc_2, y_g_2, y_rp_2, y_3v_2, y_lvl_2, y_v_2, y_i_2, s = nanowire_2

    fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(6, 1, figsize=(10, 6))
    x_max = max([x.get_wave(step).max() for step in range(len(s))])

    for step in range(len(s)):
        # nanowire 1 critical current
        ax1.plot(x.get_wave(step), y_g_1.get_wave(step), color='green', linewidth = 0.5)
        # nanowire 2 critical current
        ax1.plot(x.get_wave(step), y_g_2.get_wave(step), color='red', linewidth = 0.5)
    ax1.grid(False)
    ax1.set_xlim(left=0, right=x_max)
    ax1.set_ylabel('Critical Current', fontsize=6)

    for step in range(len(s)):
        # nanowire 1 critical current
        ax2.plot(x.get_wave(step), y_g_1.get_wave(step), color = 'green', linewidth = 0.5)
        # nanowire 2 critical current
        ax2.plot(x.get_wave(step), y_g_2.get_wave(step), color = 'red', linewidth = 0.5)
        # nanowire 1 a.c. current (fixed)
        ax2.plot(x.get_wave(step), y_n_1.get_wave(step), color = 'blue', linewidth = 0.5)
        # nanowire 2 a.c. current (controlled by nanowire 1)
        ax2.plot(x.get_wave(step), y_n_2.get_wave(step), color = 'deeppink', linewidth = 0.5)
        # nanowire 1 superconducting current
        ax2.plot(x.get_wave(step), y_sc_1.get_wave(step), color = 'black', linewidth = 0.5)
        # nanowire 2 superconducting current
        ax2.plot(x.get_wave(step), y_sc_2.get_wave(step), color = 'black', linewidth = 0.5)
    ax2.grid(False)
    ax2.set_xlim(left=0, right=x_max)
    ax2.set_ylabel('Current', fontsize=6)

    for step in range(len(s)):
        ax3.plot(x.get_wave(step), y_rp_1.get_wave(step), color = 'green', linewidth=0.5)
        ax3.plot(x.get_wave(step), y_rp_2.get_wave(step), color = 'red', linewidth=0.5)
    ax3.grid(False)
    ax3.set_xlim(left=0, right=x_max)
    ax3.set_ylabel('Volt Pulse', fontsize=6)

    for step in range(len(s)):
        ax4.plot(x.get_wave(step), y_3v_1.get_wave(step), color = 'green', linewidth=0.5)
        ax4.plot(x.get_wave(step), y_3v_2.get_wave(step), color = 'red', linewidth=0.5)
    ax4.grid(False)
    ax4.set_xlim(left=0, right=x_max)
    ax4.set_ylabel('Volt Pulse (3V)', fontsize=6)

    for step in range(len(s)):
        ax5.plot(x.get_wave(step), y_lvl_1.get_wave(step), color = 'green', linewidth=0.5)
        ax5.plot(x.get_wave(step), y_lvl_2.get_wave(step), color = 'red', linewidth=0.5)
    ax5.grid(False)
    ax5.set_xlim(left=0, right=x_max)
    ax5.set_ylabel('Volt Level', fontsize=6)

    for step in range(len(s)):
        # nanowire 1 - resistance
        v_values_1 = y_v_1.get_wave(step)
        i_values_1 = y_i_1.get_wave(step)
        y_divided_1 = [0 if i == 0 or np.isnan(i) else v / i for v, i in zip(v_values_1, i_values_1)]
        # nanowire 2 - resistance
        v_values_2 = y_v_2.get_wave(step)
        i_values_2 = y_i_2.get_wave(step)
        y_divided_2 = [0 if i == 0 or np.isnan(i) else v / i for v, i in zip(v_values_2, i_values_2)]
        # plot
        ax6.plot(x.get_wave(step), y_divided_1, color = 'green', linewidth=0.5)
        ax6.plot(x.get_wave(step), y_divided_2, color = 'red', linewidth=0.5)
    ax6.grid(False)
    ax6.set_xlim(left=0, right=x_max)
    ax6.set_ylabel('Resistance', fontsize=6)

    plt.tight_layout()
    plot_path = os.path.join(output_plot_path, 'spice_plot.png')
    plt.savefig(plot_path, dpi=500)
    plt.show()
