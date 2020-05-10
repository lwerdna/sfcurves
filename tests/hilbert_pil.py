#!/usr/bin/env python3

import sys
import random

from sfcurves.hilbert import forward

def assert_equals(actual, expected):
	if actual != expected:
		print('  actual:', actual)
		print('expected:', expected)
		assert False

if __name__ == '__main__':
	from PIL import Image, ImageDraw

	order = 5
	if sys.argv[1:]:
		order = int(sys.argv[1])

	width = 2**order
	length = 4**order
	width_img = 3*width

	print('order: %d' % order)
	print('width: %d' % width)
	print('length: %d' % length)
	print('width_img: %d' % width_img)

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
