from math import sqrt

alph_rus = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
alph_eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = '0123456789'
alph = ''
nkey = 0

def create_matrix(key, n): # Инициализация матрицы
    matrix = [[0 for i in range(n)] for i in range(n)]
    for a in range(n):
        for b in range(n):
            matrix[a][b] = key[a*n+b]
    print('key_matrix: ', matrix)
    return matrix

def turn_to_num(key):
    if not key:
        return []
    key_listed = []
    global alph
    if key[0] in numbers:
        import re
        numbers_list = re.findall(r'\d+', key)
        key_listed = [int(num) for num in numbers_list]
    else:
        for i in range(len(key)):
            if key[i] in alph:
                key_listed.append(alph.index(key[i]))
    return key_listed

def check(word):
    global alph
    if not word:
        print("Empty word")
        return None
    if word[0] in alph_rus:
        alph = alph_rus
    elif word[0] in alph_eng:
        alph = alph_eng
    else:
        print("Wrong language, try something else") 
        return None
    return alph

def get_nkey(key):
    nkey = sqrt(len(key))
    if nkey == int(nkey):
        return int(nkey)
    else:
        key_extended = key.copy()
        while sqrt(len(key_extended)) != int(sqrt(len(key_extended))):
            key_extended.append(0)
        nkey = sqrt(len(key_extended))
        return int(nkey)

def mod_inverse(a, m):
    """Находит обратный элемент a по модулю m"""
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def matrix_mod_inverse(matrix, mod_size):
    """Вычисляет обратную матрицу по модулю mod_size"""
    n = len(matrix)
    
    # Вычисляем определитель
    if n == 2:
        det = (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % mod_size
    elif n == 3:
        det = (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) -
               matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0]) +
               matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])) % mod_size
    else:
        raise ValueError("Only 2x2 and 3x3 matrices are supported")
    
    # Находим обратный определитель
    det_inv = mod_inverse(det, mod_size)
    if det_inv is None:
        raise ValueError(f"Matrix is not invertible (determinant {det} has no inverse mod {mod_size})")
    
    # Вычисляем обратную матрицу
    if n == 2:
        inv_matrix = [
            [matrix[1][1] % mod_size, -matrix[0][1] % mod_size],
            [-matrix[1][0] % mod_size, matrix[0][0] % mod_size]
        ]
    elif n == 3:
        inv_matrix = [
            [
                (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]) % mod_size,
                (matrix[0][2] * matrix[2][1] - matrix[0][1] * matrix[2][2]) % mod_size,
                (matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]) % mod_size
            ],
            [
                (matrix[1][2] * matrix[2][0] - matrix[1][0] * matrix[2][2]) % mod_size,
                (matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]) % mod_size,
                (matrix[0][2] * matrix[1][0] - matrix[0][0] * matrix[1][2]) % mod_size
            ],
            [
                (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]) % mod_size,
                (matrix[0][1] * matrix[2][0] - matrix[0][0] * matrix[2][1]) % mod_size,
                (matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]) % mod_size
            ]
        ]
    
    # Умножаем на обратный определитель
    for i in range(n):
        for j in range(n):
            inv_matrix[i][j] = (inv_matrix[i][j] * det_inv) % mod_size
            if inv_matrix[i][j] < 0:
                inv_matrix[i][j] += mod_size
    
    return inv_matrix

# =========================================
print("Mode (encrypt/decrypt): ")
choice = str(input()).lower()

print("Input phrase:")
word = (str(input())).upper()
alph = check(word)
if alph is None:
    exit()

num_word = turn_to_num(word)
print(f"alph: {alph}\n")
print(f"word: {word}")
print(f"word nums: {num_word}, length: {len(word)}")

print(f"input B-key:")
bmatrix = (str(input())).upper()
b_list = turn_to_num(bmatrix)
print("Input as: <1 2 54> or <1,22,34,4>")
print(f"Bkey: {b_list}, length: {len(b_list)}")

print(f"input A-key:")
key = (str(input())).upper()
key_listed = turn_to_num(key)
nkey = get_nkey(key_listed)
print(f"Akey: {key}")
print(f"Akey nums: {key_listed}, length: {len(key_listed)}")
print(f"nkey: {nkey}")

# Проверка слова на кратность nkey
if len(num_word) % nkey != 0:
    while len(num_word) % nkey != 0:
        if alph == alph_rus:
            num_word.append(32)  # пробел для русского
        else:
            num_word.append(25)  # Z для английского
print("Padded word:", num_word)

# Основной алгоритм
kmatrix = create_matrix(key_listed, nkey)

if choice == 'decrypt' or choice == 'd':
    try:
        kmatrix = matrix_mod_inverse(kmatrix, len(alph))
        print(f"Inverse matrix: {kmatrix}")
    except ValueError as e:
        print(f"Error: {e}")
        exit()

cyphertext = []
i = 0

while i < len(num_word):
    block = []
    for j in range(nkey):
        block.append(num_word[i])
        i += 1
    print("Block:", block)
    
    res = []
    if choice == 'decrypt' or choice == 'd':
        # Дешифрование: (block - B) * A^-1
        for j in range(nkey):
            res.append(0)
            for k in range(nkey):
                res[j] += (block[k] - b_list[k]) * kmatrix[j][k]
            res[j] = res[j] % len(alph)
            if res[j] < 0:
                res[j] += len(alph)
    else:
        # Шифрование: block * A + B
        for j in range(nkey):
            res.append(0)
            for k in range(nkey):
                res[j] += block[k] * kmatrix[j][k]
            res[j] = (res[j] + b_list[j]) % len(alph)

    print("Result:", res)
    cyphertext.append(res)

print('\nCipher matrix:', cyphertext, '\n')
cyph = []
for i in range(len(cyphertext)):
    for j in range(nkey):
        cyph.append(cyphertext[i][j] % len(alph))

print("Cipher numbers:", cyph)
result_chars = []
for num in cyph:
    result_chars.append(alph[num])
result_str = ''.join(result_chars)
print("Result:", result_str)
