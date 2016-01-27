#! /usr/bin/env python

import math

def isclose(a, b, rel_tol=1e-9, abs_tol=0.0):
    # Until ptyhon3.5 is more widely available.
    # https://www.python.org/dev/peps/pep-0485/#proposed-implementation
    return abs(a-b) <= max( rel_tol * max(abs(a), abs(b)), abs_tol )

def assert_isclose(a, b):
    assert isclose(a, b), '{} != {}'.format(a, b)

def geosynchronous_orbit():
    G = 6.67384e-11 # m^3 / kg s^2
    mass_earth = 5.9742412e+24 # kg
    revolution = 2 * math.pi # radian
    siderealday = 86164.09054 # s
    radius_earth = 6378136.49 # m

    orbital_altitude = (G * mass_earth / (revolution/siderealday)**2)**(1.0/3.0) - radius_earth

    orbital_altitude_expected = 3.57899416262e7 # m

    assert_isclose(orbital_altitude, orbital_altitude_expected)

geosynchronous_orbit()
