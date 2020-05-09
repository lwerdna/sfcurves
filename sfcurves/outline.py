def wall_follower(n, d0, d1, mapping, imapping):
	def ok(x, y):
		if x<0 or y<0: return False
		d = imapping(n**2, x, y)
		#print('is %d within %d,%d' % (d, d0, d1))
		return d>=0 and d>=d0 and d<d1

	# move left until stop
	(x,y) = mapping(n**2, d0)
	while 1:
		if x == 0: break
		if not ok(x-1,y): break
		x = x-1

	start = (x,y)
	trace = [start]
	direction = 'down'

	tendencies = ['right', 'down', 'left', 'up']

	while 1:
		#print('at (%d,%d) heading %s' % (x,y,direction))

		tendency = tendencies[(tendencies.index(direction)+1) % 4]

		xmod = {'right':1, 'down':0, 'left':-1, 'up':0}
		ymod = {'right':0, 'down':-1, 'left':0, 'up':1}

		moved = False

		# case A: we can turn right
		x_try = x+xmod[tendency]
		y_try = y+ymod[tendency]
		if ok(x_try, y_try):
			direction = tendency
			(x,y) = (x_try, y_try)
			moved = True
		else:
			# case B: we can continue in current direction
			x_try = x+xmod[direction]
			y_try = y+ymod[direction]
			if ok(x_try, y_try):
				(x,y) = (x_try, y_try)
				moved = True
			else:
				# case C: we can't continue! ah!
				direction = tendencies[(tendencies.index(direction)-1)%4]

		if moved:
			trace.append((x,y))
			
			if (x,y) == start:
				break

	return trace

