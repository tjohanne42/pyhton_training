import numpy as np
import random

class Grid(object):
	"""docstring for Grid"""
	def __init__(self, posx, posy, size):
		super(Grid, self).__init__()
		self.grid = [
			[-1, 0, 3, 0, 0, 5],
			[0, -1, 0, -1, 0, -1],
			[0, 0, 0, 0, 0, 0],
			[0, 0, -1, -1, 0, 0],
			[0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, -1, 4],
		]
		self.x_original = posx
		self.y_original = posy
		self.size = size

	def reset(self):
		self.x = self.x_original
		self.y = self.y_original
		return self.y * self.size + self.x

	def step(self, action):
		# 0 = up 1 = right 2 = down 3 = left
		if action == 0 and self.y > 0:
			self.y -= 1
		elif action == 1 and self.x < self.size - 1:
			self.x += 1
		elif action == 2 and self.y < self.size - 1:
			self.y += 1
		elif self.x > 0:
			self.x -= 1
		#doit retourner les coordonnees de la nouvelle pos
		return (self.y * self.size + self.x, self.grid[self.y][self.x])

	def show(self):
		tmp = self.grid[self.y][self.x]
		self.grid[self.y][self.x] = 2
		for each in self.grid:
			print(" ", end = "")
			for i in each:
				print("| {} ".format(i), end = "")
			print("|")
		self.grid[self.y][self.x] = tmp

	def finished(self):
		if self.grid[self.y][self.x] > 0:
			return True
		return False

def take_action(st, Q, eps):
	if random.random() < eps:
		action = random.randint(0, 3)
	else:
		action = np.argmax(Q[st])
	return action

grid = Grid(0, 5, 6)
Q = [
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	[0, 0, 0, 0],
	]
for i in range(0, 2000):
	st = grid.reset()
	while grid.finished() == False:
		at = take_action(st, Q, 0.5)
		(stp1, r) = grid.step(at)
		atp1 = take_action(stp1, Q, 0)
		Q[st][at] = Q[st][at] + 0.1 * (r + 0.9 * Q[stp1][atp1] - Q[st][at])
		st = stp1

for i in range(0, 35):
	print(i, Q[i])

done = False
while done == False:
	st = grid.reset()
	print("The car is the 2, the car has to take the maximum reward on the map")
	while grid.finished() == False and done == False:
		grid.show()
		print("Press Enter or type \"quit\"")
		i = input("")
		try:
			if i == "quit":
				done = True
		except:
			done = False
		at = take_action(st, Q, 0)
		(stp1, r) = grid.step(at)
		st = stp1
	if done == False:
		grid.show()
		i = input("")
