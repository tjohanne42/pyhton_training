n = int(input())
nb = int(n * (n + 1) / 2)
if nb % 2:
	print("NO")
else:
	tab1 = []
	tab2 = []
	size1 = 0
	size2 = 0
	if n % 4 == 0:
		i = 1
		while i < n:
			tab1.append(i)
			tab2.append(i + 1)
			tab2.append(i + 2)
			tab1.append(i + 3)
			size1 += 2
			size2 += 2
			i += 4
	elif n % 4 == 3:
		i = n
		while i >= 4:
			tab1.append(i)
			tab2.append(i - 1)
			tab2.append(i - 2)
			tab1.append(i - 3)
			size1 += 2
			size2 += 2
			i -= 4
		tab1.append(1)
		tab1.append(2)
		tab2.append(3)
		size1 += 2
		size2 += 1
	print("YES")
	print(size1)
	s = str(tab1).replace("[", "")
	s = s.replace("]", "")
	s = s.replace(",", "")
	print(s)
	print(size2)
	s = str(tab2).replace("[", "")
	s = s.replace("]", "")
	s = s.replace(",", "")
	print(s)