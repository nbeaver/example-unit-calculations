#! /usr/bin/env python

import math

def isclose(a, b, rel_tol=1e-9, abs_tol=0.0):
    # Until ptyhon3.5 is more widely available.
    # https://www.python.org/dev/peps/pep-0485/#proposed-implementation
    return abs(a-b) <= max( rel_tol * max(abs(a), abs(b)), abs_tol )

def assert_isclose(a, b):
    assert isclose(a, b), '{} != {}'.format(a, b)

def deflection():

    def deflection_1(tangent_length, radius):
        return math.hypot(tangent_length, radius) - radius

    def deflection_2(arc_length, radius):
        return radius * (math.cos(arc_length/radius)**-1 - 1)

    radius_earth = 6371.01 # km
    length = 1.0 # km

    km_to_cm = 1e3/1e-2

    deflection_1 = km_to_cm * deflection_1(length, radius_earth)

    deflection_1_expected = 7.84804915384 # cm

    assert_isclose(deflection_1, deflection_1_expected)

    deflection_2 = km_to_cm * deflection_2(length, radius_earth)

    deflection_2_expected = 7.8480493 # cm

    assert_isclose(deflection_2, deflection_2_expected)

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

def planck_units():

    hbar = 1.0545717e-34 # kg m^2 / s
    G = 6.67384e-11 # m^3 / kg s^2
    c = 2.99792458e8 # m/s
    epsilon0 = 8.8541878e-12 # A^2 s^4 / kg m^3
    k_B = 1.3806488e-23 # kg m^2 / K s^2
    pi = math.pi

    planck_length = math.sqrt(hbar * G / c**3)
    planck_mass = math.sqrt(hbar * G / c**3)
    planck_time = planck_length / c
    planck_charge = math.sqrt(4*pi*epsilon0*hbar*c)
    planck_temperature = planck_mass * c**2 / k_B

def geosynchronous_orbit():
    G = 6.67384e-11 # m^3 / kg s^2
    mass_earth = 5.9742412e+24 # kg
    revolution = 2 * math.pi # radian
    siderealday = 86164.09054 # s
    radius_earth = 6378136.49 # m

    orbital_altitude = (G * mass_earth / (revolution/siderealday)**2)**(1.0/3.0) - radius_earth

    orbital_altitude_expected = 3.57899416262e7 # m

    assert_isclose(orbital_altitude, orbital_altitude_expected)

deflection()
classical_gas()
planck_units()
geosynchronous_orbit()
