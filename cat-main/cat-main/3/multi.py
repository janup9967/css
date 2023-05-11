def encrypt(message, key):
    ciphertext = ''
    for char in message:
        if char.isalpha():
            # convert the character to its numeric value (A=0, B=1, etc.)
            num = ord(char.upper()) - ord('A')
            # apply the encryption formula and convert back to a letter
            num = (num * key) % 26
            ciphertext += chr(num + ord('A'))
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    # find the modular multiplicative inverse of the key
    inv_key = pow(key, -1, 26)
    for char in ciphertext:
        if char.isalpha():
            # convert the character to its numeric value (A=0, B=1, etc.)
            num = ord(char.upper()) - ord('A')
            # apply the decryption formula and convert back to a letter
            num = (num * inv_key) % 26
            plaintext += chr(num + ord('A'))
        else:
            plaintext += char
    return plaintext

message = 'HELLO WORLD'
key = 7

# encrypt the message
ciphertext = encrypt(message, key)
print('Ciphertext:', ciphertext)

# decrypt the ciphertext
plaintext = decrypt(ciphertext, key)
print('Plaintext:', plaintext)

# Output
# Ciphertext: XCZZU YUPZV
# Plaintext: HELLO WORLD
