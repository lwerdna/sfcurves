#!/usr/bin/env python3

import sys
import random
import functools

from sfcurves.hilbert import forward, reverse

def assert_equals(actual, expected):
	if actual != expected:
		print('  actual:', actual)
		print('expected:', expected)
		assert False

if __name__ == '__main__':
	assert_equals(forward(0,1), (0,0))

	assert_equals(forward(0,4), (0,0))
	assert_equals(forward(1,4), (0,1))
	assert_equals(forward(2,4), (1,1))
	assert_equals(forward(3,4), (1,0))

	assert_equals(forward(0,16), (0,0))
	assert_equals(forward(1,16), (1,0))
	assert_equals(forward(2,16), (1,1))
	assert_equals(forward(3,16), (0,1))
	assert_equals(forward(4,16), (0,2))
	assert_equals(forward(5,16), (0,3))
	assert_equals(forward(6,16), (1,3))
	assert_equals(forward(7,16), (1,2))
	assert_equals(forward(8,16), (2,2))
	assert_equals(forward(9,16), (2,3))
	assert_equals(forward(10,16), (3,3))
	assert_equals(forward(11,16), (3,2))
	assert_equals(forward(12,16), (3,1))
	assert_equals(forward(13,16), (2,1))
	assert_equals(forward(14,16), (2,0))
	assert_equals(forward(15,16), (3,0))

	print('mapping/unmapping random points')
	for i in range(10000):
		length = 4**random.randint(0,10)
		d = random.randint(0, length-1)
		(x,y) = forward(d, length)
		d_check = reverse(x, y, length)
		assert_equals(d, d_check)

	print('PASS')
