n = int(input())
nb = int(n * (n + 1) / 2)
s = input().split()
i = 0
while i < n - 1:
	nb -= int(s[i])
	i += 1
print(nb)