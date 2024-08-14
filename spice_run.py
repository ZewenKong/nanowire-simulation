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
    netlist.add_instructions(f".tran 0 {t} 0 1 uic")

    # Run the netlist file
    raw, log = runner.run_now(netlist)
    print('Successful/Total Simulations: ' + str(runner.okSim) + '/' + str(runner.runno))

    # Read the raw file
    raw_file = "./output/circuit_1.raw"
    LTR = RawRead(raw_file)
    x = LTR.get_trace('time')

    # nanowire voltage
    y_n = LTR.get_trace("Ix(U1:g1)")            # normal a.c.
    y_sc = LTR.get_trace("Ix(U1:n3)")           # superconducting a.c.
    y_g = LTR.get_trace("Ix(U1:n1)")            # gaussin distribution of critical current

    y_rp = LTR.get_trace("V(result-pulse)")     # result pulse voltage
    y_3v = LTR.get_trace("V(pwm-3v)")           # transformed 3V amplitude pulse

    y_lvl = LTR.get_trace("V(volt-lvl)")        # voltage level

    y_i = LTR.get_trace("I(R4)")               # current level

    s = LTR.get_steps()

    return x, y_n, y_sc, y_g, y_rp, y_3v, y_lvl, y_i, s