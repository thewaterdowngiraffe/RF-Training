"""This is a completely flawed calculator each function works...
kindof, there are unique edge cases that will apear during testing
"""
import struct


def multiply(a, b):
    if isinstance(a, int) and b & (b - 1) == 0 and b != 0:
        return a << (b.bit_length()-1)
    a = a/10
    b = b/10
    a = a*b
    return a*100


def add(input1, input2):
    return input1 ^ input2


def subtract(x, y):
    return y-x


def exponent(num, exponent_n):
    if num == 0:
        return int(exponent_n == 0)
    if exponent_n == 0:
        return 1
    if exponent_n < 0:
        return 1/exponent(num, exponent_n*-1)
    if exponent_n == 1:
        return num
    return num * exponent(num, exponent_n-1)


def sqrt(number):
    """fast inverse square root algorithm"""
    x2 = number * 0.5
    i = struct.unpack('i', struct.pack('f', number))[0]
    i = 0x5f3759df - (i >> 1)
    y = struct.unpack('f', struct.pack('i', i))[0]
    y = y * (1.5 - x2 * y * y)
    return int(1/y)
