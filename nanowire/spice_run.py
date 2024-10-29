from PyLTSpice import SpiceEditor, SimRunner
from PyLTSpice import RawRead
from PyLTSpice import LTspice

def SpiceRun(asc_path, net_path, output_path, output_plot_path, t):

    # Define the LTspice simulator
    simulator = r"C:\Program Files\LTC\LTspiceXVII\XVIIx64.exe"

    # Create a netlist of the circuit
    runner = SimRunner(output_folder=output_path, simulator=LTspice)
    runner.create_netlist(asc_path)
    netlist = SpiceEditor(net_path)

    # Set simulation time
    netlist.add_instructions(f".tran 0 {t} 0 1")

    # Run the netlist file
    raw, log = runner.run_now(netlist)
    print('Successful/Total Simulations: ' + str(runner.okSim) + '/' + str(runner.runno))

    # Read the raw file
    raw_file = "./output/circuit_1.raw"
    LTR = RawRead(raw_file)
    x = LTR.get_trace('time')

    """
    Nanowire 1
    """
    y_g_1 = LTR.get_trace("Ix(U1:n1)")          # gaussin distribution of critical current

    y_n_1 = LTR.get_trace("Ix(U1:g1)")          # normal a.c.
    y_sc_1 = LTR.get_trace("Ix(U1:n3)")         # superconducting a.c.
    

    y_rp_1 = LTR.get_trace("V(result-pulse)")   # result pulse voltage
    y_3v_1 = LTR.get_trace("V(pwm-3v)")         # transformed 3V amplitude pulse

    y_lvl_1 = LTR.get_trace("V(volt-lvl)")      # voltage level

    y_v_1 = LTR.get_trace("V(volt-r4)")
    y_i_1 = LTR.get_trace("I(R4)")              # current level

    """
    Nanowire 2
    """
    y_g_2 = LTR.get_trace("Ix(U2:n1)")          # gaussin distribution of critical current

    y_n_2 = LTR.get_trace("Ix(U2:g1)")          # normal a.c.
    y_sc_2 = LTR.get_trace("Ix(U2:n3)")         # superconducting a.c.
    

    y_rp_2 = LTR.get_trace("V(result-pulse-2)") # result pulse voltage
    y_3v_2 = LTR.get_trace("V(pwm-3v-2)")       # transformed 3V amplitude pulse

    y_lvl_2 = LTR.get_trace("V(volt-lvl-2)")    # voltage level

    y_v_2 = LTR.get_trace("V(volt-r6)")
    y_i_2 = LTR.get_trace("I(R6)")              # current level

    s = LTR.get_steps()

    nanowire_1 = [x, y_n_1, y_sc_1, y_g_1, y_rp_1, y_3v_1, y_lvl_1, y_v_1, y_i_1, s]
    nanowire_2 = [x, y_n_2, y_sc_2, y_g_2, y_rp_2, y_3v_2, y_lvl_2, y_v_2, y_i_2, s]

    return nanowire_1, nanowire_2