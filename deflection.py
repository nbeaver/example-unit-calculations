#! /usr/bin/env python

import math
import shared

def deflection_1(tangent_length, radius):
    return math.hypot(tangent_length, radius) - radius

def deflection_2(arc_length, radius):
    return radius * (math.cos(arc_length/radius)**-1 - 1)

radius_earth = 6371.01 # km
length = 1.0 # km

km_to_cm = 1e3/1e-2

deflection_1 = km_to_cm * deflection_1(length, radius_earth)

deflection_1_expected = 7.84804915384 # cm

shared.assert_isclose(deflection_1, deflection_1_expected)

deflection_2 = km_to_cm * deflection_2(length, radius_earth)

deflection_2_expected = 7.8480493 # cm

shared.assert_isclose(deflection_2, deflection_2_expected)
