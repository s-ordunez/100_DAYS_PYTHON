cipher_key = { 'a' : 1, 'b': 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6,
                   'g' : 7, 'h' : 8, 'i' : 9, 'j' : 10, 'k' : 11, 'l' : 12,
                   'm' : 13, 'n' : 14, 'o' : 15, 'p' : 16, 'q' : 17, 'r' : 18,
                   's' : 19, 't' : 20, 'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24,
                   'y' : 25, 'z' : 26}

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(og_text, shift_amt):
    encrypted_word = ''

    for char in og_text:
        if (cipher_key[char] - 1 + shift_amt) > 26 :
            encrypted_word += alphabet[cipher_key[char] - 1 + shift_amt - 26]
        else:
            encrypted_word += alphabet[cipher_key[char] - 1 + shift_amt]

    print(encrypted_word)

def decrypt(og_text, shift_amt):
    decrypted_word = ''

    for char in og_text:
        if (cipher_key[char] - 1 - shift_amt) < 0 :
            decrypted_word += alphabet[cipher_key[char] - 1 - shift_amt + 26]
        else:
            decrypted_word += alphabet[cipher_key[char] - 1 - shift_amt]

    print(decrypted_word)

#testing
encrypt('zebra', 3)
decrypt('cheud', 3)