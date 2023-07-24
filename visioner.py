alphabet = 'abcdefghijklmnopqrstuvwxyz' #0-25
key = 'idontknow'  # 0-8
print("P.S. Key:", key)

print('choose what you want');print('0 - create cipher, 1 - decipher')
comand = int(input())
match comand:
    case 0:
        print("insert text to make cipher")
        text = input().lower()
        ciph = ''; cntr = -1
        for i in text:
            if i in alphabet:
                cntr += 1
                if cntr > 8: cntr -= 9
                fin_index = alphabet.index(i) + alphabet.index(key[cntr])
                if fin_index > 25:
                    fin_index = fin_index - 26
                ciph += alphabet[fin_index]
            else:
                ciph += i
        print(ciph)
    case 1:
        print("insert text to decipher")
        text = input().lower()
        deciph = ''; cntr = -1
        for i in text:
            if i in alphabet:
                cntr+=1
                if cntr > 8: cntr-=9
                fin_index = alphabet.index(i) - alphabet.index(key[cntr])
                if fin_index < 0: fin_index = fin_index + 26
                deciph = deciph + alphabet[fin_index]
            else:
                deciph = deciph + i
        print(deciph)