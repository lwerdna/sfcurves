#!/usr/bin/env python3

import sys
import random

from sfcurves.hilbert import forward, reverse, Algorithm
from sfcurves.outline import wall_follower

def assert_equals(actual, expected):
	if actual != expected:
		print('  actual:', actual)
		print('expected:', expected)
		assert False

if __name__ == '__main__':
	# order 1
	trace = wall_follower(4, 0, 0, forward, reverse)
	assert_equals(trace, [(0,0)])

	trace = wall_follower(4, 0, 1, forward, reverse)
	assert_equals(trace, [(0,0), (0,1)])

	trace = wall_follower(4, 0, 2, forward, reverse)
	assert_equals(trace, [(0,0), (0,1), (1,1), (0,1)]) # note the (0,1) attempt to return home

	trace = wall_follower(4, 0, 3, forward, reverse)
	assert_equals(trace, [(0,0), (1,0), (1,1), (0,1)]) # note CCW travel around the square

	# order 2
	trace = wall_follower(16, 0, 7, forward, reverse)
	assert_equals(trace, [(0,0), (1,0), (1,1), (1,2), (1,3), (0,3), (0,2), (0,1)])

	trace = wall_follower(16, 2, 7, forward, reverse)
	assert_equals(trace, [(0,1), (1,1), (1,2), (1,3), (0,3), (0,2)]) # note the initial move left to find wall

	print('PASS')
