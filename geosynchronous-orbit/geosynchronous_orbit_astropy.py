#! /usr/bin/env python
from __future__ import print_function

import math
from astropy import units as u
from astropy.units import cds
cds.enable()

def orbital_radius(M, omega):
    G = 1 * cds.G
    return (G * M / omega**2)**(1.0/3.0)

earth_mass = 1 * cds.geoMass
revolution = 2 * math.pi * u.radian
sidereal_day = 1 * u.sday
earth_radius = 1 * cds.Rgeo

geosynchronous_orbital_radius = orbital_radius(earth_mass, revolution/sidereal_day).decompose()

orbital_altitude = geosynchronous_orbital_radius - earth_radius
# throws astropy.units.core.UnitConversionError

print(orbital_altitude.to(u.km))
