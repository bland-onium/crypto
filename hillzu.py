from math import sqrt
alph_rus = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alph_eng = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
numbers = '0123456789'
alph = ''
chk = 1
nkey = 0

def create_matrix(key, n):
	matrix = [[0 for i in range(n)] for i in range(n)]
	for a in range(n):
		for b in range(n):
			matrix[a][b] = key[a*n+b]
	print('key_matrix: ', matrix)
	return matrix

def turn_to_num(key): #перестройка в числовой список
	if key[-1] == ' ': key[-1]=[]
	key_listed=[]
	global nkey
	global alph
	global chk
	if key[0] in numbers:
		# numerical
		buff = ''
		for i in key:
			if i not in numbers:
				if buff != '':
					key_listed.append(int(buff))
					buff = ''
			else:
				buff += i
		key_listed.append(int(buff))
		chk = 1
		# включаем сюда декодировку из str в int
	else:
		# alphabetical
		for i in range(len(key)):
			key_listed.append(alph.index(key[i]))
		chk = 1
	return key_listed

def check(word):
	if word[0] in alph_rus:
		alph = alph_rus
	elif word[0] in alph_eng:
		alph = alph_eng
	else:
		print("Wrong language, try something else")	
	return alph

def get_nkey(key):
	nkey = sqrt(len(key))
	#print(nkey, int(nkey))
	if nkey == int(nkey):
		return int(nkey)
	else:
		global key_listed
		while int(sqrt(len(key_listed))) != sqrt(len(key_listed)):
			key.append(0)
		nkey = sqrt(len(key_listed))
		return int(nkey)

def mod_dbl_matrix(a, b, c, d):
	mat = [[a, b], [c, d]]
	mod = (mat[0][0]*mat[1][1])-mat[1][0]*mat[0][1]
	print(mat[0][0], b, c, mat[1][1], mod)
	return mod

# =========================================
print("Mode (encrypt/decrypt): ")
choice = str(input())
#choice = 'e'

print("Input phrase:")
word = (str(input())).upper()
#word = 'ЯМРИ'
#word = 'ТУЩГВА'
alph = check(word)
num_word = turn_to_num(word)
print(f"alph: {alph}\n")
print(f"word: {word}")
print(f"word: {num_word}, --> {len(word)}")

print(f"input B-key:")
bmatrix = (str(input())).upper()
#bmatrix = '1 2 3'
#bmatrix = '2 7'
b_list = turn_to_num(bmatrix)
print("Input as: <1 2 54> or <1,22,34,4>")
print(f"Bkey: {b_list}, ---> {len(b_list)}")

print(f"input A-key:")
key = (str(input())).upper()
#key = '1 2 3 0 5 4 1 7 8'
#key = '7 3 1 4'
key_listed = turn_to_num(key)
nkey = get_nkey(key_listed)
print(f"Akey: {key}")
print(f"Akey: {key_listed}, ---> {len(key_listed)}")
print(f"nkey: {nkey}")

# Проверка слова на долбоёба
if len(num_word) % nkey != 0:
	while len(num_word) % nkey != 0:
		if len(num_word) % nkey == 0:
			break
		if alph[0] == 'А':
			num_word.append(27)
		else:
			num_word.append(25)
print(num_word)

#поехали
if True:
	#собираем ключ в матрицу
	kmatrix = create_matrix(key_listed, nkey)
	
	if choice == 'd':
		mod = 0
		d = len(kmatrix)
		transmat = [[0 for i in range(d)] for j in range(d)]
		if d == 2:
			mod = mod_dbl_matrix(\
				kmatrix[0][0],kmatrix[0][1],\
				kmatrix[1][0],kmatrix[1][1])
			for i in range(d):
				for j in range(d):
					transmat[i][j] = kmatrix[(d-j+1)%d][(d-i+1)%d]*pow(-1, i+j)
		elif d == 3:
			mod = 	kmatrix[0][0]*kmatrix[1][1]*kmatrix[2][2]+\
					kmatrix[0][1]*kmatrix[1][2]*kmatrix[2][0]+\
					kmatrix[0][2]*kmatrix[1][0]*kmatrix[2][1]-\
					kmatrix[0][2]*kmatrix[1][1]*kmatrix[2][0]-\
					kmatrix[0][1]*kmatrix[1][0]*kmatrix[2][2]-\
					kmatrix[0][0]*kmatrix[1][2]*kmatrix[2][1]
			for i in range(d):
				for j in range(d):
					s = []
					for k in range(d):
						for h in range(d):
							if k != i and h != j:
								s.append(kmatrix[h][k])
					
					transmat[i][j] = mod_dbl_matrix(\
						s[0],s[1],s[2],s[3])*pow(-1, i+j)
					print(s, transmat[i][j])
					s.clear()
		elif d > 3:
			print('minor mode are not developed')
			quit()
		if mod == 0:
			print("impossible to find exit.")
			quit()
		print(f"mod = {mod}")
		if mod < 0:
			mod = len(alph)-mod
		tmod = 1
		while (mod * tmod) % (len(alph)) != 1:
			tmod += 1
		print(f"tmod = {tmod}")
		print(f"transp matrix = {transmat}")

		for i in range(d):
			for j in range(d):
				kmatrix[i][j] = (transmat[i][j] * tmod)%len(alph)
		print(f"A^-1: {kmatrix}")

		

	cyphertext = [] # Шифротекст
	i = 0

	while i < len(num_word): # бьем на блоки
		block = []
		icnt = 0
		for j in range(nkey):
			block.append(num_word[i])
			i += 1
		print(block)
		
		#start multipy
		res = []
		sum = 0
		j = 0; k = 0
		if choice == 'd':
			while j < len(block): # Цикл движения по горизонту матрицы
				res.append(0)
				print("Block {")
				while k < len(block): # Движение по вертикали
					print(f"{block[k]-b_list[k]}*{kmatrix[j][k]}")
					res[j] += (block[k]-b_list[k])*kmatrix[j][k]
					k += 1
				print("}",res[j], res[j]%len(alph))
				j += 1; k = 0
		else:
			while j < len(block): # Цикл движения по горизонту матрицы
				res.append(0)
				print("Block {")
				while k < len(block): # Движение по вертикали
					print(f"{block[k]}*{kmatrix[j][k]}")
					res[j] += block[k]*kmatrix[j][k]
					k += 1
				res[j] += b_list[j]
				print("} +",b_list[j])
				j += 1; k = 0

		print(res) # Результат перемножения блока слова
		cyphertext.append(res) # Собираем шифротекст
		block.clear()
		continue
	
	print('\n',cyphertext,'\n')
	cyph = []
	# шифротекст кривой, его надо разобрать из матрицы в список
	for i in range(len(cyphertext)):
		for j in range(nkey):
			cyph.append(cyphertext[i][j])
	print(cyph)
	for i in range(len(cyph)):
		cyph[i] = cyph[i] % len(alph)
	print("cipher nums:", cyph)
	for i in range(len(cyph)):
		cyph[i] = alph[cyph[i]]
	print("result:",cyph)

'''
	# похуй, переприсвоение
	cyphertext = cyph
	print(cyph)
	for i in range(len(cyphertext)):
		# сведение к цикличному виду
		cyphertext[i] = cyphertext[i]% (len(alph))
	for i in range(len(cyphertext)):
		cyphertext[i] = alph[cyphertext[i]]
	print(cyphertext)
'''