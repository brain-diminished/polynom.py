class Polynom:
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], list):
            args = args[0]
        if len(args) == 0:
            self.coefficients = [0]
        else:
            self.coefficients = args
            i = len(args) - 1
            while i > 0 and args[i] == 0:
                i -= 1
            self.coefficients = args[:i+1]

    def __eq__(p1, p2):
        pass

    def __ne__(p1, p2):
        pass

    def __neg__(p):
        pass

    def __add__(p1, p2):
        pass

    def __radd__(p1, p2):
        pass

    def __iadd__(p1, p2):
        pass

    def __sub__(p1, p2):
        pass

    def __rsub__(p1, p2):
        pass

    def __isub__(p1, p2):
        pass

    def __truediv__(p1, p2):
        # TODO: Algebraic fraction
        pass

    def __rtruediv__(p1, p2):
        # TODO: Algebraic fraction
        pass

    def __itruediv__(p1, p2):
        # TODO: Algebraic fraction
        pass

    def __floordiv__(p1, p2):
        pass

    def __rfloordiv__(p1, p2):
        pass

    def __ifloordiv__(p1, p2):
        pass

    def __div__(p1, p2):
        pass

    def __rdiv__(p1, p2):
        pass

    def __idiv__(p1, p2):
        pass

    def __mod__(p1, p2):
        pass

    def __rmod__(p1, p2):
        pass

    def __imod__(p1, p2):
        pass

    def __pow__(p, d):
        pass

    def __ipow__(p, d):
        pass

    def __lshift__(p, d):
        pass

    def __rshift__(p, d):
        pass

    def __call__(self, x):
        res = self.coefficients[0]
        powX = x
        for c in self.coefficients[1:]:
            res += c * powX
            powX *= x
        return res

    def derive(self):
        return Polynom([self.coefficients[i] * i for i in range(1, len(self.coefficients))])

    def antiderive(self):
        return Polynom([0] + [self.coefficients[i] / float(i + 1) for i in range(0, len(self.coefficients))])

    def integrate(self, a, b):
        prim = self.antiderive()
        return prim(b) - prim(a)

    def __str__(self):
        res = '%d' % self.coefficients[0]
        for i in range(1, len(self.coefficients)):
            res = res + " + %s X%s" % (self.coefficients[i], "^%d"%i if i > 1 else "")
        return res
