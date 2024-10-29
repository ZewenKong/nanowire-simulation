# Nanowire Simulation

Achieve probabilistic programming through nanowires to explore the intersection between quantum phenomena and probabilistic programming (superconducting). This work may establish a link between quantum programming and probabilistic programming, supporting further research in this area.

This study will present an analog circuit of a nanowire implemented using Python and LTspice to simulate the probabilistic process and demonstrate the potential of nanowires for probabilistic computing. Additionally, it will provide a reference for future experimental work.

This simulation project includes the circuit designed for probabilistic programming, a sub-circuit that provides the properties of the nanowire, and the Python scripts used to generate the physical data and summarise the results.

# SNSPD Simulation

This idea is inspired from the stochastic MTJ (Magnetic Tunnelling Junction). The MTJ is characterised by its tunnelling magnetoresistance, which can be switched between high and low values by varying the angle between the magnetisation direction of the two ferromagnetic layers. The stochastic MTJ (S-MTJ) is an unstable MTJ with a free layer (broken) that has a relatively low energy barrier, allowing thermal noise to make it fluctuate between its stable states, one being parallel (P, low resistance) to the fixed layer and the other being anti-parallel (AP, high resistance). The input voltage can affect the stability of the free layer, thereby changing its resistance to vary the output voltage. This property can be used to build the stochastic neural networks for probabilistic computing.

The nanowire is cooled well below its superconducting critical temperature and biased with a DC current that is close to but less than the superconducting critical current of the nanowire. When a photon is detected (Cooper pairs are broken), a localised non-superconducting region (hotspot) with finite electrical resistance is formed. This produces a measurable voltage pulse that is approximately equal to the bias current multiplied by the load resistance. Then most of the bias current flowing through the load resistance, the hotspot cools and returns to the superconducting state. The time for the current to return to the nanowire is typically set by the inductive time constant (kinetic inductance of the nanowire divided by the impedance of the readout circuit) of the nanowire.

To investigate the potential of SNSPDs for probabilistic computing, simulating the electrical properties is necessary. Based on this, LTspice is used to study the electrical properties of SNSPDs. Then, by adding extra circuitry in LTspice and using Python for data processing and LTspice interaction, it is possible to achieve a phenomenon similar to that of stochastic MTJs.
