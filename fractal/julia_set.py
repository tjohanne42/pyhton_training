import pygame
from pygame import gfxdraw
import math
import random

size_w, size_h = 640, 360
black = (0, 0, 0)
white = (250, 250, 250)
maxiterations = 20

w = 4
h = (w * size_h) / size_w
xmin = -w / 2
ymin = -h / 2
xmax = xmin + w
ymax = ymin + h
dx = (xmax - xmin) / size_w
dy = (ymax - ymin) / size_h

colors = []
n = 0
while n < maxiterations:
	colors.append((n * 5 % 256, n * 12 % 256, n * 24 % 256))
	n += 1

def julia_set(ca, cb):
	window_surface.fill(black)
	y = ymin
	j = 0
	while j < size_h:
		x = xmin
		i = 0
		while i < size_w:
			a = x
			b = y
			n = 0
			while n < maxiterations:
				aa = a * a
				bb = b * b
				if (aa + bb > 4.0):
					break
				twoab = 2.0 * a * b
				a = aa - bb + ca
				b = twoab + cb
				n += 1
			#if n == maxiterations:
				#pygame.gfxdraw.pixel(window_surface, i, j, black)
				#pygame.draw.line(window_surface, black, [i, j], [i, j])
			if n < maxiterations:
				pygame.gfxdraw.pixel(window_surface, i, j, colors[n])
				#pygame.draw.line(window_surface, colors[n], [i, j], [i, j])
			x += dx
			i += 1
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					return False
		y += dy
		j += 1
	pygame.display.flip()
	return True

pygame.init()
pygame.display.set_caption("Julia Set")
window_surface = pygame.display.set_mode((size_w, size_h))
launched = True
clock = pygame.time.Clock()

#angle = random.random()
ca = random.random() - random.random()
cb = random.random() - random.random()
if julia_set(ca, cb) == False:
		launched = False
while launched:
	#ca = math.cos(angle)
	#cb = math.sin(angle)
	#if julia_set(ca, cb) == False:
		#launched = False
	#angle += random.random()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			launched = False
		elif event.type == pygame.MOUSEMOTION:
			ca = (event.pos[0] - size_w / 2) / (size_w / 2)
			cb = (event.pos[1] - size_h / 2) / (size_h / 2)
			if julia_set(ca, cb) == False:
				launched = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				print("left click")
			elif event.button == 4:
				w -= w / 10
				h = (w * size_h) / size_w
				xmin = -w / 2
				ymin = -h / 2
				xmax = xmin + w
				ymax = ymin + h
				dx = (xmax - xmin) / size_w
				dy = (ymax - ymin) / size_h
				if julia_set(ca, cb) == False:
					launched = False
			elif event.button == 5:
				w += w / 10
				h = (w * size_h) / size_w
				xmin = -w / 2
				ymin = -h / 2
				xmax = xmin + w
				ymax = ymin + h
				dx = (xmax - xmin) / size_w
				dy = (ymax - ymin) / size_h
				if julia_set(ca, cb) == False:
					launched = False
	clock.tick(60)