#! /usr/bin/env python
from __future__ import print_function

import os
import math
from udunitspy import Unit

def deflection_tangent(tangent_length, radius):
    return (tangent_length**2 + radius**2)**(1.0/2.0) - radius
    # cannot use math.hypot:
    # AttributeError: Unit instance has no attribute '__float__'

def deflection_arc(arc_length, radius):
    return radius * (math.cos(arc_length/radius)**-1 - 1)

radius_earth = 6371.01 * Unit('km')
length = 1.0 * Unit('km')

#deflection_1 = deflection_arc(length, radius_earth)
# cannot add two squared quantities:
# TypeError: in method 'offset', argument 2 of type 'double'

#deflection_2 = deflection_arc(length, radius_earth)
# cannot use math.cos on two divided quantities:
# AttributeError: Unit instance has no attribute '__float__'
