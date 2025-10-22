alph_rus = "АБВГДЕЁЖЗЙКЛМНОПРСТУФХЦЧШЩЪЭЮ-12"
alph_eng = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
lang = ''

# =========================================
print("Mode (encrypt/decrypt): ")
choice = str(input())
#choice = 'e'

print("Input phrase:")
word = (str(input())).upper()
alph = ''
chk=1

if word[0] in alph_rus:
	alph = alph_rus
	lang = 'r'
elif word[0] in alph_eng:
	alph = alph_eng
	lang = 'e'
else:
	chk=0
	print("Wrong language, try something else")
print(f"alph: {alph}")

# ==========================================
# Remove duplicates from word while preserving order
wrd = ""
seen = set()
for char in word:
    if char not in seen:
        seen.add(char)
        wrd += char

matrix = []
if lang == 'r':
    n = 6
elif lang == 'e':
    n = 5
else: 
    n = 0

matrix = [['' for i in range(n)] for i in range(n)]

# Create text without duplicates
txt = wrd
seen = set(wrd)
for char in alph:
    if char not in seen:
        seen.add(char)
        txt += char

print(txt)

# Fill the matrix: start with a=0, b=0
a = 0
b = 0
for i in range(len(txt)):
    if a >= n:  # Stop if matrix is full
        break
    matrix[a][b] = txt[i]
    print('a = ', a, 'b = ', b, 'symb = ', matrix[a][b])
    b += 1
    if b >= n:
        a += 1
        b = 0

print(matrix)

# ТУТ ДОЛЖЕН ПОЯВИТЬСЯ КОД ШИФРАТОРА-ДЕШИФРАТОРА ПО ПЛЕЙФЕРУ