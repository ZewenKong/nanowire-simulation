import numpy as np
import os


def Gaussian(Ic_0, t, filename):

    # Poisson Distribution Parameters
    u = Ic_0        # mean value
    sigma = 0.015*u # standard deviation (the variable range)

    # LTspice Simulation
    t_simulation = t
    t_interval = 1e-9
    t_steps = t_simulation/t_interval

    # Generate Gaussian-distributed voltage levels
    t_points = np.arange(0, t_simulation + t_interval, t_interval)
    v_lvls = np.random.normal(u, sigma, len(t_points))

    pwl_data = np.column_stack((t_points, v_lvls))

    os.makedirs("pwl", exist_ok=True)
    with open(f"pwl/{filename}.txt", "w") as file:
        for t, v in zip(t_points, v_lvls):
            file.write(f"{t:.12e} {v:.12e}\n")
    
    return t_points, v_lvls