#! /usr/bin/env python
from __future__ import print_function

from astropy import units as u
from astropy.units import cds
cds.enable()

def orbital_radius(M, omega):
    return (cds.G * M / omega**2)**(1.0/3.0)

revolution = u.cycle.in_units(u.radian)

geosynchronous_orbital_radius = orbital_radius(cds.geoMass, revolution/u.sday).decompose()

earth_radius = 1 * cds.Rgeo
orbital_altitude = geosynchronous_orbital_radius - earth_radius
# throws astropy.units.core.UnitConversionError

print(orbital_altitude.to(u.km))
