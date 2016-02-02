#! /usr/bin/env python
from __future__ import print_function

import os
import math

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

print(planck_length, 'm')
print(planck_mass, 'kg')
print(planck_time, 's')
print(planck_charge, 'C')
print(planck_temperature, 'K')
