#! /usr/bin/env python
from __future__ import print_function

import os
import math
import natu.units

def deflection_tangent(tangent_length, radius):
    return (tangent_length**2 + radius**2)**(1.0/2.0) - radius
    # Cannot use math.hypot or math.sqrt:
    # TypeError: The quantity isn't dimensionless.
    # Cannot use numpy.hypot:
    # AttributeError: 'float' object has no attribute 'hypot'

def deflection_arc(arc_length, radius):
    return radius * (math.cos(arc_length/radius)**-1 - 1)

radius_earth = 6371.01 * natu.units.km
length = 1.0 * natu.units.km

deflection_1 = deflection_tangent(length, radius_earth)
deflection_1.display_unit = 'cm'

deflection_2 = deflection_arc(length, radius_earth)
deflection_2.display_unit = 'cm'

print(deflection_1)
print(deflection_2)
