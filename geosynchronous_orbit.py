#! /usr/bin/env python

import math
import shared

def geosynchronous_orbit():
    G = 6.67384e-11 # m^3 / kg s^2
    mass_earth = 5.9742412e+24 # kg
    revolution = 2 * math.pi # radian
    siderealday = 86164.09054 # s
    radius_earth = 6378136.49 # m

    orbital_altitude = (G * mass_earth / (revolution/siderealday)**2)**(1.0/3.0) - radius_earth

    orbital_altitude_expected = 3.57899416262e7 # m

    shared.assert_isclose(orbital_altitude, orbital_altitude_expected)

geosynchronous_orbit()
