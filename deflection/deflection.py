#! /usr/bin/env python
from __future__ import print_function

import os
import math

def deflection_tangent(tangent_length, radius):
    return math.hypot(tangent_length, radius) - radius

def deflection_arc(arc_length, radius):
    return radius * (math.cos(arc_length/radius)**-1 - 1)

radius_earth = 6371.01 # km
length = 1.0 # km

km_to_cm = 1e3/1e-2

deflection_1 = km_to_cm * deflection_tangent(length, radius_earth)

deflection_2 = km_to_cm * deflection_arc(length, radius_earth)

print(deflection_1)
print(deflection_2)
