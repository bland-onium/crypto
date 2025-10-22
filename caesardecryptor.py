alph_rus = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ" # 0-32 symb
alph_eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # 0-26 symb

print("Mode (encrypt/decrypt): ")
choice = str(input())

print("Input phrase:")
word = (str(input())).upper()
#word = 'ABRACADABRA'
alph = ''
chk=1

if word[0] in alph_rus:
	alph = alph_rus
elif word[0] in alph_eng:
	alph = alph_eng
else:
	chk=0
	print("Wrong language, try something else")
print(f"alph: {alph}")

if chk == 1:
	if choice[0] == 'd' or choice[0] == 'D':
		for k in range(len(alph)):
			new_word = ''
			indexes = []
			for i in range(len(word)):
				#print(alph.index(word[i]), word[i])
				mov = ( alph.index(word[i]) - k )
				#print(mov, (len(alph) + mov)%len(alph), k, len(alph))
				if mov < 0:
					mov = len(alph) + mov
				#print(mov, new_word)
				new_word += alph[mov]
				indexes.append(mov)
			print(f"K={k} | {indexes} | {new_word} ")
	elif choice[0] == 'e' or choice[0] == 'E':
		for k in range(len(alph)+1):
			new_word = ''
			indexes = []
			for i in range(len(word)):
				#print(alph.index(word[i]), word[i])
				mov = ( alph.index(word[i]) + k )
				#print(mov, (len(alph) + mov)%len(alph), k, len(alph))
				if mov >= len(alph):
					mov = mov % len(alph)
				#print(mov, new_word)
				new_word += alph[mov]
				indexes.append(mov)
			print(f"K={k} | {indexes} | {new_word} ")
	else: print("Wrong mode. ")
