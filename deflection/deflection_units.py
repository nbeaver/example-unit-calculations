#! /usr/bin/env python

import os
import math
import fractions
from units import unit
from units.predefined import define_units
define_units()

def deflection_tangent1(tangent_length, radius):
    return math.hypot(tangent_length, radius) - radius
    # TypeError: unsupported operand type(s) for -: 'float' and 'Quantity'

def deflection_tangent2(tangent_length, radius):
    return math.sqrt(tangent_length**2 + radius**2) - radius
    # TypeError: unsupported operand type(s) for -: 'float' and 'Quantity'

def deflection_tangent3(tangent_length, radius):
    return pow(tangent_length**2 + radius**2, 1.0/2.0) - radius
    # TypeError: can't multiply sequence by non-int of type 'float'

def deflection_tangent4(tangent_length, radius):
    return (tangent_length**2 + radius**2)**(1.0/2.0) - radius
    # TypeError: can't multiply sequence by non-int of type 'float'

def deflection_tangent5(tangent_length, radius):
    half = fractions.Fraction(1, 2)
    return (tangent_length**2 + radius**2)**half - radius
    # TypeError: can't multiply sequence by non-int of type 'Fraction'

def deflection_arc(arc_length, radius):
    return radius * (math.cos(arc_length/radius)**-1 - 1)

radius_earth = unit('km')(6371.01)
length = unit('km')(1.0)

#deflection_1 = unit('cm')(deflection_tangent1(length, radius_earth))
#deflection_1 = unit('cm')(deflection_tangent2(length, radius_earth))
#deflection_1 = unit('cm')(deflection_tangent3(length, radius_earth))
#deflection_1 = unit('cm')(deflection_tangent4(length, radius_earth))
#deflection_1 = unit('cm')(deflection_tangent5(length, radius_earth))

deflection_2 = unit('cm')(deflection_arc(length, radius_earth))

with open(os.path.splitext(__file__)[0]+'.out', 'w') as f:
    #f.write(str(deflection_1) + '\n')
    f.write(str(deflection_2) + '\n')
