This calculates the altitude of `geosynchronous orbit`_
using the equation

.. math::
    r = \sqrt[3]{
          \frac{G m}
               {(2 \pi / T)^2}
        }

where
:math:`r` is the orbital radius,
:math:`G` is the gravitational constant,
:math:`m` is the mass of the earth, and
:math:`T` is the orbital period (one sidereal day)
and subtracting the radius of the earth

.. math::
    \Delta r = r_{orbit} - r_{earth}

to find the altitude.

.. _geosynchronous orbit: https://en.wikipedia.org/wiki/Geosynchronous_orbit
