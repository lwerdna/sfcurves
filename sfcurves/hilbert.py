# space filling curves module

import math

from enum import Enum, auto, unique

@unique
class Algorithm(Enum):
	WIKIPEDIA = 1
	RECURSIVE0 = 2
	RECURSIVE1 = 3

#------------------------------------------------------------------------------
# standard hilbert map and inverse map functions from:
# https://en.wikipedia.org/wiki/Hilbert_curve
#
# tweaked to always return a curve entering at SW exiting at SE
#------------------------------------------------------------------------------

# (rx,ry) = (?,?)
# +-----+-----+
# |(0,1)|(1,1)| y==1, no transform
# +-----+-----+
# |(0,0)|(1,0)|
# +-----+-----+
#
def rotate_wikipedia(n, x, y, rx, ry):
	#print('looking up region (%d,%d)' % (rx, ry))
	if ry == 0:
		if rx == 1:
			x = n-1 - x;
			y = n-1 - y;

		(y,x) = (x,y)

	return (x,y)

def normalize_wikipedia(n, point):
	order = (n.bit_length()-1)>>1
	if order & 1:
		return (point[1], point[0])
	return point

def map_wikipedia(n, d):
	(x,y,t) = (0,0,d)

	width = 1

	while width<n:
		rx = 1 & (t//2)
		ry = 1 & (t ^ rx)

		(x, y) = rotate_wikipedia(width, x, y, rx, ry)
		x += width * rx
		y += width * ry
		#print('at width %d (x,y)=(%d,%d)' % (width, x, y))

		# next
		t //= 4
		width *= 2

	# normalize
	return normalize_wikipedia(n, (x,y))

def unmap_wikipedia(n, x, y):
	(x,y) = normalize_wikipedia(n, (x,y))

	(rx,ry,s,d)=(0,0,0,0)

	s = n//2
	while s > 0:
		rx = int((x & s) > 0)
		ry = int((y & s) > 0)
		d += s * s * ((3 * rx) ^ ry)
		(x, y) = rotate_wikipedia(n, x, y, rx, ry)
		s //= 2

	return d

#------------------------------------------------------------------------------
# alternative algorithm
#------------------------------------------------------------------------------

# compute 2d Hilbert curve coordinate from 1d line coordinate
# regions = A B   numerically ordered by entering and leaving line,
#           C D   eg: [A,C,D,B] means enter at A, exit at B, like "U"
def map_algo0(length, d, x=0, y=0, regions=list('CABD')):
	#print('d2xy(length=%d, d=%d, (x,y)=(%d,%d), regions=%s' % (length, d, x, y, regions))

	if length == 1:
		return (x,y)

	quarter = length//4

	# compute region index
	if d < quarter: region_idx = 0
	elif d < 2*quarter: region_idx = 1
	elif d < 3*quarter: region_idx = 2
	else: region_idx = 3

	# compute new x,y base
	region = regions[region_idx]
	delta = math.sqrt(length)//2
	if region == 'A':
		y += delta
	elif region == 'D':
		x += delta
	elif region == 'B':
		x += delta
		y += delta

	# compute new region
	if region_idx == 0:
		regions = [regions[i] for i in [0,3,2,1]]
	elif region_idx == 3:
		regions = [regions[i] for i in [2,1,0,3]]

	# recur
	return map_algo0(quarter, d-region_idx*quarter, x, y, regions)

#------------------------------------------------------------------------------
# alternative algorithm
#------------------------------------------------------------------------------

def map_algo1(length, d, x=0, y=0, kind='H'):
	if length == 1:
		return (x,y)

	# compute quadrant (0 is entering quadrant, 3 is exiting)
	assert not length%4
	quarter = length//4
	marks = [i*quarter for i in [1,2,3,4]]
	quadrant = next(i for i,mark in enumerate(marks) if d<mark)

	# compute new x,y base (coordinate of bottom left corner of subsquare)
	delta = math.sqrt(length)//2
	x_lookup = {'A':[0,1,1,0], 'B':[1,0,0,1], 'C':[1,1,0,0], 'H':[0,0,1,1]}
	y_lookup = {'A':[0,0,1,1], 'B':[1,1,0,0], 'C':[1,0,0,1], 'H':[0,1,1,0]}
	x += x_lookup[kind][quadrant] * delta
	y += y_lookup[kind][quadrant] * delta

	kind = {'A':'HAAC', 'B':'CBBH', 'C':'BCCA', 'H':'AHHB'}[kind][quadrant]

	# recur
	return map_algo1(length//4, d-quadrant*quarter, x, y, kind)

def unmap_algo1(length, x, y):
	# determine curve order by growing a square at origin
	order = 1
	limit = 2
	while True:
		if x<limit or y<limit:
			break
		order += 1
		limit *= 2

	# TODO

#------------------------------------------------------------------------------
# API
#------------------------------------------------------------------------------

# [0,length) -> (x,y)
def forward(d, length, algo=Algorithm.WIKIPEDIA):
	if algo == Algorithm.WIKIPEDIA:
		return map_wikipedia(length, d)
	elif algo == Algorithm.RECURSIVE0:
		return map_algo0(length, d)
	elif algo == Algorithm.RECURSIVE1:
		return map_algo1(length, d)
	else:
		raise Exception('unsupported algorithm: '+str(algo))

# (x,y) -> [0,length)
def reverse(x, y, length, algo=Algorithm.WIKIPEDIA):
	if algo == Algorithm.WIKIPEDIA:
		return unmap_wikipedia(length, x, y)

	raise Exception('unsupported algorithm: '+str(algo))

