#! /usr/bin/env python
from __future__ import print_function

import os
import math
from simtk.unit import kilometer, centimeters

def deflection_tangent(tangent_length, radius):
    return (tangent_length**2 + radius**2)**(1.0/2.0) - radius
    # Cannot user math.hypot or math.sqrt:
    # TypeError: nb_float should return float object

def deflection_arc(arc_length, radius):
    return radius * (math.cos(arc_length/radius)**-1 - 1)

radius_earth = 6371.01 * kilometer

length = 1.0 * kilometer

deflection_1 = deflection_tangent(length, radius_earth).in_units_of(centimeters)

deflection_2 = deflection_arc(length, radius_earth).in_units_of(centimeters)

print(deflection_1)
print(deflection_2)
