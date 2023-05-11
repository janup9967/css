def encrypt_text(plaintext,n):
    ans = ""
    # iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]
        
        # check if space is there then simply add space
        if ch==" ":
            ans+=" "
        # check if a character is uppercase 
        elif (ch.isupper()):
            ans += chr((ord(ch) + n-65) % 26 + 65)
        # check if a character is lowercase 
        else:
            ans += chr((ord(ch) + n-97) % 26 + 97)
    
    return ans

def dencrypt_text(plaintext,n):
    ans = ""
    # iterate over the given text
    for i in range(len(plaintext)):
        ch = plaintext[i]
        
        # check if space is there then simply add space
        if ch==" ":
            ans+=" "
        # check if a character is uppercase 
        elif (ch.isupper()):
            ans += chr((ord(ch) - n-65) % 26 + 65)
        # check if a character is lowercase 
        
        else:
            ans += chr((ord(ch) - n-97) % 26 + 97)
    
    return ans


plaintext = input("Enter the Text Message: ")
n = int(input("Enter Shift value: "))
print("Plain Text is : " + plaintext)
print("Shift pattern is : " + str(n))
text = encrypt_text(plaintext,n)
print("Encoded Text is : " + text)
print("Decoded Text is : " + dencrypt_text(text,n))

# output
# Enter the Text Message: cryptography
# Enter Shift value: 5
# Plain Text is : cryptography
# Shift pattern is : 5
# Encoded Text is : hwduytlwfumd
# Decoded Text is : cryptography

