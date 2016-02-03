#! /usr/bin/env python
from __future__ import print_function

import os
import math

def orbital_radius(M, omega):
    G = 6.67384e-11 # m^3 / kg s^2
    return (G * M / omega**2)**(1.0/3.0)

mass_earth = 5.9742412e+24 # kg
revolution = 2 * math.pi # radian
siderealday = 86164.09054 # s
radius_earth = 6378136.49 # m

orbital_altitude = orbital_radius(mass_earth, revolution/siderealday) - radius_earth

m_to_km = 1.0/1000.0

print(orbital_altitude * m_to_km, 'km')
