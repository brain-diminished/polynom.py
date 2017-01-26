# Polynom.py

*An implementation for polynom objects, aiming to ease writing, making it as natural as possible.*

## How to use
You can instanciate a polynom using class constructor, as following:
```python
P = Polynom(0, 4, 3) # P(X) = 4 X + 3 X^2
P = Polynom([0, 4, 3])
P = Polynom((0, 4, 3))
```
Of course, a `Polynom` object would not be of much use if it was not callable:
```python
print P(3)
# 39
```
But the interesting part really starts with the definition of variable `X`, which you shall not change.
```python
X = Polynom(1)
```
Why is that? Simply because once you have `X`, and using operators overloaded in class `Polynom`, you can now declare your polynoms using following writing:
```python
P = 3 - X - 10 * X**2
```
or, if you prefer:
```python
P = (3 + X) * (1 - 2 * X)
```

## Operators
- `__add__`, `+`: do I need to explain?
- `__neg__`, `-` (unary)
- `__sub__`, `-` (binary)
- `__mul__`, `*`
- `__pow__`, `**`
- `__div__`, `/`

Only remains `__floordiv__`, or `//`, as well as `__mod__`, or `%`, as the quotient and remainder of the Euclidean division of two polynoms. For now, `/` is only supposed to divide every coefficient of the polynom by a scalar value.

## String format
By default, casting a polynom to string will display the formula of the polynom, using "X" as the variable.
```python
P = (3 + X) * (1 - 2 * X)
print "P(X) = %s" % P
# P(X) = 3 + -5 X + -2 X^2
```
Indeed, not as cute as it will be (zeros should be removed, and minus signs better handled), but it's a start.

## Note
If you implement Complex numbers, class `Polynom` can work perfectly with them, as long as the basic operators are available. 

First step?
```python
i = ComplexNumber(0, 1)
```
