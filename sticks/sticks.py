import random
import numpy as np
import os

class StickGame(object):
	"""docstring for StickGame"""
	def __init__(self, nb):
		super(StickGame, self).__init__()
		self.nb = nb
		self.original_nb = nb

	def finished(self):
		if self.nb <= 0:
			return True
		return False

	def new_game(self):
		self.nb = self.original_nb
		return self.nb

	def display(self):
		print(" ", "| " * self.nb, "({})".format(self.nb))

	def action(self, action):
		self.nb -= action
		if (self.nb <= 0):
			return (0, -1)
		return (self.nb, 0)

class StickPlayer(object):
	"""docstring for StickPlayer"""
	def __init__(self, is_human, trainable, size):
		super(StickPlayer, self).__init__()
		self.is_human = is_human
		self.trainable = trainable
		self.history = []
		self.reward = []
		self.V = {}
		for s in range(1, size+1):
			self.V[s] = 0.
		self.win = 0
		self.lose = 0
		self.eps = 0.99

	def reset_stat(self):
		self.win = 0
		self.lose = 0
		self.reward = []

	def add_transition(self, tupple):
		self.history.append(tupple)
		s, a, r, sp = tupple
		self.reward.append(r)

	def greedy_step(self, state):
		vmin = 0.
		v = 0
		for i in range(0,3):
			a = i + 1
			if state - a > 0 and (vmin == 0. or self.V[state - a] < vmin):
				vmin = self.V[state - a]
				v = a
		if v > 0:
			return v
		return 1

	def play(self, state):
		if self.is_human == True:
			done = False
			while done is False:
				a = input("How many sticks do you wanna take? ")
				try:
					action = int(a)
					if action < 1 or action > 3:
						print("Action must be < 1 and > 3")
					else:
						done = True
				except:
					print("Unvalid entry, Action must be 1 <= action <= 3")
		else:
			if random.random() < self.eps:
				action = random.randint(1, 3)
			else:
				action = self.greedy_step(state)
		return action

	def train(self):
		if not self.trainable or self.is_human == True:
			return
		for transition in reversed(self.history):
			s, a, r, sp = transition
			if r == 0:
				self.V[s] = self.V[s] + 0.001 * (self.V[sp] - self.V[s])
			else:
				self.V[s] = self.V[s] + 0.001 * (r - self.V[s])
		self.history = []

def play_game(game, p1, p2, show, trainable):
	state = game.new_game()
	players = [p1, p2]
	random.shuffle(players)
	turn = random.randint(0, 1)
	count = 0
	if p1.is_human or p2.is_human:
		os.system("cls")
	while game.finished() is False:
		if show:
			game.display()
			if players[turn % 2] == p1:
				if p1.is_human:
					print("Player 1 it's your turn")
				else:
					print("IA 1 is playing")
			else:
				if p2.is_human:
					print("Player 2 it's your turn")
				else:
					print("IA 2 is playing")
		action = players[turn % 2].play(state)
		if show and players[turn % 2].is_human == False:
			print("action = {}".format(action))
		n_state, reward = game.action(action)
		if reward == -1:
			players[turn % 2].lose += 1
			players[(turn + 1) % 2].win += 1
			if show:
				if players[(turn+ 1) % 2] == p1:
					print("Player 1 wins")
				else:
					print("Player 2 wins")
		if count > 0:
			s, a, r, sp = players[(turn + 1) % 2].history[-1]
			players[(turn + 1) % 2].history[-1] = (s, a, reward * -1, n_state)
		players[turn % 2].add_transition((state, action, reward, None))
		state = n_state
		turn += 1
		count += 1
	if trainable:
		p1.train()
		p2.train()


nb_stick = 12
game = StickGame(nb_stick)
p1 = StickPlayer(False, True, nb_stick)
p2 = StickPlayer(False, True, nb_stick)
human = StickPlayer(True, False, nb_stick)
prand = StickPlayer(False, False, nb_stick)
for i in range(0, 10000):
	if i % 10 == 0:
		p1.eps = max(p1.eps * 0.996, 0.05)
		p2.eps = max(p2.eps * 0.996, 0.05)
	play_game(game, p1, p2, False, True)
for i in p1.V:
	print(i, ".", p1.V[i])
p1.reset_stat()
p1.eps = 0
prand.eps = 100
for i in range(0, 10000):
	play_game(game, p1, prand, False, False)
print("p1 winrate = {}%".format(p1.win * 100 / (p1.win + prand.win)))
i = input("Press Enter to continue ")
p1.reset_stat()
done = False
while done == False:
	play_game(game, p1, human, True, False)
	print("IA winrate against human : {}".format(p1.win * 100 / (p1.win + human.win)))
	i = input("Enter quit to exit or enter to continue : ")
	try:
		if i == "quit":
			done = True
	except:
		done = False
