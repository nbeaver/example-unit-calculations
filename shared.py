#! /usr/bin/env python

def isclose(a, b, rel_tol=1e-9, abs_tol=0.0):
    # Until ptyhon3.5 is more widely available.
    # https://www.python.org/dev/peps/pep-0485/#proposed-implementation
    return abs(a-b) <= max( rel_tol * max(abs(a), abs(b)), abs_tol )

def assert_isclose(a, b):
    assert isclose(a, b), '{} != {}'.format(a, b)
