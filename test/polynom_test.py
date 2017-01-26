#!/bin/python

import os, sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + '/../src')
from polynom import *

def func_add(f1, f2):
    def res(x):
        return f1(x) + f2(x)
    return res

def func_mul(f1, f2):
    def res(x):
        return f1(x) * f2(x)
    return res

def func_pow(f1, e):
    def res(x):
        return f1(x)**e
    return res

def func_sub(f1, f2):
    def res(x):
        return f1(x) - f2(x)
    return res

def func_const(a):
    def res(x):
        return a
    return res

def func_identity():
    def res(x):
        return x
    return res


def test_equality(f1, f2):
    for x in range(-10, 10):
        if f1(x) != f2(x):
            return False
    return True

if __name__ == '__main__':
    print "Testing Polynom.py"
    print ""
    
    # Test ctor
    print "----- TEST CONSTRUCTOR -----"
    p = Polynom(0, 4, 5)
    print "p(X) = " + str(p)
    p = Polynom(0, 4, 5, 0)
    print "p(X) = " + str(p)
    p = Polynom((0, 4, 5))
    print "p(X) = " + str(p)
    p = Polynom([0, 4, 5])
    print "p(X) = " + str(p)
    p = 3 + X
    print "p(X) = " + str(p)

    print ""

    # Test call
    print "----- TEST CALL -----"
    p = Polynom(1, 2)
    def f(x):
        return 1 + 2 * x;
    print "p(X) = " + str(p)
    assert test_equality(f, p)

    p = Polynom(1, 0, -1, 0, 1)
    def f(x):
        return 1 - x**2 + x**4;
    print "p(X) = " + str(p)
    assert test_equality(f, p)

    print ""

    coefs = [7, 2, 0, -4, .0]
    p = Polynom(coefs)
    print "p(X) = " + str(p)
    for (x, y) in [(0, 7), (1, 5), (2, -21), (-5, 497)]:
        print "p(%d) = %d" % (x, p(x))
        assert p(x) == y

    print ""

    # Test add/sub
    print "----- TEST ADD/SUB -----"
    p1 = Polynom(1, 5, 4, 2)
    print "p1(X) = " + str(p1)
    p2 = Polynom(-1, -1, 3, -2.0)
    print "p2(X) = " + str(p2)
    p = p1 + p2
    print "p1(X) + p2(X) = " + str(p)
    assert test_equality(func_add(p1, p2), p)
    p = p1
    p += p2
    print "p1(X) + p2(X) = " + str(p)
    assert test_equality(func_add(p1, p2), p)
    p = p1 + 3
    print "p1(X) + 3 = " + str(p)
    assert test_equality(func_add(p1, func_const(3)), p)
    p = 4 + p2
    print "4 + p2 = " + str(p)
    assert test_equality(func_add(func_const(4), p2), p)
    p = -p1
    print "-p1(X) = " + str(p)
    assert test_equality(func_mul(func_const(-1), p1), p)
    p = p1 - p2
    print "p1(X) - p2(X) = " + str(p)
    assert test_equality(func_sub(p1, p2), p)
    p = p1 - 3
    print "p1(X) - 3 = " + str(p)
    assert test_equality(func_sub(p1, func_const(3)), p)
    p = 4 - p2
    print "4 - p2(X) = " + str(p)
    assert test_equality(func_sub(func_const(4), p2), p)
    p = p1
    p -= 9
    print "p1(X) - 9 = " + str(p)
    assert test_equality(func_sub(p1, func_const(9)), p)

    print ""

    # Test mult
    print "----- TEST MULT -----"
    for (p1, p2) in [(Polynom(3, 5), Polynom(1, -2)), (Polynom(0, 5, -1), Polynom(1)), (Polynom(3, 5), Polynom(1, -2, 1, 0, 4))]:
        print "p1(X) = " + str(p1)
        print "p2(X) = " + str(p2)
        p = p1 * p2
        print "p1(X) * p2(X) = " + str(p)
        assert test_equality(func_mul(p1, p2), p)

    for (p, d) in [(Polynom(3, 5), 3), (Polynom(0, 5, -1), 7.2), (Polynom(3, 5), 1.0)]:
        print "p(X) = " + str(p)
        pdiv = p / d
        print "p(X) / %s = " % d + str(pdiv)
        assert test_equality(func_mul(p, func_const(1.0/d)), pdiv)

    print ""

    # Test mult
    print "----- TEST POW -----"
    for (p, e) in [(Polynom(1), 2), (Polynom(3, 5), 0), (Polynom(3, 5), 2), (Polynom(0, 5, -1), 3), (Polynom(3, 5), 5)]:
        print "p(X) = " + str(p)
        ppow = p**e
        print "p(X)^%d = " % e + str(ppow)
        assert test_equality(func_pow(p, e), ppow)

    print ""

    # Test derivative
    print "----- TEST DERIVATIVE -----"
    p = Polynom(3, 8, 4, 2)
    print "p(X) = " + str(p)
    print "P'(X) = " + str(p.derive())

    print ""

    # Test primitive
    print "----- TEST PRIMITIVE -----"
    p = Polynom(3, 8, 4, 2)
    print "p(X) = " + str(p)
    print "P(X) = " + str(p.antiderive())
    print "P'(X) = " + str(p.antiderive().derive())

    print ""

    print "Test OK"
    exit(0)
