#! /usr/bin/env python
from __future__ import print_function

import os
import math
import unum.units

def deflection_tangent(tangent_length, radius):
    return (tangent_length**2 + radius**2)**(1.0/2.0) - radius
    # cannot use math.hypot():
    # unum.ShouldBeUnitlessError: expected unitless, got 1.0 [km]
    # cannot use math.sqrt():
    # unum.ShouldBeUnitlessError: expected unitless, got 40589769.4201 [km2]
    # cannot use numpy.hypot:
    # AttributeError: 'Unum' object has no attribute 'hypot'

def deflection_arc(arc_length, radius):
    return radius * (math.cos(arc_length/radius)**-1 - 1)

radius_earth = 6371.01 * unum.units.km
length = 1.0 * unum.units.km

deflection_1 = deflection_tangent(length, radius_earth).asUnit(unum.units.cm)

deflection_2 = deflection_arc(length, radius_earth).asUnit(unum.units.cm)

print(deflection_1)
print(deflection_2)
