print("Input fraction as x/y in input (0 to stop)")

while True:
	inp = str(input("> "))
	print(inp)
	try: inp = int(inp)
	except: inp = inp
	if inp == 0 or inp == "": break

	a = ''
	b = ''
	mrk = 0
	i = 0
	while i < len(inp):
		if inp[i] == '/':
			mrk = 1
			i += 1
		if mrk == 0:
			a += inp[i]
			print("a", a)
		else:
			b += inp[i]
			print("b", b)
		i += 1
	a = int(a)
	b = int(b)
	pow1 = ((a-1)//2)%2
	pow2 = ((b-1)//2)%2
	res = pow(-1, pow1*pow2)

	print(f"y/p = ({a}/{b}) = (-1)^ {a}-1/2 * {b}-1/2 = {res}")



