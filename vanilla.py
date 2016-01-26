#! /usr/bin/env python

import math

def percent_error(expected, measured):
    return 100.0 * abs(measured - expected)/(expected)

def deflection():

    def deflection_1(tangent_length, radius):
        return math.hypot(tangent_length, radius) - radius

    def deflection_2(arc_length, radius):
        return radius * (math.cos(arc_length/radius)**-1 - 1)

    radius_earth = 6371.01 # km
    length = 1.0 # km

    km_to_cm = 1e-2/1e3

    deflection_1 = km_to_cm * deflection_1(length, radius_earth)

    expected_deflection_1 = 7.8480491 # cm

    assert percent_error(expected_deflection_1, deflection_1) < 1.0

    deflection_2 = km_to_cm * deflection_2(length, radius_earth)

    expected_deflection_2 = 7.8480493 # cm

    assert percent_error(expected_deflection_2, deflection_2) < 1.0

deflection()

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
    expected_thermal_wavelength_H2 = 7.4714277e-11 # m
    assert percent_error(expected_thermal_wavelength_H2, thermal_wavelength_H2) < 1.0

    def interparticle_spacing(mass_particle, density):
        return (mass_particle/density)**(1.0/3.0)

    interparticle_spacing_H2 = interparticle_spacing_H2(mass_H2, density_H2)
    expected_interparticle_spacing_H2 = interparticle_spacing_H2(mass_H2, density_H2)
    assert percent_error(interparticle_spacing_H2, expected_interparticle_spacing_H2) < 1.0

    def is_classical_gas(mass_particle, density, temp):
        return interparticle_spacing(mass_particle, density) > thermal_wavelength(mass_particle, temp)

    assert is_classical_gas(mass_H2, density_H2, temp_standard) == True

classical_gas()
