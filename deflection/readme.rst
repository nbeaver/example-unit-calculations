This calculates the deflection of the earth's gravitational field
over a distance of 1.0 km
by assuming that the earth is a sphere with radius 6371.01 km.

The first case is where the distance is measured
along a line tangent to the earth,
where the deflection is
:math:`sqrt(x^2 + R^2) - R`

The second case is where the distance is measured
along an arc that follow the surface of the earth,
where the deflection is
:math:`R( \sec(s/R)-1 )`.

In GNU units, the first case is::

    You have: sqrt((1km)^2 + earthradius^2) - earthradius
    You want: cm
            * 7.8480491
            / 0.1274202

and the second case is::

    You have: earthradius ( 1/cos(1km/earthradius) - 1)
    You want: cm
            * 7.8480493
            / 0.1274202
