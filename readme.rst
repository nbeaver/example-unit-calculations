Install the prerequisites::

    sudo apt-get libudunits2-0 libudunits2-dev libhdf5-dev libnetcdf-dev python-numpy python-sympy

Install PyPi packages using the `<Makefile>`_.

Criteria that will be evaluated:

- Subjective:
  - Is it maintained?
  - Does it have a consistent interface?
  - Does it emit intelligible error messages?
  - Is the name search-engine friendly?
- Compatibility:
  - Is it Python 3 compatible?
  - the ``math`` library
  - the ``decimal`` library
  - the ``fractions`` library
  - array processing with ``numpy``
  - PyPy
- Technical:
  - Is it available on PyPi?
  - What are its dependencies?
  - Does it affect numeric precision?
  - How does it handle non-linear quantities like degrees Fahrenheit?
  - How does it handle dimensionless quantities like radians and degrees?

Criteria that will not be evaluated:

- Performance.
  - Emphasis is on readability and accuracy, not speed.

Related links:

- http://python-in-the-lab.blogspot.ca/2013/01/how-many-pints-do-you-want-units-in.html
- https://stackoverflow.com/questions/2125076/unit-conversion-in-python
