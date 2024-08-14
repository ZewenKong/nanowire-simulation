def Nanowire():

    # the quantum event is generally discrete
    # the poisson distribution is used to
    # assume the variable of superconducting nanowire's critical current

    # the mean critical current (Ic_0) will be
    # affected by the geometry of the nanowire

    # Dimensions Parameters
    length = 200e-6
    width = 100e-9
    thickness = 4e-9

    # Physics Constants
    Jc = 50e9       # critical current density
    c_factor = 1    # construction factor

    # Mean Critical Current (u)
    Ic_0 = Jc*width*thickness*c_factor

    return Ic_0

    """
# Constants
# Temperature Parameters
Tc = 10.5           # cirtical temperature
Tsub = 2            # substrate temperature
# Dimensions Parameters
length = 200e-6     # length of nanowire (200 um)
thickness = 5e-9    # thickness of nanowire (5 nm)
# Electrical/Superconducting Parameters
current = 1
sheetR = 400        # sheet resistance
Jc = 50e9           # critical current density
c_factor = 1        # construction factor

# width of nanowire (vairable)
width = 100e-9

# inductance/inductivity
ind = ((1.38e-12)*sheetR)/Tc
# kinetic inductance
k_ind = (length*ind)/width          
# critical current (without possion distribution)
Ic0 = Jc*width*thickness*c_factor

# Quantum Phase Slips
# onlt quantum phase slips are considered in this simulation
# and assume the nanowire is in a ideal condition (no noise)

a = 1               # numerical factor
e = 1.602e-19       # elementary charge
h = 1.055e-34       # reduced Planck's constant
kB = 1.381e-23      # Boltzmann constant

# zero current free energy barrier
delta_F0 = a*((Ic0)^2/e^2)*(h/(kB*Tc))
# free energy barrier associated with QPS
delta_F = delta_F0 * (1 - (current/Ic0))

Ic0 = 1.0  # Mean critical current, in units of current
delta_Ic = 0.01  # Change in critical current per phase slip
lambda_value = 5  # Average number of quantum phase slips

# Generate a sample of phase slips following a Poisson distribution
n_values = np.random.poisson(lambda_value, size=1000)

# Calculate the corresponding critical currents
Ic_values = Ic0 - delta_Ic * n_values

# Calculate the expected critical current
expected_Ic = np.mean(Ic_values)
print("Expected Critical Current: ", expected_Ic)
"""


