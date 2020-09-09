import pygame
import math

def draw_fractal_tree(x, y, len, radians, width, iteration):
	if iteration < 18:
		if len < 5:
			len = 5
		if width < 1:
			width = 1
		if width == 1:
			color = [234, 61, 30]
		elif width > 1 and width <= 2:
			color = [176, 255, 89]
		elif width > 2 and width <= 3:
			color = [196, 255, 130]
		else:
			color = [210, 255, 180]
		end_x = x + int(len * math.cos(radians))
		end_y = y + int(len * math.sin(radians))
		tmp_width = int(width)
		pygame.draw.line(window_surface, color, [x, y], [end_x, end_y], tmp_width)
		pygame.display.flip()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return False
		if width > 2:
			tmp_end_x = end_x + int((width / 4 - 1) * math.cos(radians + math.pi / 2))
			tmp_end_y = end_y + int((width / 4 - 1) * math.sin(radians + math.pi / 2))
		else:
			tmp_end_x = end_x
			tmp_end_y = end_y
		if draw_fractal_tree(tmp_end_x, tmp_end_y, len * 3 / 4, radians + math.pi / 10, width * 3 / 4, iteration + 1) == False:
			return False
		if width > 2:
			tmp_end_x = end_x + int((width / 4 - 1) * math.cos(radians - math.pi / 2))
			tmp_end_y = end_y + int((width / 4 - 1) * math.sin(radians - math.pi / 2))
		if draw_fractal_tree(tmp_end_x, tmp_end_y, len * 3 / 4, radians - math.pi / 10, width * 3 / 4, iteration + 1) == False:
			return False

grey = (180, 180, 180)
white = (250, 250, 250)
black = (0, 0, 0)

pygame.init()
pygame.display.set_caption("Fractal Tree")
#window_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#print(pygame.display.Info())
size_w, size_h = 1024, 800
window_surface = pygame.display.set_mode((size_w, size_h))
window_surface.fill(grey)
pygame.display.flip()

launched = True

clock = pygame.time.Clock()


done = False
while launched:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			launched = False
	if done is False:
		if draw_fractal_tree(size_w / 2, size_h - 10, 200, math.pi + math.pi / 2, 21, 1) == False:
			launched = False
		done = True
	clock.tick(60)