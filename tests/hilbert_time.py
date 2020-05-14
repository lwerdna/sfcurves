#!/usr/bin/env python3

from timeit import timeit

import sys
import random

import math
from sfcurves.hilbert import forward, reverse, generator, Algorithm

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

full_range_length = 4**6

def full_range_wikipedia():
	global full_range_length
	for d in range(full_range_length):
		result = forward(d, length, Algorithm.WIKIPEDIA)

def full_range_recursive0():
	global full_range_length
	for d in range(full_range_length):
		result = forward(d, length, Algorithm.RECURSIVE0)

def full_range_generator():
	global full_range_length
	g = generator(full_range_length)
	for d in range(full_range_length):
		result = next(g)

trials = 50
print("full range WIKIPEDIA  trials=%d avg_time=%f seconds" % (trials, timeit(full_range_wikipedia, number=trials) / trials))
print("full range RECURSIVE0 trials=%d avg_time=%f seconds" % (trials, timeit(full_range_recursive0, number=trials) / trials))
print("full range GENERATOR  trials=%d avg_time=%f seconds" % (trials, timeit(full_range_generator, number=trials) / trials))
print('--')
print("forward WIKIPEDIA  trials=%d avg_time=%f seconds" % (trials, timeit(wikipedia, number=trials) / trials))
print("forward RECURSIVE0 trials=%d avg_time=%f seconds" % (trials, timeit(recursive0, number=trials) / trials))
print("forward RECURSIVE1 trials=%d avg_time=%f seconds" % (trials, timeit(recursive1, number=trials) / trials))
print('--')
print("reverse WIKIPEDIA  trials=%d avg_time=%f seconds" % (trials, timeit(unmap_wikipedia, number=trials) / trials))
print("reverse RECURSIVE0 trials=%d avg_time=%f seconds" % (trials, timeit(unmap_recursive0, number=trials) / trials))
#print("trials=%d avg_time=%f seconds" % (trials, timeit(unmap_recursive1, number=trials) / trials))


