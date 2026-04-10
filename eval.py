print("Add mod? Input")
mod = input("> ")
try: mod = int(mod)
except: mod = 0

print('Input base python formula (0 to stop)')
while True:
	inp = eval(str(input('> ')))
	if inp == 0: break
	if mod == 1: inp2 = bin(inp)[2:]
	elif mod == 0: inp2 = ''
	else:
		inp = inp % mod
		inp2 = inp
	print(f"> = {inp} | {inp2}(mod({mod})")

