#import time

n = input()
#tps1 = time.time()
n = int(n)
if n == 1:
	print("1")
elif n < 4:
	print("NO SOLUTION")
elif n % 2 == 0:
	z = 0
	tab = [0] * n
	i = 2
	while i <= n:
		tab[z] = i
		z += 1
		i += 2
	i = 1
	while i < n:
		tab[z] = i
		z += 1
		i += 2
	s = str(tab).replace("[", "")
	s = s.replace("]", "")
	s = s.replace(",", "")
	print(s)
else:
	z = 0
	tab = [0] * n
	i = 2
	while i < n:
		tab[z] = i
		z += 1
		i += 2
	i = 1
	while i <= n:
		tab[z] = i
		i += 2
		z += 1
	s = str(tab).replace("[", "")
	s = s.replace("]", "")
	s = s.replace(",", "")
	print(s)
#tps2 = time.time()
#print("time =", tps2 - tps1)