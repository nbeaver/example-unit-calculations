#! /usr/bin/env sh
units --terse 'earthradius ( 1/cos(1km/earthradius) - 1)' 'cm'
units --terse 'sqrt((1km)^2 + earthradius^2) - earthradius' 'cm'
