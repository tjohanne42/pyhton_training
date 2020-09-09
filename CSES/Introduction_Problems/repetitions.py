s = input()
i = 0
nb = 0
tmp = 0
c = s[0]
l = len(s)
while i < l:
	while i < l and s[i] == c:
		tmp += 1
		i += 1
	if tmp > nb:
		nb = tmp
	if i < l:
		c = s[i]
	tmp = 0
print(nb)