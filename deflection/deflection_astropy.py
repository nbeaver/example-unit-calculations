#! /usr/bin/env python

import os
import math
import astropy.units

def deflection_tangent(tangent_length, radius):
    return (tangent_length**2 + radius**2)**(1.0/2.0) - radius
    # Cannot use math.hypot or math.sqrt:
    # TypeError: Only dimensionless scalar quantities can be converted to Python scalars

def deflection_arc(arc_length, radius):
    return radius * (math.cos(arc_length/radius)**-1 - 1)

radius_earth = 6371.01 * astropy.units.km
length = 1.0 * astropy.units.km

deflection_1 = deflection_tangent(length, radius_earth).to(astropy.units.cm)

deflection_2 = deflection_arc(length, radius_earth).to(astropy.units.cm)

with open(os.path.splitext(__file__)[0]+'.out', 'w') as f:
    f.write(str(deflection_1) + '\n')
    f.write(str(deflection_2) + '\n')
