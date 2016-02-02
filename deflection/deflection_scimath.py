#! /usr/bin/env python
from __future__ import print_function

import os
import math
from scimath.units.length import km, cm
from scimath.units.api import convert

def deflection_tangent(tangent_length, radius):
    return (tangent_length**2 + radius**2)**(1.0/2.0) - radius
    # cannot use math.hypot or math.sqrt:
    # scimath.units.unit.InvalidConversion: dimensional quantities ('m') cannot be converted to scalars

def deflection_arc(arc_length, radius):
    return radius * (math.cos(arc_length/radius)**-1 - 1)

radius_earth = 6371.01 * km
length = 1.0 * km

deflection_1 = convert(deflection_tangent(length, radius_earth).value, km, cm)

deflection_2 = convert(deflection_arc(length, radius_earth).value, km, cm)

print(deflection_1, cm.label)
print(deflection_2, cm.label)
