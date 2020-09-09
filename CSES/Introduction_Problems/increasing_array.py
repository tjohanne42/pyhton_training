n = input()
n = int(n)
s = input()
tab = s.split(" ")
i = 0
while i < n:
	tab[i] = int(tab[i])
	i += 1
i = 1
count = 0
while i < n:
	if tab[i] < tab[i - 1]:
		tmp = tab[i - 1] - tab[i]
		tab[i] += tmp
		count += tmp
	else:
		i += 1
print(count)