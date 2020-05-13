#!/usr/bin/env python3

import os
import sys

from sfcurves.hilbert import forward, reverse, outline

width = 16
length = width**2
img_width = 4*width
img_height = 4*width

if __name__ == '__main__':
	import pygame
	from pygame.locals import *	
	pygame.init()
	surface = pygame.display.set_mode((img_width, img_height))
	pygame.display.set_caption('hilbert test')

	change = True
	while 1:
		# process pygame events
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()

		if change:
			surface.fill((255,255,255))

			points = [forward(d, length) for d in range(length)]
			for ((x0,y0),(x1,y1)) in zip(points[:-1], points[1:]):
				(x0,y0,x1,y1) = (4*x0+1, img_height - (4*y0+1), 4*x1+1, img_height - (4*(y1)+1))
				pygame.draw.line(surface, (255,0,0), (x0,y0), (x1,y1))

			pygame.display.update()
			change = False

