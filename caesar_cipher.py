alphabet = [
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]


def encrypt(word, shift, alphabet):
    encrypted_word = ""
    for letter in word:
        if letter in alphabet:
            for i in alphabet:
                if letter == i:
                    alpha_num = alphabet.index(i)
            encrypted_num = alpha_num + shift
            if encrypted_num > 25:
                encrypted_num %= 26
            encrypt_letter = alphabet[encrypted_num]
            encrypted_word += encrypt_letter
        else:
            encrypted_word += letter
    return encrypted_word


def decrypt(encrypted_word, shift, alphabet):
    decrypted_word = ""
    for letter in encrypted_word:
        if letter in alphabet:
            for i in alphabet:
                if letter == i:
                    alpha_num = alphabet.index(i)
            decrypted_num = alpha_num - shift
            if decrypted_num < 0:
                decrypted_num %= 26
            decrypt_letter = alphabet[decrypted_num]
            decrypted_word += decrypt_letter
        else:
            decrypted_word += letter
    return decrypted_word


word = input("Enter the word to encrypt: ").upper()
shift = int(input("Enter the shift: "))
encrypted_word = encrypt(word, shift, alphabet)
print(encrypted_word)

decrypted_word = decrypt(encrypted_word, shift, alphabet)
print(decrypted_word)
