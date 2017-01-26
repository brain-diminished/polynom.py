class Polynom:
    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], list):
                args = args[0]
            elif isinstance(args[0], tuple):
                args = list(args[0])
        if len(args) == 0:
            self._coefs = [0]
        else:
            self._coefs = args
            i = len(args) - 1
            while i > 0 and args[i] == 0:
                i -= 1
            self._coefs = list(args[:i+1])

    @property
    def degree(self):
        return len(self._coefs) - 1

    def __eq__(p1, p2):
        if len(p1._coefs) != len(p2._coefs):
            return False
        for c1, c2 in zip(p1._coefs, p2._coefs):
            if c1 != c2:
                return False
        return True

    def __ne__(p1, p2):
        return not Polynom.__eq__(p1, p2)

    def __neg__(p):
        return Polynom([-c for c in p._coefs])

    def __add__(p1, p2):
        if not isinstance(p2, Polynom):
            p2 = Polynom(p2)
        minLen = min(len(p1._coefs), len(p2._coefs))
        return Polynom([(p1._coefs[i] + p2._coefs[i]) for i in range (minLen)] + p1._coefs[minLen:] + p2._coefs[minLen:])

    def __radd__(p1, p2):
        return Polynom.__add__(p1, p2)

    def __iadd__(p1, p2):
        return Polynom.__add__(p1, p2)

    def __sub__(p1, p2):
        return Polynom.__add__(p1, -p2)

    def __rsub__(p1, p2):
        return Polynom.__radd__(-p1, p2)

    def __isub__(p1, p2):
        return Polynom.__sub__(p1, p2)

    def __mul__(p1, p2):
        if not isinstance(p2, Polynom):
            p2 = Polynom(p2)
        coefs = []
        deg = len(p1._coefs) + len(p2._coefs) - 1
        for i in range(deg):
            j0 = max(0, i - len(p2._coefs) + 1)
            j1 = min(i + 1, len(p1._coefs))
            coef = p1._coefs[j0] * p2._coefs[i - j0]
            for j in range(j0 + 1, j1):
                coef += p1._coefs[j] * p2._coefs[i - j]
            coefs += [coef]
        return Polynom(coefs)

    def __rmul__(p1, p2):
        return Polynom.__mul__(p1, p2)

    def __imul__(p1, p2):
        return Polynom.__mul__(p1, p2)

    def __pow__(p, e):
        e = int(e)
        if e <= 0:
            return Polynom(1)
        p2 = p * p
        if e % 2 == 1:
            return Polynom.__pow__(p2, e / 2) * p
        else:
            return Polynom.__pow__(p2, e / 2)

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
        if not isinstance(p2, Polynom):
            p2 = Polynom(p2)
        if p1.degree < p2.degree:
            return p1
        pass

    def __rmod__(p1, p2):
        return Polynom.__mod__(p2, p1)

    def __imod__(p1, p2):
        # TODO: Euclidean division
        pass

    def __lshift__(p, d):
        pass

    def __rshift__(p, d):
        pass

    def __call__(self, x):
        res = self._coefs[0]
        powX = x
        for c in self._coefs[1:]:
            res += c * powX
            powX *= x
        return res

    def derive(self):
        return Polynom([self._coefs[i] * i for i in range(1, len(self._coefs))])

    def antiderive(self):
        return Polynom([0] + [self._coefs[i] / float(i + 1) for i in range(0, len(self._coefs))])

    def integrate(self, a, b):
        prim = self.antiderive()
        return prim(b) - prim(a)

    def __str__(self):
        res = '%d' % self._coefs[0]
        for i in range(1, len(self._coefs)):
            res = res + " + %s X%s" % (self._coefs[i], "^%d"%i if i > 1 else "")
        return res

_1 = Polynom(1)
_0 = Polynom(0)
X = Polynom(0, 1)
