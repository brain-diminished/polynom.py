#!/bin/python

import os, sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + '/../src')
from polynom import *

if __name__ == '__main__':
    print "Testing Polynom.py"
    print ""
    
    # Test call
    p = Polynom(1, 2)
    print "p(X) = " + str(p)
    for (x, y) in [(0, 1), (1, 3), (2, 5)]:
        print "p(%d) = %d" % (x, y)
        assert p(x) == y

    print ""

    coefs = [7, 2, 0, -4, .0]
    p = Polynom(coefs)
    print "p(X) = " + str(p)
    for (x, y) in [(0, 7), (1, 5), (2, -21), (-5, 497)]:
        print "p(%d) = %d" % (x, p(x))
        assert p(x) == y

    # Test add/mul

    print ""

    # Test derivative
    p = Polynom(3, 8, 4, 2)
    print "p(X) = " + str(p)
    print "P'(X) = " + str(p.derive())

    print ""

    # Test primitive
    p = Polynom(3, 8, 4, 2)
    print "p(X) = " + str(p)
    print "P(X) = " + str(p.antiderive())
    print "P'(X) = " + str(p.antiderive().derive())

    print ""

    print "Test OK"
    exit(0)
