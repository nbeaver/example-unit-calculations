#! /usr/bin/env python
from __future__ import print_function

import os
import math
from magnitude import mg

def deflection_tangent(tangent_length, radius):
    return (tangent_length**2 + radius**2)**(1.0/2.0) - radius
    # Cannot use math.hypot or math.sqrt:
    # magnitude.MagnitudeError: Incompatible units: [1, 0, 0, 0, 0, 0, 0, 0, 0] and [0, 0, 0, 0, 0, 0, 0, 0, 0]
    # Cannot use numpy.hypot:
    # AttributeError: Magnitude instance has no attribute 'hypot'

def deflection_arc(arc_length, radius):
    return radius * (math.cos(arc_length/radius)**-1 - 1)

radius_earth = mg(6371.01, 'km')
length = mg(1, 'km')

deflection_1 = deflection_tangent(length, radius_earth).ounit('cm')
deflection_1.output_prec(10)

deflection_2 = deflection_arc(length, radius_earth).ounit('cm')
deflection_2.output_prec(10)

print(deflection_1)
print(deflection_2)
