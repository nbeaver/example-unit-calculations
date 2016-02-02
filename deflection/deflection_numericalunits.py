#! /usr/bin/env python
from __future__ import print_function

import os
import math
import numericalunits as nu
nu.reset_units()

def deflection_tangent(tangent_length, radius):
    return math.hypot(tangent_length, radius) - radius

def deflection_arc(arc_length, radius):
    return radius * (math.cos(arc_length/radius)**-1 - 1)

radius_earth = 6371.01 * nu.km
length = 1.0 * nu.km

deflection_1 = deflection_tangent(length, radius_earth) / nu.cm

deflection_2 = deflection_arc(length, radius_earth) / nu.cm

print(deflection_1)
print(deflection_2)
