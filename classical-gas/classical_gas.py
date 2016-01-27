#! /usr/bin/env python

import os
import math

def thermal_wavelength(mass_particle, temp):
    pi = math.pi
    h = 6.6260696e-34 # kg m^2 / s
    k_B = 1.3806488e-23 # kg m^2 / K s^2
    return h / math.sqrt(2 * pi * mass_particle * k_B * temp)


def interparticle_spacing(mass_particle, density):
    return (mass_particle/density)**(1.0/3.0)

density_H2 = 0.09 # kg/m^3
amu = 1.6605389e-27 # kg
mass_H2 = 2*amu
temp_standard = 273 # K
thermal_wavelength_H2 = thermal_wavelength(mass_H2, temp_standard)
interparticle_spacing_H2 = interparticle_spacing(mass_H2, density_H2)

with open(os.path.splitext(__file__)[0]+'.out', 'w') as f:
    f.write(str(thermal_wavelength) + ' m\n')
    f.write(str(interparticle_spacing) + ' m\n')
