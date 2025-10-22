alph_rus = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alph_eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


print("Mode (encrypt/decrypt): ")
choice = str(input())
#choice = 'e'

print("Input phrase:")
word = (str(input())).upper()
#word = 'MEMENTOMORI'
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

print("Input key:")
key = (str(input())).upper()
#key = 'STOUN'

if key[0] not in alph:
	print("Different languages 🗿")
	chk=0

new_word = []
if chk == 1:
	if len(word) > len(key):
		c = 0
		while len(key) < len(word):
			key += key[c%len(alph)]
			c += 1
		print(f'word: {word}')
		print(f'key: {key}')
	if choice[0]=="E" or choice[0]=="e" or choice[0]=='у' or choice[0]=='У':
		for i in range(len(word)):
			res = (alph.index(word[i])+alph.index(key[i%len(alph)]))%len(alph)
			print(res, alph[res], word[i], key[i%len(alph)], i)
			new_word.append(alph[res])
	elif choice[0]=='D' or choice[0]=='d' or choice[0]=='в' or choice[0]=='В':
		for i in range(len(word)):
			res = (alph.index(word[i])-alph.index(key[i%len(alph)]))%len(alph)
			print(res, alph[res], word[i], key[i%len(alph)], i)
			if res < 0:
				res = 26 - res
			new_word.append(alph[res])
	else:
		print('no decrypt')

	# Printing block
	print(*list(word))
	num1 = []
	num2 = []
	num3 = []
	for i in range(len(word)):
		num1.append(alph.index(word[i]))
		num2.append(alph.index(key[i]))
		num3.append(alph.index(new_word[i]))
	print(*num1)
	print(*list(key))
	print(*num2)
	print(*num3)
	print(*list(new_word))

