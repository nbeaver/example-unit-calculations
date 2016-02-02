#! /usr/bin/env python
from __future__ import print_function

import os
import math
import sympy
from sympy.physics import units

def deflection_tangent(tangent_length, radius):
    return sympy.sqrt(tangent_length**2 + radius**2) - radius
    # can't use math.hypot or math.sqrt:
    # TypeError: can't convert expression to float

def deflection_arc(arc_length, radius):
    return radius * (math.cos(arc_length/radius)**-1 - 1)

radius_earth = 6371.01 * units.km
length = 1.0 * units.km

# "To see a given quantity in terms of some other unit, divide by the desired unit:"

deflection_1 = deflection_tangent(length, radius_earth) / units.cm

deflection_2 = deflection_arc(length, radius_earth) / units.cm

print(deflection_1, 'cm')
print(deflection_2, 'cm')
