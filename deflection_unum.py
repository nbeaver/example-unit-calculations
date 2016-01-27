#! /usr/bin/env python

import os
import math
import unum.units
import fractions

def deflection_tangent1(tangent_length, radius):
    return math.hypot(tangent_length, radius) - radius
    # unum.ShouldBeUnitlessError: expected unitless, got 1.0 [km]

def deflection_tangent2(tangent_length, radius):
    return math.sqrt(tangent_length**2 + radius**2) - radius
    # unum.ShouldBeUnitlessError: expected unitless, got 40589769.4201 [km2]

def deflection_tangent3(tangent_length, radius):
    return (tangent_length**2 + radius**2)**(1.0/2.0) - radius

def deflection_tangent5(tangent_length, radius):
    half = fractions.Fraction(1, 2)
    return (tangent_length**2 + radius**2)**half - radius
    # TypeError: can't multiply sequence by non-int of type 'Fraction'

def deflection_arc(arc_length, radius):
    return radius * (math.cos(arc_length/radius)**-1 - 1)

radius_earth = 6371.01 * unum.units.km
length = 1.0 * unum.units.km

#deflection_1 = deflection_tangent1(length, radius_earth).asUnit(unum.units.cm)
#deflection_1 = deflection_tangent2(length, radius_earth).asUnit(unum.units.cm)
deflection_1 = deflection_tangent3(length, radius_earth).asUnit(unum.units.cm)
deflection_1 = deflection_tangent5(length, radius_earth).asUnit(unum.units.cm)

deflection_2 = deflection_arc(length, radius_earth).asUnit(unum.units.cm)

with open(os.path.splitext(__file__)[0]+'.out', 'w') as f:
    f.write(str(deflection_1) + '\n')
    f.write(str(deflection_2) + '\n')
