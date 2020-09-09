n = int(input())
print("0")
k = 2
while k <= n:
	nb = (k * k) * (k * k - 1) / 2
	if k >= 3:
		nb = nb - 4 * (k - 1) * (k - 2)
	print(int(nb))
	k += 1