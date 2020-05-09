#!/usr/bin/env python3

import sys
import random

from sfcurves.hilbert import forward, reverse

def assert_equals(actual, expected):
	if actual != expected:
		print('  actual:', actual)
		print('expected:', expected)
		assert False

print(forward(0,4))
print(forward(1,4))
print(forward(2,4))
print(forward(3,4))
assert_equals(forward(0,4), (0,0))
assert_equals(forward(1,4), (0,1))
assert_equals(forward(2,4), (1,1))
assert_equals(forward(3,4), (1,0))

print('PASS')
