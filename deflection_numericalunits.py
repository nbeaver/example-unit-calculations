#! /usr/bin/env python

import os
import math
import numericalunits as nu
nu.reset_units()

def deflection_1(tangent_length, radius):
    return math.hypot(tangent_length, radius) - radius

def deflection_2(arc_length, radius):
    return radius * (math.cos(arc_length/radius)**-1 - 1)

radius_earth = 6371.01 * nu.km
length = 1.0 * nu.km

deflection_1 = deflection_1(length, radius_earth) / nu.cm

deflection_2 = deflection_2(length, radius_earth) / nu.cm

with open(os.path.splitext(__file__)[0]+'.out', 'w') as f:
    f.write(str(deflection_1) + ' cm\n')
    f.write(str(deflection_2) + ' cm\n')
