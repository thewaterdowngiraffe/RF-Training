import pytest
import math
import calculator


def test_subtract():
    for i in range(-20, 21):
        for x in range(-20, 21):
            assert calculator.subtract(i, x) == i-x


def test_add():
    for i in range(-20, 21):
        for x in range(-20, 21):
            assert calculator.add(i, x) == i+x


def test_multiply():
    for a in range(-1000, 1001):
        for b in range(-1000, 1001):
            assert calculator.multiply(
                a, b) == a*b, f" failed to multiply {a}x{b}={a*b}"


def test_exponent_sqrt():
    assert calculator.exponent(10, 0.5) == calculator.sqrt(10)


def test_exponent():
    base = 7
    for i in range(-100, 110):
        assert calculator.exponent(
            base, i/10) == base ** (i/10), f"{i/10} failed"


def test_sqrt():
    # will fail (expected)
    for i in range(1, 1001):
        assert int(math.sqrt(i)) == (calculator.sqrt(i)), f"{i} failed"
