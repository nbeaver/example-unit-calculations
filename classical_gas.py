#! /usr/bin/env python

import math

def isclose(a, b, rel_tol=1e-9, abs_tol=0.0):
    # Until ptyhon3.5 is more widely available.
    # https://www.python.org/dev/peps/pep-0485/#proposed-implementation
    return abs(a-b) <= max( rel_tol * max(abs(a), abs(b)), abs_tol )

def assert_isclose(a, b):
    assert isclose(a, b), '{} != {}'.format(a, b)


def classical_gas():
    density_H2 = 0.09 # kg/m^3
    amu = 1.6605389e-27 # kg
    mass_H2 = 2*amu
    temp_standard = 273 # K

    def thermal_wavelength(mass_particle, temp):
        pi = math.pi
        h = 6.6260696e-34 # kg m^2 / s
        k_B = 1.3806488e-23 # kg m^2 / K s^2
        return h / math.sqrt(2 * pi * mass_particle * k_B * temp)

    thermal_wavelength_H2 = thermal_wavelength(mass_H2, temp_standard)
    thermal_wavelength_H2_expected = 7.47142774858e-11 # m
    assert_isclose(thermal_wavelength_H2, thermal_wavelength_H2_expected)

    def interparticle_spacing(mass_particle, density):
        return (mass_particle/density)**(1.0/3.0)

    interparticle_spacing_H2 = interparticle_spacing(mass_H2, density_H2)
    interparticle_spacing_H2_expected = interparticle_spacing(mass_H2, density_H2)
    assert_isclose(interparticle_spacing_H2, interparticle_spacing_H2_expected)

    def is_classical_gas(mass_particle, density, temp):
        return interparticle_spacing(mass_particle, density) > thermal_wavelength(mass_particle, temp)

    assert is_classical_gas(mass_H2, density_H2, temp_standard) == True

classical_gas()
