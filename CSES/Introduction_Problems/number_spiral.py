n = input()
n = int(n)
tab = ["s"] * n
i = 0
while i < n:
	tab[i] = input()
	i += 1
tab2 = [0] * n
i = 0
while i < n:
	tmp = tab[i].split(" ")
	y = int(tmp[0])
	x = int(tmp[1])
	if y >= x:
		nb = y * y
		if y % 2 == 0:
			nb = nb - x + 1
		else:
			nb = nb - y - (y - x) + 1
	else:
		nb = x * x
		if x % 2 == 0:
			nb = nb - x - (x - y) + 1
		else:
			nb = nb - y + 1
	print(nb)
	i += 1