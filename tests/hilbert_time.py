#!/usr/bin/env python3

from timeit import timeit

import sys
import random

import math
from sfcurves.hilbert import forward, reverse, Algorithm

length = 4**8
width = int(math.sqrt(length))

ds = [random.randint(0, length-1) for x in range(1000)]
points = [(random.randint(0,width-1), random.randint(0,width-1)) for x in range(1000)]

def wikipedia():
	global ds, length
	for d in ds:
		result = forward(d, length, Algorithm.WIKIPEDIA)

def recursive0():
	global ds, length
	for d in ds:
		result = forward(d, length, Algorithm.RECURSIVE0)

def recursive1():
	global ds, length
	for d in ds:
		result = forward(d, length, Algorithm.RECURSIVE1)

def unmap_wikipedia():
	global points, length
	for point in points:
		result = reverse(point[0], point[1], length, Algorithm.WIKIPEDIA)

def unmap_recursive0():
	global points, length
	for point in points:
		result = reverse(point[0], point[1], length, Algorithm.RECURSIVE0)

def unmap_recursive1():
	global points, length
	for point in points:
		result = reverse(point[0], point[1], length, Algorithm.RECURSIVE1)

trials = 50
print("trials=%d avg_time=%f seconds" % (trials, timeit(wikipedia, number=trials) / trials))
print("trials=%d avg_time=%f seconds" % (trials, timeit(recursive0, number=trials) / trials))
print("trials=%d avg_time=%f seconds" % (trials, timeit(recursive1, number=trials) / trials))
print('--')
print("trials=%d avg_time=%f seconds" % (trials, timeit(unmap_wikipedia, number=trials) / trials))
print("trials=%d avg_time=%f seconds" % (trials, timeit(unmap_recursive0, number=trials) / trials))
#print("trials=%d avg_time=%f seconds" % (trials, timeit(unmap_recursive1, number=trials) / trials))

