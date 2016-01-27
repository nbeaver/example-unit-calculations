#! /usr/bin/env python

import math

def deflection_1(tangent_length, radius):
    return math.hypot(tangent_length, radius) - radius

def deflection_2(arc_length, radius):
    return radius * (math.cos(arc_length/radius)**-1 - 1)

radius_earth = 6371.01 # km
length = 1.0 # km

km_to_cm = 1e3/1e-2

deflection_1 = km_to_cm * deflection_1(length, radius_earth)

deflection_2 = km_to_cm * deflection_2(length, radius_earth)

with open("deflection.out", 'w') as f:
    f.write(str(deflection_1) + ' cm\n')
    f.write(str(deflection_2) + ' cm\n')
