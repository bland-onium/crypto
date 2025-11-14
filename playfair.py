alph_rus = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯЫ12"
alph_eng = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
lang = ''
n = 0

# =========================================
print("Mode (encrypt/decrypt): ")
mode = str(input())
#choice = 'e'

print("Input phrase:")
word = (str(input())).upper()
alph = ''
chk=1

print("Input key(none, if key = word)")
key = (str(input())).upper()
if key == '' or key == ' ':
    key = word

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


if chk == 1:
    # ==========================================
    # Remove duplicates from word while preserving order
    wrd = ""
    seen = set()
    for char in key:
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
        print('a = ', a+1, 'b = ', b+1, 'symb = ', matrix[a][b])
        b += 1
        if b >= n:
            a += 1
            b = 0

    for i in range(n):
        print (matrix[i])

    # ТУТ ДОЛЖЕН ПОЯВИТЬСЯ КОД ШИФРАТОРА-ДЕШИФРАТОРА ПО ПЛЕЙФЕРУ

    crypt = ''
    crypt2= ''
    if lang == 'r':
        if len(word) % 2 == 1:
            word = word + 'Ъ'
        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                word = word[:i]+'Ъ'+word[i+1:]
    elif lang == 'e':
        if len(word) % 2 == 1: 
            word = word + 'Z'
        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                word = word[:i]+'Z'+word[i+1:]

    i=0
    while i < len(word)-1:
        # seek
        for a in range(n):
            for b in range(n):
                if matrix[a][b] == word[i]:
                    pos_a1 = a # row
                    pos_b1 = b # column
                elif matrix[a][b] == word[i+1]:
                    pos_a2 = a # row
                    pos_b2 = b # col
        i += 2
        # encrypt-decrypt
        new_a1=0; new_a2=0; new_b1=0; new_b2 = 0
        if mode == 'd': # Decryption
            if pos_a1 == pos_a2: # В одной строке
                new_a1 = pos_a1
                new_a2 = pos_a2
                new_b1 = pos_b2-1
                if new_b1 < 0: new_b1 = n-1
                new_b2 = pos_b1-1
                if new_b2 < 0: new_b2 = n-1
            elif pos_b1 == pos_b2: # В одном столбце
                new_b1 = pos_b1
                new_b2 = pos_b2
                new_a1 = pos_a2-1
                if new_a1 < 0: new_a1 = n-1
                new_a2 = pos_a1-1
                if new_a2 < 0: new_a2 = n-1
            else:
                new_a1 = pos_a2
                new_b1 = pos_b1
                new_a2 = pos_a1
                new_b2 = pos_b2
        else: # Encryption
            if pos_a1 == pos_a2: # На одной строке
                new_a1 = pos_a1
                new_a2 = pos_a2
                new_b1 = pos_b1+1;
                if new_b1 >= n: new_b1 = new_b1%n
                new_b2 = pos_b2+1
                if new_b2 >= n: new_b2 = new_b2%n
                #print(matrix[pos_a1][new_b1], matrix[pos_a2][new_b2]) 
            elif pos_b1 == pos_b2: # На одном столбце
                new_b1 = pos_b1
                new_b2 = pos_b2
                new_a1 = pos_a1+1
                if new_a1>= n: new_a1 = new_a1%n
                new_a2 = pos_a2+1
                if new_a2 >= n: new_a2 = new_a2%n
                #print(matrix[new_a1][pos_b1], matrix[new_a2][pos_b2])
            else: # В обычных условиях, когда они по диагонали друг от друга
                new_a1 = pos_a2
                new_b1 = pos_b1
                new_a2 = pos_a1
                new_b2 = pos_b2
        print(f'{matrix[pos_a1][pos_b1]}{matrix[pos_a2][pos_b2]} -> {matrix[new_a1][new_b1]}{matrix[new_a2][new_b2]}')
        crypt = crypt + matrix[new_a1][new_b1] + matrix[new_a2][new_b2]
        crypt2= crypt2+ matrix[new_a2][new_b2] + matrix[new_a1][new_b1]
    print(crypt)
    print(crypt2)
