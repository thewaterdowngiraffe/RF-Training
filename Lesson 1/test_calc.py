import pytest
import math
import calculator


@pytest.mark.parametrize("i", [i for i in range(-20, 20)])
@pytest.mark.parametrize("x", [i for i in range(-20, 20)])
def test_subtract(i, x):
    assert calculator.subtract(i, x) == i-x


@pytest.mark.parametrize("i", [i for i in range(-20, 20)])
@pytest.mark.parametrize("x", [i for i in range(-20, 20)])
def test_add(i, x):
    assert calculator.add(i, x) == i+x


@pytest.mark.parametrize("a", [i for i in range(-10, 11)])
@pytest.mark.parametrize("b", [i for i in range(-10, 11)])
def test_multiply(a, b):
    assert calculator.multiply(
        a, b) == a*b, f" failed to multiply {a}x{b}={a*b}"


def test_exponent_sqrt():
    assert calculator.exponent(10, 0.5) == calculator.sqrt(10)


@pytest.mark.parametrize("num", [i for i in range(-20, 21)])
@pytest.mark.parametrize("base", [i for i in range(-5, 5)])
def test_exponent(num, base):
    assert calculator.exponent(
        base, num/10) == base ** (num/10), f"{num/10} failed"


@pytest.mark.parametrize("num", [i for i in range(1, 1001)])
def test_sqrt(num):
    assert int(math.sqrt(num)) == (calculator.sqrt(num)), f"{num} failed"
