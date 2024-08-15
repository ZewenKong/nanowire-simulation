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
    t_points_1, v_lvls_1 = gaussian.Gaussian(Ic_0, t, 'gaussian_1') # nanowire 1
    t_points_2, v_lvls_2 = gaussian.Gaussian(Ic_0, t, 'gaussian_2') # nanowire 2

    # Plot and save
    gaussian_plot.GaussianPlot(output_plot_path, t_points_1, v_lvls_1, 'gaussian_current_1.png')
    gaussian_plot.GaussianPlot(output_plot_path, t_points_2, v_lvls_2, 'gaussian_current_2.png')

    # Run the spice
    nanowire_1, nanowire_2 = spice_run.SpiceRun(asc_path, net_path, output_path, output_plot_path, t)

    # Plot and save
    spice_plot.SpicePlot(output_plot_path, nanowire_1, nanowire_2)

if __name__ == "__main__":
    main()