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