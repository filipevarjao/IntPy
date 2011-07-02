=====
IntPy
=====

**NOTE: This project was discontinued. I’m currently with other priority
projects and I have not enough time to develop IntPy. Nobody has shown
interest in continuing this project. However, I still notice some demand
for this library, so I’ll keep this page online for those interested.
(09/21/2009).**

IntPy is a Python package providing types and functions for Maximum
Accuracy Interval Arithmetic developed by me at CIn/UFPE (Brazil)
(http://www.cin.ufpe.br).

The Interval Arithmetic is a mathematical tool to solve problems
related to numerical errors, based on an algebraic system formed by
all closed intervals of the Real Line (or rectangles of the Complex Plane)
and operations defined on it. Unlike usual numeric algorithms, interval
ones produce intervals containing the correct answer as a result.

The Maximum Accuracy provides an axiomatic method for arithmetic operations
performed in computers that captures essential properties associated with
rounding.

For more information about it, see:

- Moore, R. E., Interval Analysis. Prentice-Hall, Englewood Cliffs,
  New Jersey, 1966.
- Moore, R. E., Methods and Applications of Interval Analysis. SIAM Studies
  in Applied Mathematics, Philadelphia, 1979.
- Kulisch, U. W., Miranker, W. L., Computer Arithmetic in Theory and Practice.
  Academic Press, 1981.

*Project's site*: http://rafaelbarreto.wordpress.com/intpy.

Rafael Menezes Barreto (rafaelbarreto87@gmail.com)

http://rafaelbarreto.wordpress.com/

Features
--------

IntPy is a rising academic project. So, there’s not many things implemented
right now. Despite this, I really believe in that tenet: “Release Early,
Release Often”.

In fact, currently, only Real Intervals are available. No Complex Intervals,
no Interval Vectors and Matrixes, and no extensions of basic math functions.
These will be the next work and any help is welcome.

The following list points out what I intend to implement and what is already
done:

- Directed rounding: *done!*
- Rational string input: *done!*
- Real Intervals: *done!*
- Basic math functions adherent to IEEE 754: pending!
- Interval extensions of basic math functions for Real Intervals: pending!
- Complex Intervals: pending!
- Interval extensions of basic math functions for Complex Intervals: pending!
- Real Interval Vectors: pending!
- Complex Interval Vectors: pending!
- Real Interval Matrixes: pending!
- Complex Interval Matrixes: pending!
- Basic functions to operate with Interval Vector and Matrixes: pending!
- Common Interval Numeric Algorithms: pending!

Dependencies
------------

This project depends upon the following libraries:

- fpconst >= 0.7.2 (http://pypi.python.org/pypi/fpconst/)

License
-------

The current version of IntPy is licensed under GPLv2.
