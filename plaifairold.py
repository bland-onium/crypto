alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
wrong = "-_ `;:<>.,!+*^(){}[]?J"

print("insert method: 0-> encrypt; 1-> decrypt")
comand = int(input())
### kreate normal key
print("insert key")
key = str(input()).upper()
finkey = ''
for i in key:  # filling normal form of key
    if (finkey.count(i) < 1 and (i not in wrong)):
        finkey += i

### create matrix
matrix1 = ''  # matrix_fill - единица заполнения матрицы(чтобы не было выхода за допустимые границы)
for i in finkey:
    if i not in matrix1:
        matrix1 += i
for i in alphabet:
    if i not in matrix1:
        matrix1 += i
matrix = []
slice = ''; j = 0
for i in matrix1:
    if (matrix1.index(i) % 5 == 0 and matrix1.index(i) != 0):
        matrix.append(slice)  # filling final matrix as "2D" list
        slice = ''  # string which contain 5 symbols
    slice += i
matrix.append(slice)

del finkey; del slice; del matrix1; del alphabet
# more saved memory for the god of saved memory!
### text getting and normalizing
print("insert text")
first_first_text = input().upper()
first_text = ''
for i in first_first_text:
    if i not in wrong:  # deleting all punctuation differences
        first_text += i
text = ''
if len(first_text) % 2 != 0:
    first_text += 'X'  # adding "X" if we can't separate on a lot of bigramms
i = 0
while i < len(first_text):
    if len(first_text) % 2 != 0:
        first_text += 'X'
    if (first_text[i] == 'Y' and first_text[i+1] == 'Y'):
        pass
    elif (first_text[-1] == 'X' and first_text[-2] == 'X'):
        first_text = first_text.removesuffix('XX')  # deleting bigramm "XX"
    elif (first_text[i + 1] == None and first_text[i] != 'X'):  # escaping an extra "X"
        first_text += 'X'
    elif (first_text[i] == first_text[i + 1]):
        first_text = first_text[0:i + 1] + 'X' + first_text[i + 1:-1] + first_text[-1]
    text += first_text[i] + first_text[i + 1] + ' '
    i += 2
text = text.split()  # we get text as: ['SO', 'UT', 'HX']...
del first_first_text; del wrong
fintext = ''
possible_coordinates = '01234'
for i in text:
    frst = [int, int]; scnd = [int, int]
    for j in range(5):
        if (str(frst[0]) in possible_coordinates and str(scnd[0]) in possible_coordinates):
            break  # check the existing of founded coordinates
        if i[0] in matrix[j]:
            frst[0] = j; frst[1] = matrix[j].index(i[0])
        if i[1] in matrix[j]:
            scnd[0] = j; scnd[1] = matrix[j].index(i[1])

    if comand == 0:  # main part of encrypting
        if frst[0] == scnd[0]:  # if symbols on one line
            if frst[1] == 4: frst[1] = -1  # to move on another side of matrix
            if scnd[1] == 4: scnd[1] = -1
            fintext = fintext + matrix[frst[0]][frst[1] + 1] + matrix[scnd[0]][scnd[1] + 1]
            # text + symbol at right of first + symbol at right of second
            pass
        elif frst[1] == scnd[1]:  # of symbols in one column
            if frst[0] == 4: frst[0] = -1
            if scnd[0] == 4: scnd[0] = -1
            fintext = fintext + matrix[frst[0] + 1][frst[1]] + matrix[scnd[0] + 1][scnd[1]]
            # text + symbol under first + symbol under second
            pass
        else:
            fintext = fintext + matrix[frst[0]][scnd[1]] + matrix[scnd[0]][frst[1]]
            # text + symbol(x(second), y(first)) + symbol(x(first), y(second));
            # where're x, y - coordinates in matrix

    elif comand == 1:  # main part of decrypting
        # root of algorythm includes in reversing the encryptyon
        # (to be honest, this thing most of all were made by "python debugger") :))) #
        if frst[0] == scnd[0]:
            if frst[1] == 0: frst[1] = 5
            if scnd[1] == 0: scnd[1] = 5
            fintext = fintext + matrix[frst[0]][frst[1] - 1] + matrix[scnd[0]][scnd[1] - 1]
            pass
        elif frst[1] == scnd[1]:
            if frst[0] == 0: frst[0] = 5
            if scnd[0] == 0: scnd[0] = 5
            fintext = fintext + matrix[frst[0] - 1][frst[1]] + matrix[scnd[0] - 1][scnd[1]]
            pass
        else:
            fintext = fintext + matrix[frst[0]][scnd[1]] + matrix[scnd[0]][frst[1]]
        if i == text[-1] and fintext[-1] == 'X':
            fintext = fintext.removesuffix(fintext[-1])
print(fintext)

