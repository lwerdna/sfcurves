#!/usr/bin/env python3

import sys
import random

from sfcurves.hilbert import forward, reverse, Algorithm

def assert_equals(actual, expected):
	if actual != expected:
		print('  actual:', actual)
		print('expected:', expected)
		assert False

if __name__ == '__main__':
	# simple forward mapping
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

	# simple reverse mapping
	assert_equals(reverse(0,0,1), 0)

	assert_equals(reverse(0,0,4), 0)
	assert_equals(reverse(0,1,4), 1)
	assert_equals(reverse(1,1,4), 2)
	assert_equals(reverse(1,0,4), 3)

	assert_equals(reverse(0,0,16), 0)
	assert_equals(reverse(1,0,16), 1)
	assert_equals(reverse(1,1,16), 2)
	assert_equals(reverse(0,1,16), 3)
	assert_equals(reverse(0,2,16), 4)
	assert_equals(reverse(0,3,16), 5)
	assert_equals(reverse(1,3,16), 6)
	assert_equals(reverse(1,2,16), 7)
	assert_equals(reverse(2,2,16), 8)
	assert_equals(reverse(2,3,16), 9)
	assert_equals(reverse(3,3,16), 10)
	assert_equals(reverse(3,2,16), 11)
	assert_equals(reverse(3,1,16), 12)
	assert_equals(reverse(2,1,16), 13)
	assert_equals(reverse(2,0,16), 14)
	assert_equals(reverse(3,0,16), 15)


	print('mapping/unmapping random points')
	for i in range(10000):
		length = 4**random.randint(0,10)
		d = random.randint(0, length-1)
		(x,y) = forward(d, length)
		d_check = reverse(x, y, length)
		assert_equals(d_check, d)

	print('comparing algorithms')
	for i in range(10000):
		length = 4**random.randint(0,10)
		d = random.randint(0, length-1)

		p0 = forward(d, length, Algorithm.WIKIPEDIA)
		p1 = forward(d, length, Algorithm.RECURSIVE0)
		p2 = forward(d, length, Algorithm.RECURSIVE1)

		assert_equals(p0, p1)
		assert_equals(p1, p2)

	print('PASS')
