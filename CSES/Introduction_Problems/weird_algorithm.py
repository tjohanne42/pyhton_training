done = False
while done != True:
	n = input()
	try:
		n = int(n)
	except:
		print("Input positive integer")
	else:
		if n > 0:
			done = True
		else:
			print("Integer must be positive")
print(n, end = "")
while (n != 1):
	if n % 2 == 0:
		n = n / 2
		n = int(n)
	else:
		n = n * 3 + 1
		n = int(n)
	print("", n, end = "")