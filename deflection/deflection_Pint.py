#! /usr/bin/env python
from __future__ import print_function

import os
import math
from pint import UnitRegistry

def deflection_tangent(tangent_length, radius):
    return (tangent_length**2 + radius**2)**(1.0/2.0) - radius
    # Cannot use math.hypot:
    # pint.unit.DimensionalityError: Cannot convert from 'kilometer' to 'dimensionless'
    # Cannot use math.sqrt:
    # pint.unit.DimensionalityError: Cannot convert from 'kilometer ** 2' to 'dimensionless'

def deflection_arc(arc_length, radius):
    return radius * (math.cos(arc_length/radius)**-1 - 1)

ureg = UnitRegistry()

radius_earth = 6371.01 * ureg.kilometers
length = 1.0 * ureg.kilometers

deflection_1 = deflection_tangent(length, radius_earth).to(ureg.centimeters)

deflection_2 = deflection_arc(length, radius_earth).to(ureg.centimeters)

print(deflection_1)
print(deflection_2)
