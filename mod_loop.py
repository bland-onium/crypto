print("Input code as <x*y + t>. t - parseable num")


while True:
	seeking = int(input("seeking value> "))
	try: seeking = int(seeking)
	except: seeking = 2

	mod = input("mod > ")
	try: mod = int(mod)
	except: mod = 1

	print(f"seeking: {seeking}, mod: {mod}")

	inp = str(input('formula > '))
	print(inp)
	pos = 0
	if inp == 0 or inp == '': break
	elif mod == '0': inp2 = ''
	
	arr = []
	for i in range(1, 1000):
		next = inp
		rnext = 0
		next = next.replace('t', str(i))
		#print(next, i)
		rnext = eval(next)
		rnext = rnext % mod
		if rnext == seeking:
			print(f"FOUND\n{(next)}({mod}) = {rnext}\n")
			arr.append(i)
			continue
		print(f"{i} -> {rnext}")

	print(f"> = {next} | {next}(mod({mod}))")
	print(f"Array of good t's: {arr}")
