import nanowire
import gaussian
import gaussian_plot
import spice_run
import spice_plot

def main():

    # Define the process path
    asc_path = './spice/circuit.asc'
    net_path = './spice/circuit.net'
    output_path = './output'
    output_plot_path = './plot'

    # Define the simulation time
    t = 1000e-9

    # Return critical current (according to the nanowire geometry)
    Ic_0 = nanowire.Nanowire()

    # Return time points and voltage level for critical current in gaussian distribution
    t_points, v_lvls = gaussian.Gaussian(Ic_0, t)
    # Plot and save
    gaussian_plot.GaussianPlot(output_plot_path, t_points, v_lvls)

    # Run the spice
    x, y_n, y_sc, y_g, y_rp, y_3v, y_lvl, y_v, y_i, s = spice_run.SpiceRun(asc_path, net_path, output_path, output_plot_path, t)
    # Plot and save
    spice_plot.SpicePlot(output_plot_path, x, y_n, y_sc, y_g, y_rp, y_3v, y_lvl, y_v, y_i, s)

if __name__ == "__main__":
    main()