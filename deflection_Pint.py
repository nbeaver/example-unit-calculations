#! /usr/bin/env python

import os
import math
from pint import UnitRegistry

def deflection_1(tangent_length, radius):
    return math.hypot(tangent_length, radius) - radius

def deflection_2(arc_length, radius):
    return radius * (math.cos(arc_length/radius)**-1 - 1)

ureg = UnitRegistry()

radius_earth = 6371.01 * ureg.kilometers
length = 1.0 * ureg.kilometers

#deflection_1 = deflection_1(length, radius_earth) # fails

deflection_2 = deflection_2(length, radius_earth)

with open(os.path.splitext(__file__)[0]+'.out', 'w') as f:
    #f.write(str(deflection_1) + '\n')
    f.write(str(deflection_2) + '\n')
