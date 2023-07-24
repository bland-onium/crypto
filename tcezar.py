alphabet_en = 'abcdefghijklmnopqrstuvwxyz'
print('you wanna encrypt or decipher text using Tcesar?'); print('insert 0(create cipher) or 1(decipher)')
cyph_or_decyph = int(input())
if cyph_or_decyph == 0:
    print('you work with file or with text?'); print('insert 0 or 1 (0->only text; 1-> file)')
    cmd1 = int(input())
    print('insert shift'); move = int(input())
    if move > 25 or move < -26:
        move = move%26
    if move < 0:
        move = 26 + move
    match cmd1:
        case 0:
            print('insert text'); text = str(input().lower())
            fintext = ''
            for i in text:
                if i in alphabet_en:
                    num_of_symbol = alphabet_en.index(i) + move
                    if num_of_symbol > 25: num_of_symbol -= 26
                    fintext += alphabet_en[num_of_symbol]
                else: fintext += i
            print(fintext)
        case 1:
            print('write adress of file'); adress = str(input())
            text = open(adress, 'r').read().lower()
            scndtext = open(adress[:-4]+'1.txt', 'w')
            for i in text:
                if i in alphabet_en:
                    num_of_symbol = alphabet_en.index(i) + move
                    if num_of_symbol > 25: num_of_symbol-=26
                    scndtext.write(alphabet_en[num_of_symbol])
                else:
                    scndtext.write(i)
if cyph_or_decyph == 1:
    print('you work with file or with text?')
    print('insert 0 or 1 (0->only text; 1-> file)')
    cmd1 = int(input())
    print('insert shift'); move = int(input())
    if move > 25 or move < -26:
        move = move % 26
    if move < 0:
        move = 26 + move
    match cmd1:
        case 0:
            fintext = ''
            print('insert text'); text = str(input().lower())
            for i in text:
                if i in alphabet_en:
                    num_of_symbol = alphabet_en.index(i) - move
                    if num_of_symbol < 0: num_of_symbol = 26 + num_of_symbol
                    fintext += alphabet_en[num_of_symbol]
                else:
                    fintext += i
            print(fintext)
        case 1:
            print('write adress of file')
            adress = str(input())
            text = open(adress, 'r').read().lower()
            scndtext = open(adress[:-4] + '1.txt', 'w')
            for i in text:
                if i in alphabet_en:
                    num_of_symbol = alphabet_en.index(i) - move
                    if num_of_symbol < 0: num_of_symbol = 26 + num_of_symbol
                    scndtext.write(alphabet_en[num_of_symbol])
                else:
                    scndtext.write(i)