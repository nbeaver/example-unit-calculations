#! /usr/bin/env python

import os
import math
from natu import config
config.use_quantities = False
import natu.units

def deflection_tangent(tangent_length, radius):
    return math.hypot(tangent_length, radius) - radius

def deflection_arc(arc_length, radius):
    return radius * (math.cos(arc_length/radius)**-1 - 1)

radius_earth = 6371.01 * natu.units.km
length = 1.0 * natu.units.km

km_to_cm = natu.units.km / natu.units.cm

deflection_1 = km_to_cm * deflection_tangent(length, radius_earth)

deflection_2 = km_to_cm * deflection_arc(length, radius_earth)

with open(os.path.splitext(__file__)[0]+'.out', 'w') as f:
    f.write(str(deflection_1) + ' cm\n')
    f.write(str(deflection_2) + ' cm\n')
