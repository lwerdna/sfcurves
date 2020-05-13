#!/usr/bin/env python3

import os
import sys

from PIL import Image, ImageDraw

from sfcurves.hilbert import forward, reverse, outline

width = 16
length = width**2
img_width = 4*width
img_height = 4*width

def draw_hilbert():
	global img_width, img_height
	img = Image.new('RGB', (img_width, img_height))
	draw = ImageDraw.Draw(img)
	points = [forward(d, length) for d in range(length)]
	for (p0,p1) in zip(points[:-1], points[1:]):
		(x0,y0) = p0
		(x1,y1) = p1
		(x0,y0,x1,y1) = map(lambda a: 4*a+1, (x0,y0,x1,y1))
		draw.line((x0,y0, x1,y1), width=1, fill="#ff0000")
	del draw
	img.save('/tmp/tmp.png')
	return img

if __name__ == '__main__':
	import pygame
	from pygame.locals import *	
	pygame.init()
	surface = pygame.display.set_mode((img_width, img_height))
	pygame.display.set_caption('hilbert test')

	pygame.display.update()

	change = True
	while 1:
		# process pygame events
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		if change:
			# drawing to pygame
			img = draw_hilbert()
			raw_str = img.tobytes('raw', 'RGB')
			#print(raw_str)
			pygame_surface = pygame.image.fromstring(raw_str, (img_width, img_height), 'RGB')
			surface.blit(pygame_surface, (0,0))
			pygame.display.update()
			del img
			change = False