### FOR RUSSIAN LANGUAGE
"""
alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
wrong = "-_ `;:<>.,!+*^(){}[]?J"

print("insert method: 0-> encrypt; 1-> decrypt")
comand = int(input())
### kreate normal key
print("insert key")
key = str(input()).upper()
finkey = ''
for i in key:  # filling normal form of key
    if (finkey.count(i) < 1 and (i not in wrong)):
        finkey += i

### create matrix
matrix1 = ''  # matrix_fill - единица заполнения матрицы(чтобы не было выхода за допустимые границы)
for i in finkey:
    if i not in matrix1:
        matrix1 += i
for i in alphabet:
    if i not in matrix1:
        matrix1 += i
matrix = []
slice = ''; j = 0
for i in matrix1:
    if (matrix1.index(i) % 4 == 0 and matrix1.index(i) != 0):
        matrix.append(slice)  # filling final matrix as "2D" list
        slice = ''  # string which contain 5 symbols
    slice += i
matrix.append(slice)

del finkey; del slice; del matrix1; del alphabet
# more saved memory for the god of saved memory!
### text getting and normalizing
print("insert text")
first_first_text = input().upper()
first_text = ''
for i in first_first_text:
    if i not in wrong:  # deleting all punctuation differences
        first_text += i
text = ''
if len(first_text) % 2 != 0:
    first_text += 'Я'  # adding "Я" if we can't separate on a lot of bigramms
i = 0
while i < len(first_text):
    if len(first_text) % 2 != 0:
        first_text += 'Я'
    if (first_text[i] == 'Y' and first_text[i+1] == 'Y'):
        pass
    elif (first_text[-1] == 'Я' and first_text[-2] == 'Я'):
        first_text = first_text.removesuffix('ЯЯ')  # deleting bigramm "XX"
    elif (first_text[i + 1] == None and first_text[i] != 'Я'):  # escaping an extra "X"
        first_text += 'Я'
    elif (first_text[i] == first_text[i + 1]):
        first_text = first_text[0:i + 1] + 'Я' + first_text[i + 1:-1] + first_text[-1]
    text += first_text[i] + first_text[i + 1] + ' '
    i += 2
text = text.split()  # we get text as: ['SO', 'UT', 'HX']...
del first_first_text; del wrong
fintext = ''
possible_coordinates = '01234567'
for i in text:
    frst = [int, int]; scnd = [int, int]
    for j in range(8):
        if (str(frst[0]) in possible_coordinates and str(scnd[0]) in possible_coordinates):
            break  # check the existing of founded coordinates
        if i[0] in matrix[j]:
            frst[0] = j; frst[1] = matrix[j].index(i[0])
        if i[1] in matrix[j]:
            scnd[0] = j; scnd[1] = matrix[j].index(i[1])

    if comand == 0:  # main part of encrypting
        if frst[0] == scnd[0]:  # if symbols on one line
            if frst[1] == 3: frst[1] = -1  # to move on another side of matrix
            if scnd[1] == 3: scnd[1] = -1
            fintext = fintext + matrix[frst[0]][frst[1] + 1] + matrix[scnd[0]][scnd[1] + 1]
            # text + symbol at right of first + symbol at right of second
            pass
        elif frst[1] == scnd[1]:  # of symbols in one column
            if frst[0] == 7: frst[0] = -1
            if scnd[0] == 7: scnd[0] = -1
            fintext = fintext + matrix[frst[0] + 1][frst[1]] + matrix[scnd[0] + 1][scnd[1]]
            # text + symbol under first + symbol under second
            pass
        else:
            fintext = fintext + matrix[frst[0]][scnd[1]] + matrix[scnd[0]][frst[1]]
            # text + symbol(x(second), y(first)) + symbol(x(first), y(second));
            # where're x, y - coordinates in matrix

    elif comand == 1:  # main part of decrypting
        # root of algorythm includes in reversing the encryptyon
        # (to be honest, this thing most of all were made by "python debugger") :))) #
        if frst[0] == scnd[0]:
            if frst[1] == 0: frst[1] = 4
            if scnd[1] == 0: scnd[1] = 4
            fintext = fintext + matrix[frst[0]][frst[1] - 1] + matrix[scnd[0]][scnd[1] - 1]
            pass
        elif frst[1] == scnd[1]:
            if frst[0] == 0: frst[0] = 8
            if scnd[0] == 0: scnd[0] = 8
            fintext = fintext + matrix[frst[0] - 1][frst[1]] + matrix[scnd[0] - 1][scnd[1]]
            pass
        else:
            fintext = fintext + matrix[frst[0]][scnd[1]] + matrix[scnd[0]][frst[1]]
        if i == text[-1] and fintext[-1] == 'Я':
            fintext = fintext.removesuffix(fintext[-1])
print(fintext)
"""
