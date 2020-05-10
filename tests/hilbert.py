#!/usr/bin/env python3

import sys
import random

from sfcurves.hilbert import forward, reverse

def assert_equals(actual, expected):
	if actual != expected:
		print('  actual:', actual)
		print('expected:', expected)
		assert False

print(forward(0,1))
print('--')
print(forward(0,4))
print(forward(1,4))
print(forward(2,4))
print(forward(3,4))
print('--')
for d in range(16):
	print(forward(d,16))
print('--')
assert_equals(forward(0,4), (0,0))
assert_equals(forward(1,4), (0,1))
assert_equals(forward(2,4), (1,1))
assert_equals(forward(3,4), (1,0))

print('PASS')

if sys.argv[1:] and sys.argv[1]=='image':
	from PIL import Image, ImageDraw

	width = 4
	length = width*width

	width_img = 3*width
	img = Image.new('RGB', (width_img, width_img))
	draw = ImageDraw.Draw(img)

	pts = [forward(x, length) for x in range(length)]
	pts = [(3*p[0]+1, 3*p[1]+1) for p in pts]
	pts = [(p[0], width_img-1-p[1]) for p in pts]
	lines = zip(pts[:-1], pts[1:])
	for line in lines:
		((x1,y1),(x2,y2)) = line
		#print('drawing line (%d,%d) -> (%d,%d)' % (x1,y1,x2,y2))
		draw.line((x1,y1,x2,y2), width=1, fill='#FF0000')

	del draw
	fpath = '/tmp/tmp.png'
	print('saving %s' % fpath)
	img.save(fpath)
	
