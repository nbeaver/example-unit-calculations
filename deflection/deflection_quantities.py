#! /usr/bin/env python
from __future__ import print_function

import os
import math
import numpy
import quantities as pq

def deflection_tangent(tangent_length, radius):
    return numpy.hypot(tangent_length, radius) - radius
    # cannot user math.hypot or math.sqrt:
    # ValueError: Unable to convert between units of "dimensionless" and "km"

def deflection_arc(arc_length, radius):
    return radius * (math.cos(arc_length/radius)**-1 - 1)

radius_earth = 6371.01 * pq.km
length = 1.0 * pq.km

deflection_1 = deflection_tangent(length, radius_earth).rescale('cm')

deflection_2 = deflection_arc(length, radius_earth).rescale('cm')

print(deflection_1)
print(deflection_2)
