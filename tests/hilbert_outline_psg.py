#!/usr/bin/env python
#
# use PySimpleGui to show a real-time view of regions controlled by sliders

import io
import math
import base64
from PIL import Image, ImageDraw

from sfcurves.hilbert import forward, reverse, outline

import PySimpleGUI as sg

order = 5
length = 4**order
width = int(math.sqrt(length))
width_img = 4*width
height_img = 4*width

def img_to_b64gif(img):
	# PIL -> gif -> string
	gif = None
	with io.BytesIO() as output:
		img.save(output, format="GIF")
		gif = output.getvalue()

	# gif string -> base64
	return base64.b64encode(gif)

def draw_region(start, stop, background):
	result = background.copy()

	if start == stop: return result
	if start > stop: (start,stop) = (stop,start)

	#print('calling outline(%d,%d,%d)' % (start, stop, length))
	trace = outline(start, stop, length)
	#print(trace)

	if len(trace) < 2:
		return result

	trace = [(4*p[0]+1, 4*p[1]+1) for p in trace]

	draw = ImageDraw.Draw(result)
	draw.polygon(trace, outline='#00FF00')
	del draw
	return result

if __name__ == '__main__':
	# generate background PIL image
	img_background = Image.new('RGB', (width_img, height_img))
	draw = ImageDraw.Draw(img_background)
	points = [forward(d, length) for d in range(length)]
	for (p0,p1) in zip(points[:-1], points[1:]):
		(x0,y0) = p0
		(x1,y1) = p1
		(x0,y0,x1,y1) = map(lambda a: 4*a+1, (x0,y0,x1,y1))
		draw.line((x0,y0, x1,y1), width=1, fill="#ff0000")
	del draw

	# start
	graph = sg.Graph((width_img,height_img), (0,0), (width_img,height_img), background_color='green', key='graph', pad=(0,0), enable_events=True)
	gui_rows = [[sg.Slider(range=(0,length-1), default_value=0, orientation='h', key='region_start', enable_events=True)],
				[sg.Slider(range=(0,length-1), default_value=length//2, orientation='h', key='region_end', enable_events=True)],
				[sg.Quit()],
				[graph]
				]

	window = sg.Window('Hilbert Curve Region', auto_size_text=True).Layout(gui_rows)

	initial_run = True
	while (True):
		# This is the code that reads and updates your window
		event, values = window.Read(timeout=100)

		update_image = False
		if event == None:
			print('None event')
			break
		elif event == '__TIMEOUT__':
			#print('TIMEOUT event')
			pass
		elif event == 'Quit':
			print('Quit event')
			break
		elif event == 'region_start':
			update_image = True
		elif event == 'region_end':
			update_image = True
		elif event == 'graph':
			print('you clicked the graph at: ', values['graph'])
		else:
			print('unknown event: ', event)
			print('       values: ', values)
			pass

		if initial_run or update_image:
			#print('updating image')
			start = int(values['region_start'])
			stop = int(values['region_end'])
			img = draw_region(start, stop, img_background)
			graph.Erase()
			graph.DrawImage(data=img_to_b64gif(img), location=(0,height_img-1))

		initial_run = False
		
	window.Close() # Don't forget to close your window!
