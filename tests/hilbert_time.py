#!/usr/bin/env python3

from timeit import timeit

import sys
import random

from sfcurves.hilbert import forward, reverse, Algorithm

length = 4**8

points = [random.randint(0, length-1) for x in range(1000)]

print(points)

def wikipedia():
	global points, length
	for point in points:
		result = forward(point, length, Algorithm.WIKIPEDIA)
	
def recursive0():
	global points, length
	for point in points:
		result = forward(point, length, Algorithm.RECURSIVE0)

def recursive1():
	global points, length
	for point in points:
		result = forward(point, length, Algorithm.RECURSIVE1)

trials = 500
print("trials=%d avg_time=%f seconds" % (trials, timeit(wikipedia, number=trials) / trials))
print("trials=%d avg_time=%f seconds" % (trials, timeit(recursive0, number=trials) / trials))
print("trials=%d avg_time=%f seconds" % (trials, timeit(recursive1, number=trials) / trials))
